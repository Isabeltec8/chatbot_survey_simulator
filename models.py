"""
Definiciones de clases y estructuras de datos
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from config import SatisfactionLevel, ResponseTime

@dataclass
class SurveyResponse:
    user_id: str
    timestamp: datetime
    satisfaction: SatisfactionLevel
    response_time: ResponseTime
    usefulness: int  # 1-5 scale
    would_recommend: bool
    comments: Optional[str] = None
    session_duration: Optional[float] = None  # in minutes