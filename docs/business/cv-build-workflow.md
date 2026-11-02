# Quy trình build CV online

> Nguồn chân lý cho mọi AI/người khi tạo hoặc sửa CV trong repo này. CV mẫu: `quan_phan/` → `cv_quan_phan.html`.

## 1. Cấu trúc

| Đường dẫn | Vai trò |
|---|---|
| `<person>/cv-template.html` | Nguồn trang: nội dung + CSS + script EN/VI. Placeholder `{{FONT_CSS}}`, `{{PHOTO}}`. **Chỉ sửa ở đây.** |
| `<person>/photo.jpg` | Ảnh chân dung (~250×250, JPEG), nhúng base64 khi build. |
| `<person>/certificate/*.pdf`, `<person>/degree/*.jpg` | File được trang link tới → phải commit (`.gitignore` có ngoại lệ `!quan_phan/certificate/*.pdf`; người mới cần thêm dòng tương tự). |
| `<person>/*` khác (vd TopCV PDF) | Dữ liệu gốc, bị `*.pdf` ignore, không public. |
| `assets/fonts/bvp-{latin,vietnamese}-{400,600}.woff2` | Be Vietnam Pro (OFL), dùng chung. |
| `scripts/build-cv-html.py` | `python -I scripts/build-cv-html.py <person>` → `cv_<person>.html` ở root (1 file tự chứa). |
| `cv_<person>.html` | Output publish. **Không sửa tay** — lần build sau sẽ ghi đè. |

Publish: GitHub Pages của repo `happywindapp/CV` (nhánh `main`, root). URL phân biệt hoa thường: `https://happywindapp.github.io/CV/cv_quan_phan.html` (200), `/cv/...` → 404.

## 2. Tạo CV cho người mới

1. Tạo `<ten_nguoi>/`, copy `quan_phan/cv-template.html` làm khung, thay toàn bộ nội dung + object `VI`.
2. Đặt `photo.jpg`; file chứng chỉ/bằng cần link thì để trong `<ten_nguoi>/` và thêm ngoại lệ `.gitignore` nếu là PDF.
3. Build, verify (mục 6), đưa lệnh commit cho user tự chạy.

## 3. Design system (bản redesign 2026-11)

- Tham khảo: portfolio Brittany Chiang và các roundup developer portfolio 2026 — hero màu đậm, section đánh số, timeline card, tech chip, 1 màu nhấn.
- Token CSS ở `:root`: `--bg --surface --text --muted --line --accent --accent-strong --accent-soft --hero-*`. Light/dark tự động theo `prefers-color-scheme`; nav/hero/footer luôn tối bằng cách override token cục bộ (`.nav, .hero, footer { --bg: var(--hero-bg) ... }`).
- Mỗi CV đúng 1 màu nhấn, chọn theo nhận diện của người đó, đổi qua token (`:root`, dark, print, gradient hero, glow ảnh): Quan teal (`#0a7b70` light, `#5fd9c6` dark/hero); Serena mocha (`#8c5e45` light, `#e2b598` dark/hero, hero nâu `#2b1b14`). Không thêm màu nhấn thứ hai.
- Bo góc: card 10px (`--radius`), nút 8px, chip pill, ảnh tròn.
- Khối trang: hero (tên, chức danh, tagline, chip liên hệ, ảnh) → 4 card số liệu đè mép hero → `01 About` → `02 Experience` (timeline, card mỗi công ty, `Stack` dạng chip) → `03 Skills` (card + chip viền) → `04 Education` (card bằng có link + bảng chứng chỉ có link PDF) → footer.
- Responsive: breakpoint `@media screen and (max-width: 47.99rem)` (phải có `screen` để bản in A4 không rơi vào layout mobile); nav cuộn ngang trên mobile; ẩn nút Save PDF dưới 26rem.
- Print: `@media print` + `@page A4`, nền trắng, bỏ shadow/hiệu ứng; mục tiêu ≤ 5 trang.

## 4. Song ngữ EN/VI

- EN là HTML gốc. Phần tử cần dịch có `data-i18n="key"` (thay `innerHTML`); dịch thuộc tính dùng thêm `data-i18n-attr="alt"` / `"aria-label"`.
- Bản dịch nằm trong object `VI` của `<script>` cuối template; key `title` cho tiêu đề tab. Thiếu key → hiện EN, không lỗi.
- Không lồng phần tử `data-i18n` trong nhau. Heading chứa link → đặt `data-i18n` lên `<a>` (vd bằng thạc sĩ), nếu không link sẽ mất khi đổi ngôn ngữ.
- Nhãn cột bảng trên mobile lấy từ `thead th` đã dịch.
- Chọn ngôn ngữ: nút EN|VI, nhớ bằng `localStorage` (`cv-lang`), link trực tiếp `?lang=vi`.
- Giữ tiếng Anh ở cả bản VI: chức danh, stack/kỹ năng, tên khóa học, tên giải thưởng riêng.

## 5. Quy tắc nội dung

- Không bịa: mọi số liệu/thành tích phải có trong nguồn hoặc do user xác nhận. Wording đúng vai trò thật (vd user chỉ thiết kế vài service trong hệ thống 50+ microservice ⇒ "50+ microservices in a logistics system, as Technical Architect", không viết "architected"); giải thưởng startup ghi là của sản phẩm/hệ thống.
- Riêng tư: số điện thoại che dạng `0909 54****` (không `tel:`); không ghi ngày sinh, địa chỉ nhà; user đã bỏ thành phố. Ảnh scan bằng có ngày sinh + số hiệu — user chủ động public, nhắc lại rủi ro nếu thêm file tương tự.
- Tên (Quan Phan): EN `Quan Phan (Wyndham)`, VI `Phan Ngọc Minh Quân`; ghi chú chứng chỉ giữ tên thật để tra mã.
- Link ngoài phải kiểm tra còn sống; domain hết hạn/bán (vd `mercantilebank.com`) → chỉ ghi tên, không link.

## 6. Verify trước khi báo xong

1. **Trước khi build:** `git status` + `git log` — user hay tự commit/sửa trực tiếp `cv_*.html`. So chữ HEAD với bản sắp build; có chỉnh sửa tay thì port vào template trước.
2. Build lại, kiểm placeholder đã thay hết.
3. Headless Chrome (`C:/Program Files/Google/Chrome/Application/chrome.exe --headless=new`): desktop 1280 light + dark (`--force-dark-mode --blink-settings=preferredColorScheme=0`), `?lang=vi`.
4. Mobile 375/320: **phải** qua trang wrapper `<iframe style="width:375px">` + `--allow-file-access-from-files` (xem `ai-context/memory/headless-chrome-mobile-screenshot-needs-iframe.md`).
5. Print: `--print-to-pdf` rồi đếm `/Count`; muốn nhìn layout in thì copy HTML, đổi `@media print` → `@media all`, chụp ở bề rộng 688px.
6. `--dump-dom` với `?lang=vi`: không có `undefined`, `lang="vi"`, link vẫn còn.
7. Link file nội bộ: url-decode, file tồn tại và đã được git track.
