# File: backend_functions.py
import requests
def analyze_symptoms(symptoms):
    """
    Analyzes the reported symptoms and provides a preliminary recommendation.
    """
    if "fever" in symptoms and "cough" in symptoms:
        return "Your symptoms suggest a possible respiratory infection. Please consult a doctor."
    elif "headache" in symptoms and "nausea" in symptoms:
        return "These symptoms may indicate a migraine. Rest in a quiet room and monitor your condition."
    else:
        return "Your symptoms appear mild. If they persist or worsen, consider consulting a healthcare professional."

def schedule_appointment(date, specialty):
    """
    Schedules a medical appointment.
    """
    return f"Your appointment for {specialty} has been scheduled on {date}. A confirmation email has been sent."

# Mapping of function names to their implementations.
function_map = {
    "analyze_symptoms": analyze_symptoms,
    "schedule_appointment": schedule_appointment,
}

