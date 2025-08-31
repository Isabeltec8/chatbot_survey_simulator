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
        raise