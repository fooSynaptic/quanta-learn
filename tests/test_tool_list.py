"""Regression tests for reusable tool-list implementations.

These cover the modules that previously shipped with logic bugs, so the suite
doubles as a guard against regressions.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tool-list" / "algorithms"


def _load(module_name: str, relative_path: str):
    """Import a tool-list module by file path (paths are not import-safe names)."""
    spec = importlib.util.spec_from_file_location(module_name, TOOLS / relative_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_mergesort_sorts():
    merge_sort = _load("ql_merge_sort", "sorting/merge_sort.py")
    assert merge_sort.mergesort([3, 5, 4, 1, 7, 9, 2]) == [1, 2, 3, 4, 5, 7, 9]
    assert merge_sort.mergesort([1]) == [1]


def test_select_sort_sorts():
    select_sort = _load("ql_select_sort", "sorting/select_sort.py")
    assert select_sort.select_sort([6, 3, 5, 4, 1, 7, 9, 2]) == [1, 2, 3, 4, 5, 6, 7, 9]


def test_linked_list_insert_and_delete():
    mod = _load("ql_linked_list", "linked-list/MyLinkedList.py")
    ll = mod.MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    assert [ll.get(i) for i in range(3)] == [1, 2, 3]
    assert ll.sz == 3

    ll.deleteAtIndex(1)
    assert ll.get(1) == 3
    assert ll.sz == 2


def test_linked_list_out_of_range_returns_sentinel():
    mod = _load("ql_linked_list2", "linked-list/MyLinkedList.py")
    ll = mod.MyLinkedList()
    ll.addAtHead(10)
    assert ll.get(-1) == -1
    assert ll.get(5) == -1


def test_resized_array_stack_lifo():
    mod = _load(
        "ql_array_stack",
        "cs-courses/AlgorithmsFourthEdith/reSizedArrayStack.py",
    )
    stack = mod.reSizedArrayStack()
    for i in range(5):
        stack.push(i)
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2


def test_linked_stack_is_empty():
    mod = _load("ql_linked_stack", "cs-courses/AlgorithmsFourthEdith/LinkedStack.py")
    stack = mod.linkedStack()
    assert stack.isEmpty()
    stack.push(1)
    assert not stack.isEmpty()
    assert stack.pop() == 1
    assert stack.isEmpty()


def test_smo_svm_separates_linear_data():
    pytest.importorskip("numpy")
    import numpy as np

    spec = importlib.util.spec_from_file_location(
        "ql_smo_svm", ROOT / "tool-list" / "ml" / "svm" / "smo_svm.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ql_smo_svm"] = mod
    spec.loader.exec_module(mod)

    X = np.array([[2.0, 2.0], [3.0, 3.0], [-2.0, -2.0], [-3.0, -3.0]])
    y = np.array([1, 1, -1, -1])
    model = mod.SMOSVM(C=1.0, tol=1e-3, max_iter=100).fit(X, y)
    assert model.score(X, y) == 1.0
