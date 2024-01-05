from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from mangum import Mangum


ALLOWED_ORIGINS = [
    "*",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("startup fastapi")
    yield
    # shutdown
    print("Shutdown fastapi")


description = """Fastapi do awesome stuff. 🚀"""

app = FastAPI(
    title="Fastapi serverless",
    description=description,
    summary="This sample API is a RESTful set of HTTP endpoints",
    version="0.0.1",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello_world():
    return {'message': 'Hello from Fastapi Serverless API'}

handler = Mangum(app)
