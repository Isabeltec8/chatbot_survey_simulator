"""
Modelos de datos para la encuesta de satisfacción del chatbot
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from config import SatisfactionLevel, ResolutionType

@dataclass
class ChatbotSurveyResponse:
    user_id: str
    timestamp: datetime
    satisfaction: SatisfactionLevel
    resolution_type: ResolutionType
    response_accuracy: int  # 1-5 scale
    would_use_again: bool
    problem_solved: bool
    conversation_duration: float  # in minutes
    user_comment: Optional[str] = None
    suggested_improvements: Optional[str] = None