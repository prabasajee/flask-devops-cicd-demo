# DevOps CI/CD Demo

This project demonstrates a simple CI/CD pipeline for a Python Flask web application using Docker and GitHub Actions.

## Features
- Simple Flask web app
- Dockerfile for containerization
- GitHub Actions workflow for CI/CD (build, lint, Docker build)

## Getting Started

### Prerequisites
- Python 3.11+
- Docker (optional, for containerization)

### Run Locally
```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

### Build and Run with Docker
```bash
docker build -t flask-cicd-demo .
docker run -p 5000:5000 flask-cicd-demo
```

### CI/CD
On every push or pull request to the `main` branch, GitHub Actions will:
- Install dependencies
- Lint the code
- Build the Docker image

---

Feel free to fork and extend this project!
