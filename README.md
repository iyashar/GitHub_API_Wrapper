# 🚀 GitHub API Wrapper

یک API بسیط و قدرتمند ساخته شده با **FastAPI** برای تعامل با **GitHub API** که دسترسی آسان به اطلاعات کاربران، ریپازیتوری‌ها و جستجو را فراهم می‌کند.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub_API-181717?style=for-the-badge&logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## ✨ ویژگی‌ها

- 🎯 **دسترسی آسان** به GitHub API
- ⚡ **سریع و کارآمد** با FastAPI
- 📚 **مستندات خودکار** با Swagger UI
- 🎨 **ظاهر زیبا و ریسپانسیو**
- 🔒 **مدیریت خطاهای پیشرفته**
- 📊 **پشتیبانی از rate limiting**
- 🔍 **جستجوی پیشرفته ریپازیتوری‌ها**


## 🛠️ نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.7+
- pip

### مرحله ۱: کلون کردن ریپازیتوری

```bash
git clone https://github.com/your-username/github-api-wrapper.git
cd github-api-wrapper
```

### مرحله 2: نصب نیازمندی ها
```bash
pip install -r requirements.txt
```
### مرحله 3: اجرای برنامه
```bash
# روش ۱: مستقیم
python github_api.py

# روش ۲: با uvicorn (بهترین روش)
uvicorn github_api:app --reload --host 0.0.0.0 --port 8000

# روش ۳: با فایل اجرایی
python run.py
```

### مرحله ۴: بررسی اجرای برنامه
```bash
بروید به: http://localhost:8000

```
### مرحله 5: 🧪 تست کردن
```bash
# تست خودکار
python test_api.py
```
### تست دستی
```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/user/octocat
```

### 🐛 عیب‌یابی
#### مشکل: {"detail":"Not Found"}
مطمئن شوید سرور در حال اجراست
آدرس endpoint را بررسی کنید
#### مشکل: اتصال به GitHub
اتصال اینترنت را بررسی کنید
می توانید GitHub Token را تنظیم کنید

### 🤝 مشارکت
ریپازیتوری را fork کنید
یک branch جدید ایجاد کنید
تغییرات را commit کنید
نهایتا Pull Request ایجاد کنید

### 📄 لایسنس
این پروژه تحت لایسنس MIT منتشر شده است.
