from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import users, events, recommendations, auth

app = FastAPI(
    title="Eventus API",
    description="API для рекомендательной системы мероприятий «Ивентус»",
    version="1.0.0"
)

# CORS — разрешаем все источники для фронтенд-команды
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/api/auth", tags=["Авторизация"])
app.include_router(users.router, prefix="/api/users", tags=["Пользователи"])
app.include_router(events.router, prefix="/api/events", tags=["Мероприятия"])
app.include_router(recommendations.router, prefix="/api/recommendations", tags=["Рекомендации"])

@app.get("/")
def root():
    return {
        "message": "Eventus API работает",
        "status": "ok",
        "docs": "/docs",
        "openapi": "/openapi.json"
    }

@app.get("/health")
def health():
    return {"status": "ok"}