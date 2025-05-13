from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import entries, auth, users, summary, categories
from app.core.config import settings

app = FastAPI(title="Logly API", version="0.1.0")

# CORS 허용 (개발 단계 전체 오픈)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포 시 특정 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 연결
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(entries.router, prefix="/entries", tags=["Entries"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])

@app.get("/")
def root():
    return {"message": "Hello from Logly API 🚀"}
