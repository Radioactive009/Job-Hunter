from fastapi import FastAPI

app = FastAPI(
    title="AI Job Intelligence Platform",
    description="Personalized job discovery and recommendation system",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Job Intelligence Platform is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }