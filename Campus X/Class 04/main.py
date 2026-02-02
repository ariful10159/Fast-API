import json

from fastapi import FastAPI, HTTPException, Query 

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


@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or BMI"),
          order: str = Query("asc", description="Sort order: asc or desc")):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid sort_by field. Must be one of {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order. Must be "asc" or "desc"')
    
    data = load_data()

    sort_order  = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)

    return
    
