from pydantic import BaseModel, Field

# 1️⃣ Pydantic Model তৈরি
class Patient(BaseModel):
    name: str
    age: int = Field(gt=0, le=120)  # age must be > 0 and <= 120
    email: str | None = None        # optional field


# 2️⃣ Raw input data (dictionary)
patient_data = {
    "name": "Rahim",
    "age": "24",      # string হলেও Pydantic এটাকে int এ convert করবে
    "email": "rahim@gmail.com"
}

# 3️⃣ Model instantiate (automatic validation happens here)
patient = Patient(**patient_data)

# 4️⃣ Validated object ব্যবহার
def insert_patient_data(patient: Patient):
    print("Patient Name:", patient.name)
    print("Patient Age:", patient.age)
    print("Patient Email:", patient.email)


insert_patient_data(patient)
