<<<<<<< HEAD
"""
Generador de datos de muestra para el chatbot
"""

import random
from datetime import datetime, timedelta
from models import ChatbotSurveyResponse
from config import SatisfactionLevel, ResolutionType, logger

class ChatbotDataGenerator:
    @staticmethod
    def generate_chatbot_data(num_samples: int = 500) -> list[ChatbotSurveyResponse]:
        """Genera datos de muestra para simulación de chatbot"""
        logger.info(f"Generando {num_samples} interacciones de chatbot...")
        
        responses = []
        for i in range(num_samples):
            user_id = f"user_{random.randint(10000, 99999)}"
            timestamp = datetime.now() - timedelta(days=random.randint(0, 30))
            
            # Simular métricas de chatbot
            satisfaction_val = min(5, max(1, int(random.gauss(3.8, 1.0))))
            accuracy_val = min(5, max(1, int(random.gauss(4.0, 0.8))))
            resolution_val = random.randint(1, 4)
            problem_solved = random.random() > 0.25  # 75% de problemas resueltos
            
            response = ChatbotSurveyResponse(
                user_id=user_id,
                timestamp=timestamp,
                satisfaction=SatisfactionLevel(satisfaction_val),
                resolution_type=ResolutionType(resolution_val),
                response_accuracy=accuracy_val,
                would_use_again=random.random() > 0.3,
                problem_solved=problem_solved,
                conversation_duration=random.uniform(0.5, 8.0),
                user_comment=ChatbotDataGenerator._generate_chatbot_comments(satisfaction_val, problem_solved),
                suggested_improvements=ChatbotDataGenerator._generate_improvements(satisfaction_val)
            )
            
            responses.append(response)
        
        logger.info("Datos de chatbot generados exitosamente")
        return responses
    
    @staticmethod
    def _generate_chatbot_comments(satisfaction: int, problem_solved: bool) -> str:
        """Genera comentarios relevantes para chatbot"""
        
        positive_comments = [
            "El chatbot resolvió mi problema instantáneamente",
            "Respuestas precisas y muy útiles",
            "Excelente experiencia de usuario",
            "Mucho mejor que esperar a un agente humano",
            "Muy intuitivo y fácil de usar"
        ]
        
        neutral_comments = [
            "Funciona bien para consultas básicas",
            "A veces da respuestas genéricas",
            "Útil pero limitado en temas complejos",
            "Buen primer nivel de soporte",
            "Regular, necesita más capacitación"
        ]
        
        negative_comments = [
            "No entendió mi pregunta varias veces",
            "Respuestas irrelevantes a mi consulta",
            "Tuve que contactar a un agente humano",
            "Muy confuso, no resolvió mi problema",
            "Frustrante experiencia de usuario"
        ]
        
        if not problem_solved:
            return random.choice([
                "No pudo resolver mi problema",
                "Tuve que escalar a soporte humano",
                "La solución no fue adecuada",
                "Quedé con la misma duda"
            ])
        
        if satisfaction >= 4:
            return random.choice(positive_comments)
        elif satisfaction == 3:
            return random.choice(neutral_comments)
        else:
            return random.choice(negative_comments)
    
    @staticmethod
    def _generate_improvements(satisfaction: int) -> str:
        """Genera sugerencias de mejora"""
        if satisfaction >= 4:
            return random.choice([
                "Más integraciones con otros sistemas",
                "Expandir funcionalidades",
                "Mayor personalización",
                "Ninguna, está perfecto"
            ])
        else:
            return random.choice([
                "Mejorar comprensión de lenguaje natural",
                "Más opciones de escalamiento",
                "Respuestas más específicas",
                "Menos respuestas genéricas",
                "Mejor flujo de conversación"
            ])
=======
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
>>>>>>> 53b17a6d039be7f9f9740d7321751bca552f8415
