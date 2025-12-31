# 🚀 Nexus AI Gateway

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688?style=for-the-badge&logo=fastapi)
![Poetry](https://img.shields.io/badge/Poetry-Dependencies-blueviolet?style=for-the-badge&logo=poetry)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)

**Nexus** is a high-performance, asynchronous AI Inference Gateway designed to handle high-concurrency model serving. It acts as the orchestration layer between end-users and heavy GPU compute resources.

> **Status:** Active Development 🚧

## 🏗 Architecture & Tech Stack

This project mirrors a **Production-Grade AI Infrastructure** used at scale.

* **Core Framework:** `FastAPI` (Asynchronous I/O for high throughput).
* **Dependency Management:** `Poetry` (Deterministic builds, no `pip` drift).
* **Code Quality:** `Ruff` (Strict linting) + `Pre-commit Hooks` (Automated guardrails).
* **Server:** `Uvicorn` (ASGI implementation).
* **Lifespan Management:** Efficient resource loading (ML models loaded once on startup).

## ⚡ Engineering Decisions (The "Why")

### 1. Why Poetry over Pip?
Standard `requirements.txt` files often lead to "Dependency Drift" where development and production environments silently diverge. Nexus uses **Poetry** to enforce a strict lockfile (`poetry.lock`), ensuring bit-for-bit reproducibility across all environments.

### 2. Why Async FastAPI?
AI Inference is I/O bound (waiting for GPU). A synchronous framework (Django/Flask) would block the entire server while waiting for a prediction. **FastAPI's async event loop** allows Nexus to handle thousands of concurrent requests while waiting for the GPU worker to respond.

### 3. Automated Guardrails
We enforce code quality *before* the commit happens. The `.pre-commit-config.yaml` configuration ensures that no unformatted code ever enters the repository, reducing technical debt and code review friction.

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.10+
* Poetry (`curl -sSL https://install.python-poetry.org | python3 -`)

### Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/Somrat390/nexus-ai-gateway
cd nexus-ai-gateway

# 2. Install dependencies (Deterministic)
poetry install

# 3. Activate the Robot Guard
poetry run pre-commit install

# 4. Run the Server
poetry run uvicorn src.nexus_ai_gateway.main:app --reload
```

## 📖 API Documentation

Once the server is running, access the auto-generated Swagger UI:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Core Endpoints
* `GET /health`: Health check for Kubernetes/Load Balancers.

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (**Pre-commit will verify your code**).
4. Push to the branch.
5. Open a Pull Request.