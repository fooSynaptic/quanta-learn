let state = { data: null, categoryFilter: null, selectedId: null, solvedTopicFilter: null, selectedSolvedId: null, selectedProblemId: null };
let dragMoved = false;

const READING_COLS = [
  { key: "inbox", label: "待处理" },
  { key: "active", label: "进行中" },
  { key: "done", label: "已消化" },
];

const STATUS_LABEL = {
  inbox: "待处理",
  active: "进行中",
  done: "已消化",
  archived: "归档",
};

const CATEGORY_LABEL = {
  unknown: "未分类",
  reading: "阅读",
  algorithm: "算法",
  debug: "调试",
  "system-design": "系统设计",
  other: "其他",
};

async function loadData() {
  const res = await fetch("/api/data");
  state.data = await res.json();
  render();
  if (state.selectedId) {
    showDetail(state.selectedId, false);
  }
}

function toast(msg) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.classList.remove("hidden");
  setTimeout(() => el.classList.add("hidden"), 2800);
}

function catLabel(cat) {
  return CATEGORY_LABEL[cat] || cat;
}

function renderStats() {
  const s = state.data.stats;
  const el = document.getElementById("stats");
  const cards = [
    ["阅读待消化", s.reading_pending, "wip", "reading"],
    ["阅读已消化", s.reading_done, "done", "reading"],
    ["消化率", `${(s.reading_digest_rate * 100).toFixed(0)}%`, "", "reading"],
    ["问题未解决", s.problem_open, "wip", "problem"],
    ["问题已解决", s.problem_solved, "done", "problem"],
    ["题解库", s.solved_count, "done", "solved"],
    ["工具", s.tool_count, "", "solved"],
  ];
  el.innerHTML = cards
    .map(
      ([label, val, cls, tab]) =>
        `<div class="stat ${cls}" data-tab="${tab}"><span>${label}</span><strong>${val}</strong></div>`
    )
    .join("");
  el.querySelectorAll(".stat").forEach((node) => {
    node.addEventListener("click", () => switchTab(node.dataset.tab));
  });
}

function switchTab(name) {
  document.querySelectorAll(".tab").forEach((t) => {
    t.classList.toggle("active", t.dataset.tab === name);
  });
  document.querySelectorAll(".panel").forEach((p) => {
    p.classList.toggle("active", p.id === `panel-${name}`);
  });
}

function renderCategoryFilters() {
  const by = state.data.stats.reading_by_category || {};
  const el = document.getElementById("reading-filters");
  const entries = Object.entries(by).sort((a, b) => b[1] - a[1]);
  el.innerHTML =
    `<button type="button" class="chip ${state.categoryFilter ? "" : "active"}" data-cat="">全部</button>` +
    entries
      .map(
        ([cat, n]) =>
          `<button type="button" class="chip ${state.categoryFilter === cat ? "active" : ""}" data-cat="${cat}">${catLabel(cat)} (${n})</button>`
      )
      .join("");
  el.querySelectorAll(".chip").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.categoryFilter = btn.dataset.cat || null;
      renderCategoryFilters();
      renderKanban();
    });
  });
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function cardHtml(item) {
  const match =
    item.has_tool_match || item.has_solved_match
      ? '<span class="badge match">已关联</span>'
      : "";
  const cat = item.category || "unknown";
  const sub = item.url_preview || item.path_short || item.domain || "（无链接）";
  const selected = state.selectedId === item.id ? " selected" : "";
  return `<div class="card${selected}" draggable="true" data-id="${item.id}" data-status="${item.status}">
    <div class="title">${escapeHtml(item.title || item.id)}</div>
    <div class="subtitle">${escapeHtml(sub)}</div>
    <div class="meta">
      <span class="badge ${cat}">${catLabel(cat)}</span>
      <span class="badge">${STATUS_LABEL[item.status] || item.status}</span>
      ${item.domain ? `<span class="badge">${escapeHtml(item.domain)}</span>` : ""}
      ${match}
    </div>
  </div>`;
}

function filterItems(items) {
  if (!state.categoryFilter) return items;
  return items.filter((i) => i.category === state.categoryFilter);
}

async function setReadingStatus(id, status) {
  const res = await fetch(`/api/reading/${id}/status`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status }),
  });
  if (!res.ok) throw new Error(await res.text());
  await loadData();
  toast(`已设为：${STATUS_LABEL[status] || status}`);
}

