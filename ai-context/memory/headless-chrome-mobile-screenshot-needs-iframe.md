# Chụp mobile bằng Chrome headless: dùng wrapper iframe

**Triệu chứng:** `chrome --headless=new --window-size=375,900 --screenshot=...` cho ảnh trang như bị tràn ngang (chữ hero bị cắt mép phải) dù CSS responsive đúng.

**Nguyên nhân:** cửa sổ Chrome có bề rộng tối thiểu (~500px), layout viewport rộng hơn 375 nhưng ảnh chỉ chụp 375px.

**Cách xử lý đúng:** tạo trang wrapper chứa `<iframe src="file:///C:/CV/cv_quan_phan.html" style="width:375px;height:1100px;border:0">` (có thể đặt nhiều iframe 375/320 cạnh nhau), chụp wrapper với `--allow-file-access-from-files`.
