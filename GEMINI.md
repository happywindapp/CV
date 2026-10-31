# GEMINI.md — Workspace `c:/CV` (CV)

> [AUTO-LOAD] Gemini CLI (v0.1.6+) **và Google Antigravity** đọc tự động (Antigravity ưu tiên file này hơn `AGENTS.md`).
> Nội dung đồng bộ `CLAUDE.md` — giữ ngắn. Antigravity còn nạp `.agent/rules/*` + `.agent/workflows/*`.

## Workspace là gì

`c:/CV` **chính là git repo** `happywindapp/CV` (nhánh `main`). Hiện chỉ có scaffold AI, chưa có code/nội dung; mục đích + tech stack chưa chốt (xem CV-1 trong `ai-context/working/issues-open.md`).
Đọc `ai-context/project-context.md` đầu tiên.

## Tech stack

- **Sản phẩm:** chưa chốt — điền khi có code, không suy đoán từ tên repo.
- **Scaffold AI:** Markdown (`docs/`, `ai-context/`), PowerShell (`scripts/`).

## Naming & clean code

- File kebab-case mô tả rõ mục đích. Code theo convention ngôn ngữ (Go snake_case, C# PascalCase).
- YAGNI · KISS · DRY. Diff hẹp. Comment tối thiểu (mặc định không comment). File < ~200 dòng.

## Guardrails

- DB **READ-ONLY** (chỉ SELECT/metadata).
- KHÔNG tự `git commit`/`git push` — đưa lệnh cho user.
- **Giải thích song ngữ:** kỹ thuật/pattern/khái niệm quan trọng ghi `English term (thuật ngữ tiếng Việt)`, chỉ thuật ngữ then chốt, lần đầu nhắc. Chi tiết: `ai-context/memory/bilingual-technique-names-in-explanations.md`.
- PR description theo chuẩn `ai-context/prompts/pr-description.md` (fix bug vs feature mới khác nhau).
- Skill cá nhân → `~/.claude/skills/`; skill dùng chung project → `ai-context/skills/` (junction `.gemini/skills/`). Cài tool → `C:\_devtools\`.

## Điều hướng

1. `ai-context/project-context.md` 2. `docs/INDEX.md` 3. `ai-context/working/sprint-current.md` 4. `ai-context/memory/` 5. `.agent/` (rules + workflows cho Antigravity)

