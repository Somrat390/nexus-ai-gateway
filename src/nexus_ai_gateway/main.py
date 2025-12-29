from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print("Starting up the Nexus AI Gateway...")
    yield
    # Shutdown actions
    print("Shutting down the Nexus AI Gateway...")


app = FastAPI(
    title="Nexus AI Gateway",
    description="API Gateway for Nexus AI services",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0", "mode": "production"}
