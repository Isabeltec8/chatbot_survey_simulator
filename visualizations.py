"""
Visualizaciones específicas para métricas de chatbot
"""

import matplotlib.pyplot as plt
import seaborn as sns
from models import ChatbotSurveyResponse
from typing import List
from config import VISUALIZATION_FILENAME, logger

class ChatbotVisualizer:
    @staticmethod
    def generate_chatbot_visualizations(responses: List[ChatbotSurveyResponse]) -> None:
        """Genera visualizaciones específicas para chatbot"""
        if not responses:
            logger.warning("No hay datos para visualizar")
            return
        
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Distribución de satisfacción
        sat_values = [r.satisfaction.value for r in responses]
        axes[0, 0].hist(sat_values, bins=5, alpha=0.7, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Distribución de Satisfacción del Chatbot')
        axes[0, 0].set_xlabel('Nivel de Satisfacción')
        axes[0, 0].set_ylabel('Frecuencia')
        
        # Tasa de resolución de problemas
        resolved = [1 if r.problem_solved else 0 for r in responses]
        resolved_rate = sum(resolved) / len(resolved) * 100
        labels = ['Resueltos', 'No Resueltos']
        sizes = [resolved_rate, 100 - resolved_rate]
        axes[0, 1].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
        axes[0, 1].set_title('Tasa de Resolución de Problemas')
        
        # Relación entre precisión y satisfacción
        accuracy = [r.response_accuracy for r in responses]
        axes[1, 0].scatter(accuracy, sat_values, alpha=0.6, color='orange')
        axes[1, 0].set_title('Precisión vs Satisfacción')
        axes[1, 0].set_xlabel('Precisión de Respuesta')
        axes[1, 0].set_ylabel('Satisfacción')
        
        # Distribución de tipos de resolución
        resolution_types = [r.resolution_type.value for r in responses]
        resolution_labels = ['Completa', 'Parcial', 'No Resuelta', 'Derivada']
        resolution_counts = [resolution_types.count(i) for i in range(1, 5)]
        axes[1, 1].bar(resolution_labels, resolution_counts, color='lightblue', alpha=0.7)
        axes[1, 1].set_title('Distribución de Tipos de Resolución')
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(VISUALIZATION_FILENAME, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Visualizaciones de chatbot guardadas en '{VISUALIZATION_FILENAME}'")