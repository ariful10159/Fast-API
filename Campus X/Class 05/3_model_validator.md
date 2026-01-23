

```python
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict
```

* **BaseModel** → ডাটা structure এবং validation এর জন্য
* **EmailStr** → ইমেইল সঠিক কিনা চেক করে
* **model_validator** → পুরো model-এর উপর custom validation করার জন্য
* **List, Dict** → টাইপ annotation এর জন্য

---

```python
class Patient(BaseModel):
```

* এটা Pydantic এর মডেল, যা রোগীর ডাটা define করে

---

### Fields / Attributes

```python
name: str
email: EmailStr
age: int
weight: float
married: bool
allergies: List[str]
contact_details: Dict[str, str]
```

* **name** → রোগীর নাম (string)
* **email** → রোগীর ইমেইল (valid format)
* **age** → বয়স (integer)
* **weight** → ওজন (float)
* **married** → বিবাহিত কিনা (True/False)
* **allergies** → এলার্জির তালিকা (string এর list)
* **contact_details** → ফোন, ঠিকানা ইত্যাদি key-value আকারে

---

### Model Validator

```python
@model_validator(mode='after')
def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('Patients older than 60 must have an emergency contact')
    return model
```

* **mode='after'** → সব field validate হওয়ার পরে এই function চালানো হবে
* কোড চেক করে:

  * যদি রোগীর বয়স **60 এর বেশি**
  * এবং contact_details এ **emergency contact না থাকে**
    → তাহলে error দেখাবে
* যদি সব ঠিক থাকে → model return করবে

**মানে:** ৬০ বছরের বেশি রোগীদের জন্য emergency contact বাধ্যতামূলক

---

### Update function

```python
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
```

* Patient object থেকে ডাটা print করে

---

### Patient data

```python
patient_info = {
    'name':'nitish',
    'email':'abc@icici.com',
    'age': '65',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details':{'phone':'2353462', 'emergency':'235236'}
}
```

* রোগীর তথ্য dictionary আকারে
* age string `'65'` হলেও Pydantic automatically int এ convert করবে

---

### Object creation এবং function call

```python
patient1 = Patient(**patient_info) 
update_patient_data(patient1)
```

* Patient object তৈরি হলো
* emergency contact validation হলো
* সব ঠিক থাকলে function call করে ডাটা print হবে

---

### Output হবে:

```text
nitish
65
['pollen', 'dust']
True
updated
```

---

সংক্ষেপে:
এই কোড **রোগীর ডাটা validate করে**, বিশেষ করে **৬০ বছরের বেশি রোগীর emergency contact check করে**। তারপর সেই ডাটা update বা display করার জন্য function ব্যবহার করা হয়।

---

