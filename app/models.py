from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class LogEntry(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    log_level = Column(String, index=True)
    message = Column(String)
    source = Column(String, index=True)