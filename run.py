import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "github_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # برای توسعه - تغییرات به صورت خودکار اعمال شود
        workers=1
    )