async function showDetail(id, scrollPanel = true) {
  state.selectedId = id;
  document.querySelectorAll(".card[data-id]").forEach((c) => {
    c.classList.toggle("selected", c.dataset.id === id);
  });

  const panel = document.getElementById("detail-panel");
  panel.innerHTML = "<p class=\"detail-placeholder\">加载中…</p>";

  try {
    const res = await fetch(`/api/reading/${id}/detail`);
    if (!res.ok) throw new Error("not found");
    const item = await res.json();
    const url = item.url || "";
    const urlBlock = url.startsWith("http")
      ? `<div class="url-box"><a href="${escapeHtml(url)}" target="_blank" rel="noopener">${escapeHtml(url)}</a></div>`
      : `<div class="url-box">${escapeHtml(url || "（无 URL，可能仅为历史记录或本地路径）")}</div>`;

    const rel = item.related || {};
    const relHtml = [
      rel.tools?.length ? `工具：${rel.tools.join(", ")}` : "",
      rel.solved?.length ? `题解：${rel.solved.join(", ")}` : "",
      rel.problems?.length ? `问题：${rel.problems.join(", ")}` : "",
    ]
      .filter(Boolean)
      .join("<br>") || "—";

    panel.innerHTML = `
      <h2>${escapeHtml(item.title || item.id)}</h2>
      <dl>
        <dt>当前状态</dt>
        <dd>${STATUS_LABEL[item.status] || item.status}</dd>
        <dt>分类</dt>
        <dd>${catLabel(item.category || "unknown")}</dd>
        <dt>来源</dt>
        <dd>${escapeHtml(item.source || "—")}</dd>
        <dt>书签路径</dt>
        <dd>${escapeHtml(item.source_path || "—")}</dd>
        <dt>链接</dt>
        <dd>${urlBlock}</dd>
        <dt>摘要</dt>
        <dd>${escapeHtml(item.summary || "—")}</dd>
        <dt>标签</dt>
        <dd>${(item.tags || []).map(escapeHtml).join(", ") || "—"}</dd>
        <dt>关联</dt>
        <dd>${relHtml}</dd>
        <dt>时间</dt>
        <dd>收录 ${escapeHtml(item.captured_at || "—")} · 最近 ${escapeHtml(item.last_seen || item.updated_at || "—")}</dd>
      </dl>
      <dt>移动到</dt>
      <div class="status-actions">
        ${["inbox", "active", "done", "archived"]
          .map(
            (st) =>
              `<button type="button" data-status="${st}" class="${item.status === st ? "active" : ""}">${STATUS_LABEL[st]}</button>`
          )
          .join("")}
      </div>
    `;

    panel.querySelectorAll(".status-actions button").forEach((btn) => {
      btn.addEventListener("click", async () => {
        try {
          await setReadingStatus(id, btn.dataset.status);
        } catch (e) {
          toast("更新失败");
          console.error(e);
        }
      });
    });

    if (scrollPanel && window.matchMedia("(max-width: 1024px)").matches) {
      panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }
  } catch (e) {
    panel.innerHTML = "<p class=\"detail-placeholder\">加载详情失败</p>";
    console.error(e);
  }
}

function setupColumnDnD(colEl, targetStatus) {
  colEl.addEventListener("dragover", (e) => {
    e.preventDefault();
    colEl.classList.add("drag-over");
  });
  colEl.addEventListener("dragleave", () => colEl.classList.remove("drag-over"));
  colEl.addEventListener("drop", async (e) => {
    e.preventDefault();
    colEl.classList.remove("drag-over");
    const id = e.dataTransfer.getData("text/plain");
    if (!id) return;
    try {
      await setReadingStatus(id, targetStatus);
      if (state.selectedId === id) showDetail(id, false);
    } catch (err) {
      toast("更新失败");
      console.error(err);
    }
  });
}

function bindCards(root) {
  root.querySelectorAll(".card[data-id]").forEach((card) => {
    card.addEventListener("dragstart", (e) => {
      dragMoved = false;
      card.classList.add("dragging");
      e.dataTransfer.setData("text/plain", card.dataset.id);
    });
    card.addEventListener("drag", () => {
      dragMoved = true;
    });
    card.addEventListener("dragend", () => {
      card.classList.remove("dragging");
    });
    card.addEventListener("click", () => {
      if (dragMoved) return;
      showDetail(card.dataset.id);
    });
  });
}

