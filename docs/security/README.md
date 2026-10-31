# Security — `c:/CV`

> Repo chưa có sản phẩm nên chưa có auth flow. Hiện tại "Security" = **guardrails vận hành AI** + **xử lý secrets**.
> Nguồn sự thật: `~/.claude/CLAUDE.md`, `~/.claude/rules/*`, `~/.claude/.ckignore`.

## 1. Guardrails cứng (agent BẮT BUỘC tuân thủ)

| Luật | Nội dung | Nguồn |
|------|----------|-------|
| **DB READ-ONLY** | Chỉ `SELECT`/`SHOW`/`EXPLAIN`/metadata. Mọi INSERT/UPDATE/DELETE/DDL → viết SQL cho user TỰ chạy, kể cả khi user ra lệnh trực tiếp | `~/.claude/CLAUDE.md` |
| **Git thủ công** | KHÔNG tự `git commit`/`git push`. Chuẩn bị xong → đưa lệnh/message cho user | `~/.claude/CLAUDE.md` |
| **Editing scope** | Chỉ đụng dòng cần cho task; không drive-by reformat/cleanup | `~/.claude/CLAUDE.md` |
| **Cài tool per-user** | Dưới `C:\_devtools\<tool>\`, không admin; backup PATH trước khi sửa env | `~/.claude/CLAUDE.md` |

## 2. Xử lý secrets (Quy tắc #3 — inventory, KHÔNG copy giá trị)

**File nhạy cảm — chỉ tham chiếu, KHÔNG đưa giá trị vào docs/commit:**

| File | Chứa gì | Trạng thái |
|------|---------|-----------|
| `server-config.md` | Giá trị env thật (chưa có file này) | Gitignored, KHÔNG commit |
| `~/.claude/settings.json` → `env` | Biến inject vào shell agent | Local, không commit |

**Quy tắc khi tài liệu hoá:** liệt kê TÊN biến/endpoint, KHÔNG bao giờ chép password/token. Khi cần kết nối → trỏ tới `server-config.md`.

## 3. Context-safety (`.ckignore`)

- Chặn đọc thư mục nặng (`node_modules`, `.git`, `vendor`, `target`, `dist`, `.venv`...) để không bơm rác vào context LLM.
- `.env`/`.env.*` được phép đọc (`!` prefix) — nhưng vẫn áp Quy tắc #3 khi trích xuất.

## 4. Chưa áp dụng

- Auth flow (OAuth/JWT/session), permission matrix role×resource, rate limiting: điền khi sản phẩm cần.
