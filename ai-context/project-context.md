# Project Context — CV

> Mọi AI Agent ĐỌC FILE NÀY ĐẦU TIÊN. Cập nhật 2026-11-03.

## Elevator pitch

Build các CV cá nhân dạng trang HTML tĩnh tự chứa, song ngữ EN/VI, public qua GitHub Pages. Nguồn mỗi người nằm ở `<ten>/` (vd `quan_phan/`), trang xuất ra ở root (vd `cv_quan_phan.html`).

## Hiện trạng

- Workspace root `c:/CV` **chính là git repo** GitHub `happywindapp/CV`, nhánh `main`; GitHub Pages bật ở root.
- CV đã có: Quan Phan — `quan_phan/` → `cv_quan_phan.html`, live tại `https://happywindapp.github.io/CV/cv_quan_phan.html` (path phân biệt hoa thường).
- User tự commit/push, thường commit thẳng `cv_*.html` ngay sau mỗi lượt sửa.

## Kiến trúc high-level

`<person>/cv-template.html` + `<person>/photo.jpg` + `assets/fonts/` → `python -I scripts/build-cv-html.py <person>` → `cv_<person>.html` (1 file HTML+CSS+JS, font và ảnh nhúng base64, không dependency). Chi tiết: [`docs/business/cv-build-workflow.md`](../docs/business/cv-build-workflow.md).

## Repos

| Repo | Vị trí | Vai trò |
|------|--------|---------|
| `CV` | `c:/CV` (chính là workspace root) | GitHub `happywindapp/CV`, nhánh `main`, GitHub Pages |

## Hệ ngoài

- GitHub Pages (hosting tĩnh).
- `verify.csc.edu.vn` — tra mã chứng chỉ được link từ CV.

## Ranh giới & nguyên tắc

- Chỉ sửa `cv-template.html`, không sửa tay `cv_*.html` (build ghi đè).
- Trước khi build: kiểm `git log` + so nội dung với HEAD để không đè chỉnh sửa của user.
- Không bịa nội dung CV; che thông tin cá nhân (SĐT, ngày sinh, địa chỉ).
- Scaffold AI nằm chung repo với sản phẩm; junction `*/skills` gitignored, clone mới chạy `pwsh -File scripts/link-shared-skills.ps1`.
- Git commit/push do user tự chạy.

## Đang vướng

Xem [`ai-context/working/issues-open.md`](working/issues-open.md).

## Trỏ tới chi tiết

- Mục lục: `docs/INDEX.md`
- Quy trình CV: `docs/business/cv-build-workflow.md`
- Quyết định đã chốt: `docs/decisions/`
- Workflow vận hành AI: `docs/business/`