function renderKanban() {
  const q = state.data.reading_queues;
  const kanban = document.getElementById("kanban");
  kanban.innerHTML = READING_COLS.map(
    ({ key, label }) => `
    <div class="kanban-col" data-status="${key}">
      <h3>${label} (${filterItems(q[key] || []).length})</h3>
      <div class="col-body" id="body-${key}"></div>
    </div>`
  ).join("");

  READING_COLS.forEach(({ key }) => {
    const body = document.getElementById(`body-${key}`);
    const items = filterItems(q[key] || []);
    body.innerHTML = items.map((i) => cardHtml(i)).join("");
    setupColumnDnD(body.closest(".kanban-col"), key);
    bindCards(body);
  });

  const archived = filterItems(q.archived || []);
  document.getElementById("archived-count").textContent = String(archived.length);
  const archCol = document.getElementById("col-archived");
  archCol.innerHTML = archived.map((i) => cardHtml(i)).join("");
  setupColumnDnD(archCol, "archived");
  bindCards(archCol);
}

function renderProblems() {
  const q = state.data.problem_queues;
  const openEl = document.getElementById("problem-open");
  const solvedEl = document.getElementById("problem-solved");
  openEl.innerHTML = (q.open || []).map((i) => problemCard(i)).join("");
  solvedEl.innerHTML = (q.solved || []).map((i) => problemCard(i)).join("");
  bindProblemCards(openEl);
  bindProblemCards(solvedEl);
}

function bindProblemCards(root) {
  root.querySelectorAll(".card[data-id]").forEach((card) => {
    card.addEventListener("click", () => showProblemDetail(card.dataset.id));
  });
}

async function showProblemDetail(id) {
  state.selectedProblemId = id;
  const panel = document.getElementById("problem-detail-panel");
  panel.innerHTML = '<p class="detail-placeholder">加载中…</p>';
  try {
    const res = await fetch(`/api/problem/${id}/detail`);
    if (!res.ok) throw new Error("not found");
    const item = await res.json();
    const rel = item.related || {};
    panel.innerHTML = `
      <h2>${escapeHtml(item.title || item.id)}</h2>
      <dl>
        <dt>状态</dt><dd>${escapeHtml(item.status || "—")}</dd>
        <dt>类型</dt><dd>${escapeHtml(item.kind || "—")}</dd>
        <dt>来源</dt><dd>${escapeHtml(item.source || "—")}</dd>
        <dt>优先级</dt><dd>${escapeHtml(item.priority || "—")}</dd>
        <dt>引用</dt><dd>${escapeHtml(item.source_ref || "—")}</dd>
        <dt>笔记路径</dt><dd>${escapeHtml(item.path || "—")}</dd>
        <dt>备注</dt><dd>${escapeHtml(item.notes || "—")}</dd>
        <dt>关联阅读</dt><dd>${(rel.reading || []).join(", ") || "—"}</dd>
        <dt>关联题解</dt><dd>${(rel.solved_similar || []).join(", ") || "—"}</dd>
      </dl>`;
  } catch (e) {
    panel.innerHTML = '<p class="detail-placeholder">加载失败</p>';
  }
}

function problemCard(item) {
  const sel = state.selectedProblemId === item.id ? " selected" : "";
  return `<div class="card${sel}" data-id="${item.id}">
    <div class="title">${escapeHtml(item.title)}</div>
    <div class="meta">
      <span class="badge">${item.kind || ""}</span>
      <span class="badge">${item.status}</span>
      <span class="badge">${item.priority || ""}</span>
    </div>
  </div>`;
}

function renderSolvedTopicFilters() {
  const list = state.data.solved_list || [];
  const counts = {};
  list.forEach((i) => {
    (i.topics || []).forEach((t) => {
      counts[t] = (counts[t] || 0) + 1;
    });
  });
  const el = document.getElementById("solved-topic-filters");
  const entries = Object.entries(counts).sort((a, b) => b[1] - a[1]);
  el.innerHTML =
    `<button type="button" class="chip ${state.solvedTopicFilter ? "" : "active"}" data-topic="">全部主题</button>` +
    entries
      .map(
        ([t, n]) =>
          `<button type="button" class="chip ${state.solvedTopicFilter === t ? "active" : ""}" data-topic="${escapeHtml(t)}">${escapeHtml(t)} (${n})</button>`
      )
      .join("");
  el.querySelectorAll(".chip").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.solvedTopicFilter = btn.dataset.topic || null;
      renderSolvedTopicFilters();
      renderSolved();
    });
  });
}

function filterSolved(list) {
  if (!state.solvedTopicFilter) return list;
  return list.filter((i) => (i.topics || []).includes(state.solvedTopicFilter));
}

