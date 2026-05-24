# Problem List:
you can pr to share your own solution and discuss with me in the issues.
---

# From ximalaya & bixin
- Compute the square root of a real number `n`, keep 6 decimals. [ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/square_n.py)

- Given three circles with the centers `o` and the radius `r`, compute the area of the three, keep 6 decimals, the metric of `o` and `r`
can be arbitrary number. [ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/AreaofCricle.py)

- Check if a binary search tree is a valide balanced tree. [ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/valide_balence_BST.py)

- The 100 power of `2`(fastPower).[ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/greatPower.py)

# From byteDance
- The `k` nearest point from `(0, 0)`(cpl smaller than `nlogn`).[ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/kNear.py)

- Copy listnode with random pointer, **with cycle**.

- Given item array with length n and value array of length k, for k times, you can pick begin or end in the item array, the total value is sum of the multiply of item and value, return the highest value choices strategy. [ref solution]

# From PDD
- Path cross the most chess pieces.[ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/maxChess.py)
- Find the k larggest element from array with size N.[ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/get_k_top.py)


# From bilibili
- Given array s, return the minest index sum of three element, which their sum is K.[ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/threeSumofIndex.py)

- Given list with parent child pair, return the root of biggest linkset.[ref solution](https://github.com/fooSynaptic/exam/blob/master/interviewProblem/biggestRoot.py)





---
# un-trackable sources.
- Most Common Word 
```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.sub('[^a-z]', ' ', paragraph).split() 
        d = dict()

        for word in words:
            d[word] = d.get(word, 0) + 1

        return [x for x in sorted(d.items(), key=lambda x:x[1]) if not x[0] in banned][-1][0]
```
- Longest Palindromic Substring
