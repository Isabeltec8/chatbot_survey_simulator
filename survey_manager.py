"""
Gestión principal de las encuestas y operaciones CRUD
"""

import pandas as pd
from models import SurveyResponse
from analytics import SurveyAnalytics
from data_generator import DataGenerator
from visualizations import SurveyVisualizer
from config import CSV_FILENAME, logger

class SurveyManager:
    def __init__(self):
        self.responses: list[SurveyResponse] = []
        self.analytics = None
    
    def load_sample_data(self, num_samples: int = 1000) -> None:
        """Carga datos de muestra"""
        self.responses = DataGenerator.generate_sample_data(num_samples)
        self._update_analytics()
    
    def add_response(self, response: SurveyResponse) -> None:
        """Añade una nueva respuesta a la encuesta"""
        self.responses.append(response)
        self._update_analytics()
        logger.info(f"Nueva respuesta añadida: {response.user_id}")
    
    def _update_analytics(self) -> None:
        """Actualiza el análisis de datos"""
        self.analytics = SurveyAnalytics(self.responses)
    
    def get_report(self) -> dict:
        """Obtiene el reporte de análisis"""
        if self.analytics:
            return self.analytics.get_detailed_report()
        return {}
    
    def export_to_csv(self, filename: str = CSV_FILENAME) -> None:
        """Exporta los datos a un archivo CSV"""
        data = []
        for response in self.responses:
            data.append({
                'user_id': response.user_id,
                'timestamp': response.timestamp,
                'satisfaction': response.satisfaction.value,
                'response_time': response.response_time.value,
                'usefulness': response.usefulness,
                'would_recommend': response.would_recommend,
                'comments': response.comments,
                'session_duration': response.session_duration
            })
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        logger.info(f"Datos exportados a {filename}")
    
    def generate_visualizations(self) -> None:
        """Genera visualizaciones de los datos"""
        SurveyVisualizer.generate_visualizations(self.responses)