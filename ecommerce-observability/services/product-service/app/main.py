from fastapi import FastAPI

app = FastAPI(title="Product-service")

@app.get("/")
def root():
    return {
        "service": "product-service",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

