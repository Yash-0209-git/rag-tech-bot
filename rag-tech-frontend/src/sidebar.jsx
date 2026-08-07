import React from "react";

export default function Sidebar({
  open = true,
  onToggle,
  history = [],
  onNew,
  onSelect,
  onDelete,
  currentIndex = 0,
}) {
  return (
    <aside className={`sidebar glass-card ${open ? "open" : "closed"}`}>
      <div className="sidebar-top neon-header">
        <div className="brand">
          <div className="logo">⚡</div>
          <div>
            <div className="brand-title">RAG-Tech</div>
            <div className="brand-sub">Neon Assistant</div>
          </div>
        </div>

        <div className="sidebar-actions">
          <button className="btn-primary small" onClick={onNew}>+ New</button>
          <button className="icon-btn" onClick={onToggle}>✕</button>
        </div>
      </div>

      <div className="history-list">
        {history.map((h, i) => (
          <div
            key={h.id}
            className={`history-item ${i === currentIndex ? "active" : ""}`}
            onClick={() => onSelect(i)}
          >
            <div className="hist-title">{h.title || "Chat"}</div>
            <div className="hist-meta">
              <button className="icon-mini" onClick={(e) => { e.stopPropagation(); onDelete(i); }}>🗑</button>
            </div>
          </div>
        ))}
        {history.length === 0 && <div className="empty-note">No chats yet</div>}
      </div>

      <div className="sidebar-footer">
        <div className="small-muted">Local mode — data stays on disk</div>
      </div>
    </aside>
  );
}
