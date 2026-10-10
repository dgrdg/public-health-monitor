# ۱. استفاده از ایمیج رسمی و سبک پایتون نسخه 3.9
FROM mcr.microsoft.com/mirror/docker/library/python:3.11-slim

# ۲. تعیین دایرکتوری کاری داخل کانتینر
WORKDIR /app

# ۳. کپی کردن فایل نیازمندی‌ها به داخل کانتینر
COPY requirements.txt .

# ۴. نصب پکیج‌ها و کتابخانه‌های مورد نیاز
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ۵. کپی کردن سایر فایل‌های پروژه (مثل app.py) به داخل کانتینر
COPY . .

# ۶. تعیین دستور پیش‌فرض برای زمان اجرای کانتینر
CMD ["python", "app.py"]
