from app.database import SessionLocal
from app.models import LogEntry

def store_log(log_data):
    db = SessionLocal()
    new_log = LogEntry(**log_data)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    db.close()
    return new_log