# ==================================
# STAGE 1: The Builder (Heavy Lifting)
# ==================================
FROM python:3.12-slim as builder

# install system dependencies (if needed) and poetry
RUN pip install poetry==1.7.1

# Configure poetry to create venv inside the project
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Copy only the dependency files first (for caching)
COPY pyproject.toml poetry.lock ./

# Install dependencies (Main group only, no dev tools like pytest)
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# ==================================
# STAGE 2: The Runtime (Clean & Slim)
# ==================================
FROM python:3.12-slim as runtime

# Set environment variables for production
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv /app/.venv

# Copy the actual application code
COPY src ./src

# The command to run the server
# Note: We bind to 0.0.0.0 (All IPs) not 127.0.0.1 (Localhost)
# This is required for Docker to listen outside the container.
CMD ["uvicorn", "src.nexus_ai_gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]