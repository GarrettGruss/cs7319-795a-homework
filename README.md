# CS 7319 Homework 4 - Kubernetes Deployment

A REST API that serves inspirational quotes, containerized with Docker and deployed on Kubernetes using Minikube.

## Assignment Overview

This project implements a FastAPI REST API with Pydantic models that serves inspirational quotes randomly selected from a local pool. The application is containerized and deployed on Minikube with 4 replicas.

**Instructor:** Dr. Isaac Chow  
**Due Date:** September 21, 2025

## Functional Requirements

### API Endpoints
- **GET /api/quotes** - Returns a JSON array of exactly 4 quotes chosen randomly from a pool of 51+ quotes
- **GET /** - Homepage with a minimal static page that displays quotes fetched from `/api/quotes`

### Quote Schema
Each quote object includes:
- `quote` - The inspirational quotation text
- `author` - Attribution to the quote's author

### Configuration
- Application listens on port **8080** (aligned with container/Kubernetes settings)

## Data

The project includes a comprehensive quotes dataset (`data/quotes.json`) with 51 humorous "inspirational" quotes from various fictional authors, providing a diverse pool for random selection.

## Architecture

### Backend Technology
- **FastAPI** - Modern, fast web framework for building APIs with Python
- **Pydantic** - Data validation and settings management using Python type annotations
- **Uvicorn** - ASGI server for running the FastAPI application

### Frontend Technology
- **Streamlit** - Interactive web application framework for data apps
- **Requests** - HTTP library for API communication

### Containerization
- Dockerized service that runs locally
- Container configured to expose port 8080
- Python-based container with FastAPI dependencies

### Kubernetes Deployment
- Deployed on Minikube
- **4 replicas** using Kubernetes Deployment
- Service exposure via NodePort (suitable for Minikube)
- Kubernetes manifests for deployment and service configuration

## Project Structure

```
.
├── data/
│   └── quotes.json          # Pool of inspirational quotes
├── src/
│   ├── backend/             # FastAPI application
│   │   ├── model/           # Pydantic models
│   │   ├── service/         # Business logic
│   │   ├── controller/      # API routes
│   │   └── main.py         # FastAPI entry point
│   └── frontend/            # Streamlit application
│       ├── app.py          # Streamlit UI
│       └── api_client.py   # API client
├── tests/                   # Unit tests
├── Dockerfile               # Docker containerization
├── k8s.yaml                # Kubernetes manifests
└── README.md               # This file
```

## Getting Started

### Prerequisites
- Python 3.8+ for local development
- Docker installed locally
- Minikube installed and running
- kubectl configured to work with Minikube

### Local Development

#### Full Stack Development
1. **Terminal 1** - Start backend: `PYTHONPATH=src uvicorn backend.main:app --host 0.0.0.0 --port 8080 --reload`
2. **Terminal 2** - Start frontend: `src/frontend/streamlit run app.py`
3. Access frontend at `http://localhost:8501` (connects to backend automatically)

#### Testing
- Run unit tests: `python -m pytest tests/`
- Test API directly: `curl http://localhost:8080/api/quotes`

### Kubernetes Deployment
1. Apply Kubernetes manifests: `kubectl apply -f k8s.yaml`
2. Verify deployment: `kubectl get deployments`
3. Check service: `kubectl get services`
4. Access the application through Minikube service

### Verification
- Confirm 4 replicas are running
- Test endpoint access on Minikube
- Validate random quote selection from the pool

## Deliverables

1. ✅ Source Code and Dockerfile
2. ✅ Kubernetes manifests (k8s.yaml)
3. 📸 Screenshots showing successful runs
4. 📋 Verification of endpoint access on Minikube

## Sample Quote Response

```json
[
  {
    "quote": "Dream follow you, but nightmare is faster runner.",
    "author": "Marcus Wellington"
  },
  {
    "quote": "Success is 1% inspiration, 99% doing math wrong about percentage.",
    "author": "Dr. Robert Chen"
  },
  {
    "quote": "Rome wasn't build in day, was actually several day, maybe week even.",
    "author": "Antonio Ricci"
  },
  {
    "quote": "When door close, window open, but sometimes is just drafty house.",
    "author": "Vladimir Petrov"
  }
]
```

## Notes

The quotes dataset contains intentionally humorous takes on classic inspirational sayings, providing both entertainment value and technical functionality for the API demonstration.