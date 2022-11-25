from fastapi import FastAPI
from src.endpoints.users_router import user_router
from src.endpoints.auth.router import router
from src.core.settings import settings


app = FastAPI(
    title='Ecommerce API',
    version='0.0.1'
)

app.include_router(user_router)
app.include_router(router)

