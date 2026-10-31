# Server Config (EXAMPLE)

> Copy file này thành `server-config.md` (đã gitignore) rồi điền giá trị thật của bạn.
> TUYỆT ĐỐI KHÔNG commit `server-config.md`. File này chỉ liệt kê TÊN biến, không có giá trị.
>
> Bảng dưới sinh từ `template.config.json` (services + datastores + messaging) qua
> `pwsh scripts/apply-template.ps1` — đừng sửa tay phần giữa marker `gen:env`.

## Biến môi trường theo tier

<!-- BEGIN gen:env -->
**datastore**

| Store | Env vars |
|-------|----------|

**messaging**

| Type | Env var |
|------|---------|
<!-- END gen:env -->

## Notes

- `{{host}}` / `{{port}}` là placeholder điền khi copy sang `server-config.md` thật.
- Mọi giá trị nhạy cảm sống trong `server-config.md` (gitignored) hoặc secret manager.
- Không hardcode credentials vào code/docs.
