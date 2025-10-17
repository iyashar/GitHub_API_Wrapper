import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoint(endpoint, name):
    """تابع کمکی برای تست endpointها"""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        print(f"\n{'='*50}")
        print(f"🧪 تست {name}")
        print(f"📡 Endpoint: {endpoint}")
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ موفق! پاسخ دریافت شد.")
            print(f"📦 نمونه داده: {json.dumps(data, indent=2)[:200]}...")
        else:
            print(f"❌ خطا: {response.text}")
            
    except Exception as e:
        print(f"🔥 خطا در اتصال: {e}")

def run_all_tests():
    """اجرای تمام تست‌ها"""
    print("🚀 شروع تست‌های API GitHub")
    
    # تست endpointهای مختلف
    test_endpoint("/user/octocat", "اطلاعات کاربر octocat")
    test_endpoint("/user/microsoft/repos?limit=2", "ریپازیتوری‌های مایکروسافت")
    test_endpoint("/search/repos?q=fastapi&limit=1", "جستجوی ریپازیتوری‌های FastAPI")
    test_endpoint("/rate_limit", "مشاهده rate limit")
    
    # تست خطا - کاربر ناموجود
    test_endpoint("/user/this_user_does_not_exist_12345", "کاربر ناموجود")

if __name__ == "__main__":
    run_all_tests()