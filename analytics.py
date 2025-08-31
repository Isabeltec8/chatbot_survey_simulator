"""
Análisis de métricas específicas para chatbot
"""

import statistics
from typing import Dict, List
from models import ChatbotSurveyResponse
from config import logger, SUCCESS_RATE_THRESHOLD

class ChatbotAnalytics:
    def __init__(self, responses: List[ChatbotSurveyResponse]):
        self.responses = responses
        self.metrics = self._calculate_chatbot_metrics()
    
    def _calculate_chatbot_metrics(self) -> Dict:
        """Calcula métricas específicas de chatbot"""
        if not self.responses:
            return {}
        
        satisfaction_scores = [r.satisfaction.value for r in self.responses]
        accuracy_scores = [r.response_accuracy for r in self.responses]
        resolution_types = [r.resolution_type.value for r in self.responses]
        would_use_again = [1 if r.would_use_again else 0 for r in self.responses]
        problem_solved = [1 if r.problem_solved else 0 for r in self.responses]
        
        # Métricas clave para chatbot
        success_rate = (sum(1 for r in self.responses 
                          if r.satisfaction.value >= SUCCESS_RATE_THRESHOLD and r.problem_solved) 
                       / len(self.responses)) * 100 if self.responses else 0
        
        deflection_rate = (sum(1 for r in self.responses 
                             if r.resolution_type.value == 1) 
                          / len(self.responses)) * 100 if self.responses else 0
        
        return {
            'total_interactions': len(self.responses),
            'success_rate': success_rate,
            'deflection_rate': deflection_rate,
            'average_satisfaction': statistics.mean(satisfaction_scores) if self.responses else 0,
            'average_accuracy': statistics.mean(accuracy_scores) if self.responses else 0,
            'reuse_intention': statistics.mean(would_use_again) * 100 if self.responses else 0,
            'problem_resolution_rate': statistics.mean(problem_solved) * 100 if self.responses else 0,
            'avg_conversation_duration': statistics.mean([r.conversation_duration for r in self.responses]) if self.responses else 0
        }
    
    def get_chatbot_report(self) -> Dict:
        """Genera reporte específico para chatbot"""
        return {
            'performance_metrics': self.metrics,
            'satisfaction_distribution': self._get_distribution('satisfaction'),
            'resolution_distribution': self._get_distribution('resolution'),
            'accuracy_distribution': self._get_distribution('accuracy'),
            'top_improvement_suggestions': self._get_improvement_suggestions()
        }
    
    def _get_distribution(self, metric: str) -> Dict:
        """Obtiene distribución de métricas"""
        if not self.responses:
            return {}
            
        if metric == 'satisfaction':
            values = [r.satisfaction.value for r in self.responses]
            max_val = 5
        elif metric == 'resolution':
            values = [r.resolution_type.value for r in self.responses]
            max_val = 4
        elif metric == 'accuracy':
            values = [r.response_accuracy for r in self.responses]
            max_val = 5
        else:
            return {}
        
        distribution = {}
        for i in range(1, max_val + 1):
            distribution[i] = values.count(i) / len(values) * 100
        
        return distribution
    
    def _get_improvement_suggestions(self, n: int = 8) -> List[Dict]:
        """Obtiene las sugerencias de mejora más comunes"""
        if not self.responses:
            return []
            
        suggestions = [r.suggested_improvements for r in self.responses if r.suggested_improvements]
        suggestion_counts = {}
        
        for suggestion in suggestions:
            suggestion_counts[suggestion] = suggestion_counts.get(suggestion, 0) + 1
        
        sorted_suggestions = sorted(suggestion_counts.items(), key=lambda x: x[1], reverse=True)
        return [{'suggestion': suggestion, 'count': count} for suggestion, count in sorted_suggestions[:n]]