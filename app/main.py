from fastapi import FastAPI
from app.routes import log_routes, alert_routes
from app.database import engine, Base

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(log_routes.router)
app.include_router(alert_routes.router)

@app.get("/")
def read_root():
    return {"message": "AI Log Analyzer API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)