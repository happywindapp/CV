# Project Context — CV

> Mọi AI Agent ĐỌC FILE NÀY ĐẦU TIÊN. Nội dung rút từ hiện trạng `c:/CV` ngày 2026-11-01.

## Elevator pitch

Build các CV cá nhân dạng trang HTML tĩnh tự chứa, public qua GitHub Pages. Dữ liệu nguồn mỗi người nằm ở `<ten>/` (vd `quan_phan/`), trang xuất ra ở root (vd `cv_quan_phan.html`).

## Hiện trạng

- Workspace root `c:/CV` **chính là git repo** GitHub `happywindapp/CV`, nhánh `main`.
- Local chưa có commit; remote trống.
- Chỉ có scaffold AI (template v1.0.0) + thư mục con `CV/` rỗng, chưa rõ vai trò.

## Kiến trúc high-level

Chưa có. Điền khi chốt stack.

## Repos

| Repo | Vị trí | Vai trò |
|------|--------|---------|
| `CV` | `c:/CV` (chính là workspace root) | GitHub `happywindapp/CV`, nhánh `main` |

## Hệ ngoài

Chưa có.

## Ranh giới & nguyên tắc

- Scaffold AI nằm chung repo với sản phẩm; junction `*/skills` gitignored, clone mới chạy `pwsh -File scripts/link-shared-skills.ps1`.
- DB luôn **READ-ONLY**. Git commit/push do user tự chạy.

## Đang vướng

Xem [`ai-context/working/issues-open.md`](working/issues-open.md).

## Trỏ tới chi tiết

- Mục lục: `docs/INDEX.md`
- Quyết định đã chốt: `docs/decisions/`
- Workflow vận hành AI: `docs/business/`
