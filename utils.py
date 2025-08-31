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
        raise