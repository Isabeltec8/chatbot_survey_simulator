"""
Generación de visualizaciones para los datos de encuestas
"""

import matplotlib.pyplot as plt
import seaborn as sns
from models import SurveyResponse
from typing import List
from config import VISUALIZATION_FILENAME, logger

class SurveyVisualizer:
    @staticmethod
    def generate_visualizations(responses: List[SurveyResponse]) -> None:
        """Genera visualizaciones de los datos"""
        if not responses:
            logger.warning("No hay datos para visualizar")
            return
        
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Distribución de satisfacción
        sat_values = [r.satisfaction.value for r in responses]
        axes[0, 0].hist(sat_values, bins=5, alpha=0.7, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Distribución de Satisfacción')
        axes[0, 0].set_xlabel('Nivel de Satisfacción')
        axes[0, 0].set_ylabel('Frecuencia')
        
        # Distribución de tiempo de respuesta
        time_values = [r.response_time.value for r in responses]
        axes[0, 1].hist(time_values, bins=5, alpha=0.7, color='lightgreen', edgecolor='black')
        axes[0, 1].set_title('Distribución de Tiempo de Respuesta')
        axes[0, 1].set_xlabel('Tiempo de Respuesta')
        axes[0, 1].set_ylabel('Frecuencia')
        
        # Relación entre satisfacción y utilidad
        usefulness = [r.usefulness for r in responses]
        axes[1, 0].scatter(sat_values, usefulness, alpha=0.6, color='orange')
        axes[1, 0].set_title('Satisfacción vs Utilidad')
        axes[1, 0].set_xlabel('Satisfacción')
        axes[1, 0].set_ylabel('Utilidad')
        
        # Tasa de recomendación
        recommend = [1 if r.would_recommend else 0 for r in responses]
        recommend_rate = sum(recommend) / len(recommend) * 100
        labels = ['Recomendaría', 'No recomendaría']
        sizes = [recommend_rate, 100 - recommend_rate]
        axes[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightcoral', 'lightblue'])
        axes[1, 1].set_title('Tasa de Recomendación')
        
        plt.tight_layout()
        plt.savefig(VISUALIZATION_FILENAME, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Visualizaciones generadas y guardadas en '{VISUALIZATION_FILENAME}'")