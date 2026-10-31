# Architecture — `c:/CV`

> Kiến trúc sản phẩm: chưa chốt (xem CV-1 trong `ai-context/working/issues-open.md`).

## Cấu trúc repo hiện tại

| Thành phần | Vai trò |
|-----------|---------|
| `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.agent/` | Config auto-load cho từng AI tool |
| `ai-context/` | Context, memory, prompts, skills dùng chung |
| `docs/` | Single source of truth |
| `plans/` | Kế hoạch triển khai + reports nội bộ |
| `scripts/`, `template.config.json`, `.template-version` | Apply/validate template, tạo junction skills |
| `CV/` | Thư mục con rỗng, chưa track trong git; vai trò chưa xác định |
