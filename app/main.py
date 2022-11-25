from fastapi import FastAPI
from app.endpoints.users_router import user_router
from app.endpoints.auth.router import router
from app.core.settings import settings


app = FastAPI(
    title='Ecommerce API',
    version='0.0.1'
)

app.include_router(user_router)
app.include_router(router)

