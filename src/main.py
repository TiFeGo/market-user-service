from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.endpoints.users_router import user_router
from src.endpoints.auth.router import router
from src.core.settings import settings
from src.core import tracing_tools
from prometheus_fastapi_instrumentator import Instrumentator



app = FastAPI(
    title='Ecommerce API',
    version='0.0.1'
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    tracing_tools.init_tracer()
    Instrumentator().instrument(app).expose(app)

app.include_router(user_router)
app.include_router(router)

