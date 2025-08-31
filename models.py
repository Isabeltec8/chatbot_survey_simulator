<<<<<<< HEAD
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
=======
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
>>>>>>> 53b17a6d039be7f9f9740d7321751bca552f8415
