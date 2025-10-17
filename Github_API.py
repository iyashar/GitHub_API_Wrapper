from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
import requests
import os
from typing import Optional

app = FastAPI(
    title="GitHub API Wrapper",
    description="یک API بسیط برای تعامل با GitHub API",
    version="2.0.0"
)

# توکن دسترسی GitHub (اختیاری - برای rate limit بالاتر)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else "",
    "Accept": "application/vnd.github.v3+json"
}

@app.get("/", response_class=HTMLResponse)
async def root():
    """صفحه اصلی API با ظاهر زیبا"""
    return """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GitHub API Wrapper</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 40px 20px;
                color: #333;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            
            .header {
                text-align: center;
                margin-bottom: 50px;
                color: white;
            }
            
            .header h1 {
                font-size: 3rem;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            .header p {
                font-size: 1.2rem;
                opacity: 0.9;
            }
            
            .cards-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 25px;
                margin-bottom: 40px;
            }
            
            .endpoint-card {
                background: white;
                border-radius: 15px;
                padding: 25px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border-left: 5px solid #667eea;
            }
            
            .endpoint-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 40px rgba(0,0,0,0.3);
            }
            
            .card-header {
                display: flex;
                align-items: center;
                margin-bottom: 15px;
            }
            
            .card-icon {
                font-size: 2rem;
                margin-left: 15px;
                width: 50px;
                height: 50px;
                background: #667eea;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            
            .card-title {
                font-size: 1.4rem;
                color: #2d3748;
                font-weight: 600;
            }
            
            .card-description {
                color: #666;
                margin-bottom: 20px;
                line-height: 1.6;
            }
            
            .endpoint-url {
                background: #f7fafc;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                padding: 12px 15px;
                font-family: 'Courier New', monospace;
                color: #2d3748;
                margin-bottom: 15px;
                direction: ltr;
                text-align: left;
            }
            
            .example-link {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
                text-decoration: none;
                transition: background 0.3s ease;
                font-size: 0.9rem;
            }
            
            .example-link:hover {
                background: #5a67d8;
            }
            
            .footer {
                text-align: center;
                margin-top: 50px;
                color: white;
            }
            
            .docs-link {
                display: inline-flex;
                align-items: center;
                background: rgba(255,255,255,0.2);
                color: white;
                padding: 12px 24px;
                border-radius: 25px;
                text-decoration: none;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.3);
            }
            
            .docs-link:hover {
                background: rgba(255,255,255,0.3);
                transform: scale(1.05);
            }
            
            .method-get {
                border-left-color: #48bb78;
            }
            
            .method-get .card-icon {
                background: #48bb78;
            }
            
            .health-status {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
                text-align: center;
                color: white;
            }
            
            .status-badge {
                display: inline-block;
                background: #48bb78;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9rem;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 GitHub API Wrapper</h1>
                <p>یک API بسیط و قدرتمند برای دسترسی به اطلاعات GitHub</p>
            </div>
            
            <div class="health-status">
                <h3>✅ وضعیت سرویس: فعال</h3>
                <div class="status-badge">هم اکنون در حال اجرا</div>
            </div>
            
            <div class="cards-grid">
                <div class="endpoint-card method-get">
                    <div class="card-header">
                        <div class="card-icon">👤</div>
                        <h3 class="card-title">اطلاعات کاربر</h3>
                    </div>
                    <p class="card-description">دریافت اطلاعات پایه هر کاربر GitHub شامل نام، بیو، تعداد ریپازیتوری‌ها و...</p>
                    <div class="endpoint-url">GET /api/user/{username}</div>
                    <a href="/api/user/iYashar" class="example-link">مثال: کاربر iYashar</a>
                </div>
                
                <div class="endpoint-card method-get">
                    <div class="card-header">
                        <div class="card-icon">📂</div>
                        <h3 class="card-title">ریپازیتوری‌های کاربر</h3>
                    </div>
                    <p class="card-description">دریافت لیست ریپازیتوری‌های هر کاربر به همراه جزئیات کامل</p>
                    <div class="endpoint-url">GET /api/user/{username}/repos?limit=5</div>
                    <a href="/api/user/microsoft/repos?limit=3" class="example-link">مثال: ریپازیتوری‌های مایکروسافت</a>
                </div>
                
                <div class="endpoint-card method-get">
                    <div class="card-header">
                        <div class="card-icon">🔍</div>
                        <h3 class="card-title">جستجوی ریپازیتوری‌ها</h3>
                    </div>
                    <p class="card-description">جستجوی پیشرفته در بین میلیون‌ها ریپازیتوری GitHub</p>
                    <div class="endpoint-url">GET /api/search/repos?q=query&limit=10</div>
                    <a href="/api/search/repos?q=fastapi+python&limit=2" class="example-link">مثال: جستجوی FastAPI</a>
                </div>
                
                <div class="endpoint-card method-get">
                    <div class="card-header">
                        <div class="card-icon">📊</div>
                        <h3 class="card-title">محدودیت درخواست</h3>
                    </div>
                    <p class="card-description">بررسی میزان درخواست‌های باقی‌مانده به GitHub API</p>
                    <div class="endpoint-url">GET /api/rate_limit</div>
                    <a href="/api/rate_limit" class="example-link">مشاهده وضعیت فعلی</a>
                </div>
                
                <div class="endpoint-card method-get">
                    <div class="card-header">
                        <div class="card-icon">❤️</div>
                        <h3 class="card-title">بررسی سلامت</h3>
                    </div>
                    <p class="card-description">بررسی وضعیت کلی API و اتصال به سرور</p>
                    <div class="endpoint-url">GET /health</div>
                    <a href="/health" class="example-link">تست سلامت سرویس</a>
                </div>
            </div>
            
            <div class="footer">
                <a href="/docs" class="docs-link">
                    📚 مشاهده مستندات کامل API (Swagger UI)
                </a>
                <p style="margin-top: 20px; opacity: 0.8;">ساخته شده با FastAPI ❤️</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    """بررسی سلامت API"""
    return {
        "status": "healthy",
        "message": "API در حال اجراست!",
        "version": "2.0.0"
    }

@app.get("/api/user/{username}")
async def get_user_info(username: str):
    """دریافت اطلاعات پایه یک کاربر GitHub"""
    try:
        response = requests.get(
            f"https://api.github.com/users/{username}",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="کاربر در GitHub یافت نشد")
        elif response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, 
                detail=f"خطا از سمت GitHub: {response.text}"
            )
        
        user_data = response.json()
        
        return {
            "success": True,
            "username": user_data.get("login"),
            "name": user_data.get("name"),
            "bio": user_data.get("bio"),
            "public_repos": user_data.get("public_repos"),
            "followers": user_data.get("followers"),
            "following": user_data.get("following"),
            "avatar_url": user_data.get("avatar_url"),
            "profile_url": user_data.get("html_url"),
            "created_at": user_data.get("created_at"),
            "location": user_data.get("location"),
            "company": user_data.get("company")
        }
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="اتصال به GitHub timeout خورد")
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="عدم توانایی در اتصال به GitHub")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطای داخلی: {str(e)}")

@app.get("/api/user/{username}/repos")
async def get_user_repos(
    username: str,
    limit: Optional[int] = Query(5, ge=1, le=100, description="تعداد ریپازیتوری‌ها"),
    sort: Optional[str] = Query("updated", description="مرتب‌سازی بر اساس: created, updated, pushed, full_name")
):
    """دریافت ریپازیتوری‌های یک کاربر"""
    try:
        response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            params={"sort": sort, "per_page": limit},
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="کاربر یافت نشد")
        elif response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="خطا در ارتباط با GitHub")
        
        repos_data = response.json()
        
        repos = []
        for repo in repos_data:
            repos.append({
                "name": repo.get("name"),
                "full_name": repo.get("full_name"),
                "description": repo.get("description"),
                "url": repo.get("html_url"),
                "stars": repo.get("stargazers_count"),
                "forks": repo.get("forks_count"),
                "language": repo.get("language"),
                "updated_at": repo.get("updated_at"),
                "is_fork": repo.get("fork"),
                "size": repo.get("size")
            })
        
        return {
            "success": True,
            "username": username,
            "total_repos": len(repos_data),
            "repos": repos
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطای داخلی: {str(e)}")

@app.get("/api/search/repos")
async def search_repositories(
    q: str = Query(..., description="عبارت جستجو"),
    limit: Optional[int] = Query(10, ge=1, le=100, description="تعداد نتایج")
):
    """جستجوی ریپازیتوری‌ها در GitHub"""
    try:
        response = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": q, "per_page": limit},
            headers=headers,
            timeout=10
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="خطا در ارتباط با GitHub")
        
        search_data = response.json()
        
        results = []
        for item in search_data.get("items", []):
            results.append({
                "name": item.get("name"),
                "full_name": item.get("full_name"),
                "description": item.get("description"),
                "url": item.get("html_url"),
                "stars": item.get("stargazers_count"),
                "forks": item.get("forks_count"),
                "language": item.get("language"),
                "owner": item.get("owner", {}).get("login"),
                "updated_at": item.get("updated_at"),
                "license": item.get("license", {}).get("name") if item.get("license") else None
            })
        
        return {
            "success": True,
            "query": q,
            "total_count": search_data.get("total_count"),
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطای داخلی: {str(e)}")

@app.get("/api/rate_limit")
async def get_rate_limit():
    """بررسی میزان درخواست‌های باقی‌مانده"""
    try:
        response = requests.get("https://api.github.com/rate_limit", headers=headers, timeout=10)
        rate_data = response.json()
        
        return {
            "success": True,
            "rate_limit": rate_data.get("rate", {}),
            "resources": rate_data.get("resources", {})
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطای داخلی: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "github_api_fixed:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )