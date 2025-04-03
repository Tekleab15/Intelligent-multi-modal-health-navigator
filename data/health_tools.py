analyze_symptoms_function = {
    "name": "analyze_symptoms",
    "description": "Analyzes reported symptoms and gives a preliminary recommendation regarding consultation.",
    "parameters": {
        "type": "object",
        "properties": {
            "symptoms": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of symptoms (e.g., ['fever', 'cough'])."
            }
        },
        "required": ["symptoms"]
    }
}

# 3. Initiate Video Consultation (Doxy.me)
initiate_video_consultation_doxy_function = {
    "name": "initiate_video_consultation_doxy",
    "description": "Initiates a video consultation using the Doxy.me telemedicine platform.",
    "parameters": {
        "type": "object",
        "properties": {
            "patient_name": {
                "type": "string",
                "description": "Name of the patient."
            },
            "preferred_time": {
                "type": "string",
                "description": "Preferred consultation time in ISO format (e.g., 2025-03-04T14:00:00)."
            }
        },
        "required": ["patient_name", "preferred_time"]
    }
}


# 2. Schedule Appointment
schedule_appointment_function = {
    "name": "schedule_appointment",
    "description": "Schedules an appointment given a date and a medical specialty.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Appointment date in yyyy-mm-dd format."
            },
            "specialty": {
                "type": "string",
                "description": "Medical specialty (e.g., 'General Medicine')."
            }
        },
        "required": ["date", "specialty"]
    }
}

# 4. Initiate Chat/Video Session (QuickBlox)
initiate_chat_video_quickblox_function = {
    "name": "initiate_chat_video_quickblox",
    "description": "Initiates a secure chat or video session using QuickBlox.",
    "parameters": {
        "type": "object",
        "properties": {
            "patient_id": {
                "type": "string",
                "description": "Unique identifier for the patient."
            },
            "session_type": {
                "type": "string",
                "description": "Type of session to initiate (e.g., 'video' or 'chat')."
            }
        },
        "required": ["patient_id", "session_type"]
    }
}

# 5. Retrieve Patient Data (FHIR)
get_patient_data_fhir_function = {
    "name": "get_patient_data_fhir",
    "description": "Retrieves patient data using the FHIR standard.",
    "parameters": {
        "type": "object",
        "properties": {
            "patient_id": {
                "type": "string",
                "description": "Unique identifier for the patient."
            }
        },
        "required": ["patient_id"]
    }
}

# 6. Initiate Vonage Consultation
initiate_vonage_consultation_function = {
    "name": "initiate_vonage_consultation",
    "description": "Initiates a consultation session using Vonage's API. Determines if the session is voice, video, or messaging.",
    "parameters": {
        "type": "object",
        "properties": {
            "patient_id": {
                "type": "string",
                "description": "Unique identifier for the patient."
            },
            "channel": {
                "type": "string",
                "description": "Communication channel: 'voice', 'video', or 'message'."
            }
        },
        "required": ["patient_id", "channel"]
    }
}
