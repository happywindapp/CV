# Deployment — `c:/CV`

> Mục 2–4 là cấu hình môi trường agent, áp dụng ngay. Deploy sản phẩm điền khi có sản phẩm.

## 1. Deploy sản phẩm

Chưa có: chưa chốt (xem CV-1 trong `ai-context/working/issues-open.md`).

## 2. Sinh skills catalog

- `python ~/.claude/scripts/generate_catalogs.py --skills` — sinh catalog để agent kích hoạt skill theo `description`.
- Script lỗi → sửa & chạy lại tới khi pass (luật vận hành).

## 3. Biến môi trường agent (KHÔNG commit secrets — Quy tắc #3)

Inject qua `~/.claude/settings.json` → `env`. Danh sách biến gom **theo tier** sinh từ
`template.config.json` — xem [server-config.example.md](../../server-config.example.md) (khối `gen:env`)
và [Service Registry](../services-registry.md). Giá trị thật sống trong `server-config.md` (gitignored).

## 4. Cài dev tool

- Mọi tool dưới `C:\_devtools\<tool>\`, per-user (không admin), `PrependPath=0`, tự quản PATH ở User scope.
- Backup PATH ra file timestamp trong thư mục tool trước khi sửa env.
