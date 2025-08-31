"""
Configuración y constantes del simulador de encuestas
"""

from enum import Enum
import logging

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('chatbot_survey.log'),
        logging.StreamHandler()
    ]
)

# Crear el logger
logger = logging.getLogger(__name__)

class SatisfactionLevel(Enum):
    MUY_INSATISFECHO = 1
    INSATISFECHO = 2
    NEUTRO = 3
    SATISFECHO = 4
    MUY_SATISFECHO = 5

class ResponseTime(Enum):
    INMEDIATO = 1
    RÁPIDO = 2
    MODERADO = 3
    LENTO = 4
    MUY_LENTO = 5

# Configuración de la aplicación
SAMPLE_SIZE = 1000
CSV_FILENAME = "chatbot_survey_data.csv"
VISUALIZATION_FILENAME = "chatbot_survey_analysis.png"