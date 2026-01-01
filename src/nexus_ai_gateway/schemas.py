from pydantic import BaseModel, Field, validator


class PredictionRequest(BaseModel):
    input_text: str = Field(
        ...,
        min_length=5,
        max_length=1000,
        description="This text to be processed by the AI model.",
        example="What is the capital of France?",
    )
    model_name: str = Field("gpt-4-turbo", description="The specific AI model to use")

    @validator("model_name")
    def validate_model_name(cls, v):
        allowed_models = {"gpt-4-turbo", "claude-3-opus", "bert-base"}
        if v not in allowed_models:
            raise ValueError(f"model_name must be one of {allowed_models}")
        return v


class PredictionResponse(BaseModel):
    status: str
    result: str
    model_used: str
