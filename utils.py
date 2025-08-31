<<<<<<< HEAD
"""
Utilidades para la encuesta de chatbot
"""

import random
from datetime import datetime
from models import ChatbotSurveyResponse
from config import SatisfactionLevel, ResolutionType

def interactive_chatbot_survey() -> ChatbotSurveyResponse:
    """Interfaz interactiva para evaluación de chatbot"""
    print("=== ENCUESTA DE SATISFACCIÓN DEL CHATBOT ===\n")
    
    try:
        user_id = input("ID de usuario (opcional): ") or f"user_{random.randint(10000, 99999)}"
        
        print("\n¿Cómo calificaría su experiencia con el chatbot? (1-5):")
        print("1. Muy Insatisfecho")
        print("2. Insatisfecho")
        print("3. Neutral")
        print("4. Satisfecho")
        print("5. Muy Satisfecho")
        
        satisfaction = int(input("\nSatisfacción (1-5): "))
        while satisfaction not in range(1, 6):
            print("Por favor, ingrese un valor entre 1 y 5")
            satisfaction = int(input("Satisfacción (1-5): "))
        
        print("\nTipo de resolución:")
        print("1. Completa - El chatbot resolvió completamente mi problema")
        print("2. Parcial - El chatbot ayudó pero no resolvió completamente")
        print("3. No Resuelta - El chatbot no pudo resolver mi problema")
        print("4. Derivada - El chatbot me derivó a un agente humano")
        
        resolution = int(input("\nTipo de resolución (1-4): "))
        while resolution not in range(1, 5):
            print("Por favor, ingrese un valor entre 1 y 4")
            resolution = int(input("Tipo de resolución (1-4): "))
        
        accuracy = int(input("\nPrecisión de las respuestas (1-5): "))
        while accuracy not in range(1, 6):
            print("Por favor, ingrese un valor entre 1 y 5")
            accuracy = int(input("Precisión (1-5): "))
        
        problem_solved = input("\n¿El chatbot resolvió su problema? (s/n): ").lower().startswith('s')
        would_use_again = input("¿Usaría el chatbot nuevamente? (s/n): ").lower().startswith('s')
        
        duration = float(input("\nDuración de la conversación (minutos): ") or "3.0")
        comment = input("Comentarios sobre la experiencia: ")
        improvements = input("Sugerencias de mejora: ")
        
        response = ChatbotSurveyResponse(
            user_id=user_id,
            timestamp=datetime.now(),
            satisfaction=SatisfactionLevel(satisfaction),
            resolution_type=ResolutionType(resolution),
            response_accuracy=accuracy,
            would_use_again=would_use_again,
            problem_solved=problem_solved,
            conversation_duration=duration,
            user_comment=comment or None,
            suggested_improvements=improvements or None
        )
        
        print("\n¡Gracias por su feedback! Su opinión nos ayuda a mejorar el chatbot.")
        return response
        
    except ValueError as e:
        print(f"Error en la entrada: {e}")
        raise
    except Exception as e:
        print(f"Error inesperado: {e}")
=======
"""
Utilidades y funciones auxiliares
"""

import random
from datetime import datetime
from models import SurveyResponse
from config import SatisfactionLevel, ResponseTime

def interactive_survey() -> SurveyResponse:
    """Interfaz interactiva para añadir respuestas manualmente"""
    print("=== ENCUESTA DE SATISFACCIÓN DEL CHATBOT ===\n")
    
    try:
        user_id = input("ID de usuario (opcional): ") or f"user_{random.randint(10000, 99999)}"
        
        print("\nPor favor, califique su experiencia (1-5):")
        print("1. Muy Insatisfecho")
        print("2. Insatisfecho")
        print("3. Neutral")
        print("4. Satisfecho")
        print("5. Muy Satisfecho")
        
        satisfaction = int(input("\nSatisfacción (1-5): "))
        while satisfaction not in range(1, 6):
            print("Por favor, ingrese un valor entre 1 y 5")
            satisfaction = int(input("Satisfacción (1-5): "))
        
        print("\nTiempo de respuesta:")
        print("1. Inmediato")
        print("2. Rápido")
        print("3. Moderado")
        print("4. Lento")
        print("5. Muy Lento")
        
        response_time = int(input("\nTiempo de respuesta (1-5): "))
        while response_time not in range(1, 6):
            print("Por favor, ingrese un valor entre 1 y 5")
            response_time = int(input("Tiempo de respuesta (1-5): "))
        
        usefulness = int(input("\nUtilidad del chatbot (1-5): "))
        while usefulness not in range(1, 6):
            print("Por favor, ingrese un valor entre 1 y 5")
            usefulness = int(input("Utilidad (1-5): "))
        
        would_recommend = input("\n¿Recomendaría nuestro chatbot? (s/n): ").lower().startswith('s')
        comments = input("\nComentarios adicionales (opcional): ")
        
        session_duration = float(input("\nDuración de la sesión (minutos): ") or "5.0")
        
        response = SurveyResponse(
            user_id=user_id,
            timestamp=datetime.now(),
            satisfaction=SatisfactionLevel(satisfaction),
            response_time=ResponseTime(response_time),
            usefulness=usefulness,
            would_recommend=would_recommend,
            comments=comments or None,
            session_duration=session_duration
        )
        
        print("\n¡Gracias por completar la encuesta! Su feedback es muy valioso.")
        return response
        
    except ValueError as e:
        print(f"Error en la entrada: {e}")
        raise
    except Exception as e:
        print(f"Error inesperado: {e}")
>>>>>>> 53b17a6d039be7f9f9740d7321751bca552f8415
        raise