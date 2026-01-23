import json

from fastapi import FastAPI 

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return{'message': 'Hello, World!'}

@app.get("/about")
def about():
    return{'message': 'This is a patient data API.'}    

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'Patient not found'}