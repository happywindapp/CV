# Build lại CV có thể đè chỉnh sửa user vừa commit

**Triệu chứng:** sau khi AI build lại `cv_quan_phan.html` từ template, các thay đổi user đã tự làm và commit (link PDF chứng chỉ, bỏ cột Hours, link bằng — commit `48cbeaa`) biến mất trong working copy; user phải yêu cầu lại.

**Nguyên nhân:** template build là nguồn riêng; user sửa thẳng file output `cv_*.html` (hoặc qua AI/tool khác) nên template không biết. Build = ghi đè toàn bộ file.

**Cách xử lý đúng:**
1. Trước mỗi lần build: `git status`, `git log -3 -- cv_<person>.html`.
2. So nội dung chữ HEAD với bản sắp build (strip `<style>`, `<script>`, tag, so danh sách từ); khác biệt ngoài thay đổi mình định làm ⇒ port vào `<person>/cv-template.html` trước.
3. Chỉ sửa template; nhắc user không sửa tay `cv_*.html`.
