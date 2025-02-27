from fastapi import APIRouter, HTTPException
from app.log_ingestion import store_log
from app.models import LogEntry
from app.database import SessionLocal

router = APIRouter()

@router.post("/logs/")
def create_log(log_data: dict):
    return store_log(log_data)

@router.get("/logs/")
def get_logs():
    db = SessionLocal()
    logs = db.query(LogEntry).all()
    db.close()
    return logs