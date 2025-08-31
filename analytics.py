<<<<<<< HEAD
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
=======
"""
Análisis y cálculo de métricas de las encuestas
"""

import statistics
from typing import Dict, List
from models import SurveyResponse
from config import logger

class SurveyAnalytics:
    def __init__(self, responses: List[SurveyResponse]):
        self.responses = responses
        self.metrics = self._calculate_metrics()
    
    def _calculate_metrics(self) -> Dict:
        """Calcula métricas clave de satisfacción"""
        if not self.responses:
            return {}
        
        satisfaction_scores = [r.satisfaction.value for r in self.responses]
        response_times = [r.response_time.value for r in self.responses]
        usefulness_scores = [r.usefulness for r in self.responses]
        recommendations = [1 if r.would_recommend else 0 for r in self.responses]
        
        # Calcular NPS (Net Promoter Score)
        promoters = sum(1 for r in self.responses if r.satisfaction.value >= 4)
        detractors = sum(1 for r in self.responses if r.satisfaction.value <= 2)
        nps = ((promoters - detractors) / len(self.responses)) * 100 if self.responses else 0
        
        return {
            'total_responses': len(self.responses),
            'average_satisfaction': statistics.mean(satisfaction_scores) if self.responses else 0,
            'nps_score': nps,
            'response_time_avg': statistics.mean(response_times) if self.responses else 0,
            'usefulness_avg': statistics.mean(usefulness_scores) if self.responses else 0,
            'recommendation_rate': statistics.mean(recommendations) * 100 if self.responses else 0
        }
    
    def get_detailed_report(self) -> Dict:
        """Genera un reporte detallado de las métricas"""
        return {
            'summary_metrics': self.metrics,
            'satisfaction_distribution': self._get_distribution('satisfaction'),
            'response_time_distribution': self._get_distribution('response_time'),
            'usefulness_distribution': self._get_distribution('usefulness'),
            'top_comments': self._get_top_comments(),
            'trend_analysis': self._analyze_trends()
        }
    
    def _get_distribution(self, metric: str) -> Dict:
        """Obtiene la distribución de una métrica específica"""
        if not self.responses:
            return {}
            
        if metric == 'satisfaction':
            values = [r.satisfaction.value for r in self.responses]
        elif metric == 'response_time':
            values = [r.response_time.value for r in self.responses]
        elif metric == 'usefulness':
            values = [r.usefulness for r in self.responses]
        else:
            return {}
        
        distribution = {}
        for i in range(1, 6):
            distribution[i] = values.count(i) / len(values) * 100
        
        return distribution
    
    def _get_top_comments(self, n: int = 10) -> List[Dict]:
        """Obtiene los comentarios más comunes"""
        if not self.responses:
            return []
            
        comments = [r.comments for r in self.responses if r.comments]
        comment_counts = {}
        
        for comment in comments:
            comment_counts[comment] = comment_counts.get(comment, 0) + 1
        
        sorted_comments = sorted(comment_counts.items(), key=lambda x: x[1], reverse=True)
        return [{'comment': comment, 'count': count} for comment, count in sorted_comments[:n]]
    
    def _analyze_trends(self) -> Dict:
        """Analiza tendencias temporales"""
        if len(self.responses) < 10:
            return {}
        
        # Agrupar por semana
        weekly_data = {}
        for response in self.responses:
            week = response.timestamp.isocalendar()[1]
            year = response.timestamp.year
            key = f"{year}-W{week}"
            
            if key not in weekly_data:
                weekly_data[key] = []
            
            weekly_data[key].append(response.satisfaction.value)
        
        trends = {}
        for week, scores in weekly_data.items():
            trends[week] = statistics.mean(scores)
        
        return trends
>>>>>>> 53b17a6d039be7f9f9740d7321751bca552f8415
