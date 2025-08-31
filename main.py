"""
Punto de entrada principal del Simulador de Encuestas de Satisfacción de Chatbot
"""

from survey_manager import SurveyManager
from utils import interactive_survey
from config import SAMPLE_SIZE, logger

def main():
    """Función principal del simulador"""
    manager = SurveyManager()
    
    # Generar datos de muestra
    manager.load_sample_data(SAMPLE_SIZE)
    
    while True:
        print("\n=== SIMULADOR DE ENCUESTAS DE SATISFACCIÓN ===")
        print("1. Añadir respuesta manual")
        print("2. Ver reporte actual")
        print("3. Generar visualizaciones")
        print("4. Exportar a CSV")
        print("5. Salir")
        
        choice = input("\nSeleccione una opción: ")
        
        if choice == '1':
            try:
                response = interactive_survey()
                manager.add_response(response)
            except Exception:
                print("Error al procesar la encuesta. Intente nuevamente.")
        elif choice == '2':
            report = manager.get_report()
            print("\n=== REPORTE DE SATISFACCIÓN ===")
            print(f"Total respuestas: {report.get('summary_metrics', {}).get('total_responses', 0)}")
            print(f"Satisfacción promedio: {report.get('summary_metrics', {}).get('average_satisfaction', 0):.2f}")
            print(f"NPS Score: {report.get('summary_metrics', {}).get('nps_score', 0):.1f}")
            print(f"Tasa de recomendación: {report.get('summary_metrics', {}).get('recommendation_rate', 0):.1f}%")
        elif choice == '3':
            manager.generate_visualizations()
            print("Visualizaciones generadas exitosamente")
        elif choice == '4':
            filename = input("Nombre del archivo CSV: ") or "chatbot_survey_data.csv"
            manager.export_to_csv(filename)
        elif choice == '5':
            print("¡Gracias por usar el simulador!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()