from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.nexus_ai_gateway.schemas import PredictionRequest, PredictionResponse


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


@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    print(f"Received prediction request: {request.model_name}")
    mock_result = "AI processing complete..."
    return PredictionResponse(
        status="success", result=mock_result, model_used=request.model_name
    )
