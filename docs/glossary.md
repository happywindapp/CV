# Glossary

> Thuật ngữ dùng trong repo này.

## AI tooling

| Thuật ngữ | Định nghĩa |
|-----------|-----------|
| Skill | Folder + `SKILL.md`, năng lực AI nạp động theo `description` |
| Plugin | Bó skill + commands + connectors cho 1 vai trò |
| MCP | Model Context Protocol — chuẩn kết nối AI tới tool ngoài qua `.mcp.json` |
| Catalog | Danh mục skill sinh bởi `generate_catalogs.py`, agent đọc để kích hoạt |
| Hook | Script tự động chạy before/after event, cấu hình trong `settings.json` |
| Agent / subagent | Tác nhân chuyên trách (planner, tester, code-reviewer...) trong workflow |
| Memory | Bài học file-based ở `~/.claude/projects/<workspace>/memory/`, index `MEMORY.md` |
| Work-context path | Git root của project đang sửa; truyền cho subagent thay vì CWD |

## Domain nghiệp vụ

Chưa có: chưa chốt (xem CV-1 trong `ai-context/working/issues-open.md`).
