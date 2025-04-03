# Intelligent Multimodal Health Navigator

## Overview
The **Intelligent Multimodal Health Navigator** is an AI-powered application designed to provide personalized healthcare insights and assistance. Using advanced machine learning models and API integrations, the navigator supports users by:
- Analyzing symptoms to provide preliminary recommendations.
- Scheduling medical appointments based on user preferences.
- Offering a user-friendly interface powered by Gradio.

## Features
- **Symptom Analysis**: Preliminary health guidance based on user-input symptoms.
- **Appointment Scheduling**: Seamless booking of medical appointments with date and specialty selection.
- **Gradio UI Integration**: Interactive web interface for easy accessibility.
- **Scalable Design**: Modular architecture for future enhancements and integrations.

## File Structure
```plaintext
├── data                # Directory for datasets or temporary files
├── notebooks           # Jupyter/Colab notebooks for experiments and demos
├── results             # Output files and analysis results
├── src                 # Source code and backend modules
│   ├── backend_functions.py # Functions for symptom analysis & scheduling
│   ├── dispatching.py        # Dispatcher for executing function calls
│   ├── json_tools.py   # Gradio interface for the application
├── README.md           # Documentation for your project
├── requirements.txt    # Project dependencies
├── Intelligent_Multimodal_Health_Navigator.ipynb # Demonstration notebook

## Setup Instructions
### Clone the Repository:
```bash
git clone https://github.com/tekleab15/Intelligent_Multimodal_Health_Navigator.git
cd Intelligent_Multimodal_Health_Navigator

##Test with Examples:
### Input queries like:
- "I have a fever and cough."
- "Book an appointment for General Medicine on 2025-03-04."

##License 
MIT Licence