async function showSolvedDetail(id) {
  state.selectedSolvedId = id;
  document.querySelectorAll("#solved-list .card").forEach((c) => {
    c.classList.toggle("selected", c.dataset.id === id);
  });
  const panel = document.getElementById("solved-detail-panel");
  panel.innerHTML = '<p class="detail-placeholder">加载中…</p>';
  try {
    const res = await fetch(`/api/solved/${id}/detail`);
    if (!res.ok) throw new Error("not found");
    const item = await res.json();
    const rel = item.related || {};
    const paths = (item.paths || [])
      .map((p) => `<li><code>${escapeHtml(p)}</code></li>`)
      .join("");
    const topics = (item.topics || [])
      .map((t) => `<span class="badge topic-chip" data-topic="${escapeHtml(t)}">${escapeHtml(t)}</span>`)
      .join(" ");
    panel.innerHTML = `
      <h2>${escapeHtml(item.title || item.id)}</h2>
      <dl>
        <dt>主题 topics</dt>
        <dd>
          <div class="meta">${topics || "—"}</div>
          <p class="hint">topics 是知识点标签（如 tree、dp、sorting），用于匹配阅读材料和待办。</p>
        </dd>
        <dt>语言</dt><dd>${escapeHtml(item.language || "—")}</dd>
        <dt>质量</dt><dd>${escapeHtml(item.quality || "—")}</dd>
        <dt>来源</dt><dd>${escapeHtml(item.source || "—")}</dd>
        <dt>代码路径</dt><dd><ul class="path-list">${paths || "<li>—</li>"}</ul></dd>
        <dt>摘要</dt><dd>${escapeHtml(item.summary || "—")}</dd>
        <dt>变体</dt><dd>${(item.variants || []).map(escapeHtml).join(", ") || "—"}</dd>
        <dt>关联工具</dt><dd>${(rel.tools || []).join(", ") || "—"}</dd>
        <dt>关联阅读</dt><dd>${(rel.reading || []).join(", ") || "—"}</dd>
        <dt>时间</dt><dd>${escapeHtml(item.updated_at || item.created_at || "—")}</dd>
      </dl>`;
    panel.querySelectorAll(".topic-chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        state.solvedTopicFilter = chip.dataset.topic;
        renderSolvedTopicFilters();
        renderSolved();
      });
    });
  } catch (e) {
    panel.innerHTML = '<p class="detail-placeholder">加载失败</p>';
  }
}

function renderSolved() {
  const list = filterSolved(state.data.solved_list || []);
  const el = document.getElementById("solved-list");
  el.innerHTML = list
    .map((i) => {
      const sel = state.selectedSolvedId === i.id ? " selected" : "";
      const topics = (i.topics || [])
        .map(
          (t) =>
            `<span class="badge topic-chip" data-topic="${escapeHtml(t)}" title="点击按主题筛选">${escapeHtml(t)}</span>`
        )
        .join("");
      const sub = i.path_preview
        ? `${escapeHtml(i.path_preview)}${i.path_count > 1 ? ` 等 ${i.path_count} 个文件` : ""}`
        : "";
      return `<div class="card${sel}" data-id="${i.id}">
        <div class="title">${escapeHtml(i.title)}</div>
        ${sub ? `<div class="subtitle">${sub}</div>` : ""}
        <div class="meta">${topics}
          <span class="badge">${escapeHtml(i.language || "")}</span>
          <span class="badge">${escapeHtml(i.source || "")}</span>
        </div>
      </div>`;
    })
    .join("");

  el.querySelectorAll(".card[data-id]").forEach((card) => {
    card.addEventListener("click", () => showSolvedDetail(card.dataset.id));
  });
  el.querySelectorAll(".topic-chip").forEach((chip) => {
    chip.addEventListener("click", (e) => {
      e.stopPropagation();
      state.solvedTopicFilter = chip.dataset.topic;
      renderSolvedTopicFilters();
      renderSolved();
      toast(`已筛选主题：${chip.dataset.topic}`);
    });
  });
}

function render() {
  renderStats();
  renderCategoryFilters();
  renderKanban();
  renderProblems();
  renderSolvedTopicFilters();
  renderSolved();
}

document.querySelectorAll(".tab").forEach((btn) => {
  btn.addEventListener("click", () => switchTab(btn.dataset.tab));
});
document.getElementById("btn-refresh").addEventListener("click", loadData);

loadData().catch((e) => {
  toast("加载失败");
  console.error(e);
});
