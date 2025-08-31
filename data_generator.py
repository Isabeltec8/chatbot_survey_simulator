"""
Generación de datos de muestra para la simulación
"""

import random
from datetime import datetime, timedelta
from models import SurveyResponse
from config import SatisfactionLevel, ResponseTime, logger

class DataGenerator:
    @staticmethod
    def generate_sample_data(num_samples: int = 1000) -> list[SurveyResponse]:
        """Genera datos de muestra para simulación"""
        logger.info(f"Generando {num_samples} respuestas de muestra...")
        
        responses = []
        for i in range(num_samples):
            user_id = f"user_{random.randint(10000, 99999)}"
            timestamp = datetime.now() - timedelta(days=random.randint(0, 30))
            
            # Simular distribución normal con tendencia positiva
            satisfaction_val = min(5, max(1, int(random.gauss(3.8, 1.2))))
            response_time_val = min(5, max(1, int(random.gauss(2.5, 1.0))))
            usefulness_val = min(5, max(1, int(random.gauss(4.0, 0.8))))
            
            response = SurveyResponse(
                user_id=user_id,
                timestamp=timestamp,
                satisfaction=SatisfactionLevel(satisfaction_val),
                response_time=ResponseTime(response_time_val),
                usefulness=usefulness_val,
                would_recommend=random.random() > 0.3,  # 70% probability
                comments=DataGenerator._generate_random_comments(satisfaction_val),
                session_duration=random.uniform(1.0, 15.0)
            )
            
            responses.append(response)
        
        logger.info("Datos de muestra generados exitosamente")
        return responses
    
    @staticmethod
    def _generate_random_comments(satisfaction: int) -> str:
        """Genera comentarios aleatorios basados en el nivel de satisfacción"""
        positive_comments = [
            "Excelente servicio, muy útil",
            "Resolvió mi problema rápidamente",
            "Muy intuitivo y fácil de usar",
            "Respuestas precisas y relevantes",
            "Me encantó la experiencia"
        ]
        
        neutral_comments = [
            "Funciona bien, pero podría mejorar",
            "Aceptable para necesidades básicas",
            "No está mal, pero hay alternativas mejores",
            "Cumple su función principal",
            "Regular, esperaba más funcionalidades"
        ]
        
        negative_comments = [
            "No entendió mis preguntas",
            "Muy lento en responder",
            "Respuestas poco útiles",
            "Interfaz confusa",
            "No resolvió mi problema"
        ]
        
        if satisfaction >= 4:
            return random.choice(positive_comments)
        elif satisfaction == 3:
            return random.choice(neutral_comments)
        else:
            return random.choice(negative_comments)