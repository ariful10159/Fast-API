
# 📘 Pydantic – Complete Notes (Beginner → Advanced)

## 1. Pydantic কী এবং কেন দরকার

### Pydantic পরিচিতি

* **Pydantic** হলো Python-এর একটি শক্তিশালী লাইব্রেরি, যা ব্যবহার করা হয়:

  * ডেটা ভ্যালিডেশন
  * টাইপ এনফোর্সমেন্ট
  * ডেটা মডেল তৈরির জন্য
* Python ডাইনামিক টাইপড ভাষা হওয়ায় ভুল টাইপ বা ভুল ডেটা সহজেই ঢুকে যেতে পারে।
* প্রোডাকশন-গ্রেড অ্যাপে (API, Database, ML pipeline) এটা বড় সমস্যা।

### কোথায় Pydantic ব্যবহার হয়

* FastAPI (request/response validation + docs)
* YAML / JSON config validation
* Machine Learning pipelines
* Data ingestion layer
* Microservices communication

---

## 2. Why Pydantic is Used (সমস্যা যেগুলো সমাধান করে)

### সমস্যা ১: Python-এর Dynamic Typing

```python
def insert_patient_data(name, age):
    pass
```

* কেউ ভুল করে `age="twenty"` পাঠালে Python কিছু বলবে না।
* ভুল ডেটা সরাসরি ডেটাবেসে ঢুকে যাবে।

### Type Hinting কেন যথেষ্ট না

```python
def insert_patient_data(name: str, age: int):
    pass
```

* এটা শুধু developer hint
* Runtime-এ কোনো validation হয় না

### Manual Validation কেন খারাপ

```python
if not isinstance(age, int):
    raise TypeError
```

* একই কোড বারবার লিখতে হয়
* Scalability নেই
* Code messy হয়ে যায়

### সমস্যা ২: Data Validation

* age নেগেটিভ হতে পারে না
* email valid হতে হবে
* weight > 0 হতে হবে

👉 এসব হাতে-কলমে করলে boilerplate কোড বেড়ে যায়
👉 **এই সব সমস্যা Pydantic এক জায়গায় সমাধান করে**

---

## 3. How Pydantic Works (৩ ধাপের প্রসেস)

### ধাপ ১: Pydantic Model তৈরি

* `BaseModel` থেকে ইনহেরিট করা হয়
* এখানে schema + validation লেখা হয়

### ধাপ ২: Raw Data দিয়ে Object তৈরি

* Dictionary বা JSON ইনপুট দেওয়া হয়
* এই সময়েই validation হয়

### ধাপ ৩: Validated Object ব্যবহার

* `.name`, `.age` এর মতো attribute দিয়ে access
* Invalid হলে program থেমে যায়

---

## 4. Basic Pydantic Model Example

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

* `age="30"` → automatically `30` (type conversion)
* `age="THIRTY"` → ValidationError

---

## 5. Model Expansion (Advanced Fields)

### Supported Field Types

```python
from typing import List, Dict, Optional
from pydantic import BaseModel
```

```python
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
```

---

## 6. Required vs Optional Fields

### Default Behavior

* সব ফিল্ড required

### Optional Field বানানোর নিয়ম

```python
from typing import Optional

email: Optional[str] = None
```

### Default Value

```python
country: str = "Bangladesh"
```

---

## 7. Built-in Custom Data Types

### Email Validation

```python
from pydantic import EmailStr

email: EmailStr
```

### URL Validation

```python
from pydantic import AnyUrl

linkedin: AnyUrl
```

---

## 8. Field Function (Core Validation Tool)

```python
from pydantic import Field
```

### Numeric Constraints

```python
age: int = Field(gt=0, lt=120)
weight: float = Field(gt=0)
```

### String Constraints

```python
name: str = Field(max_length=50)
```

### List Constraints

```python
allergies: List[str] = Field(max_length=5)
```

### Metadata (Docs)

```python
name: str = Field(description="Patient full name")
```

---

## 9. Field Validator (Single Field Logic)

### Purpose

* একটি ফিল্ডের ওপর কাস্টম লজিক

```python
from pydantic import field_validator
```

```python
@field_validator("name")
@classmethod
def name_cannot_be_admin(cls, v):
    if v.lower() == "admin":
        raise ValueError("Invalid name")
    return v
```

### Email Domain Check

```python
@field_validator("email")
@classmethod
def email_domain_check(cls, v):
    if not v.endswith("@gmail.com"):
        raise ValueError("Only Gmail allowed")
    return v
```

---

## 10. Model Validator (Cross-field Validation)

### Purpose

* একাধিক ফিল্ড একসাথে যাচাই

```python
from pydantic import model_validator
```

```python
@model_validator(mode="after")
def check_married_email(self):
    if self.married and self.email is None:
        raise ValueError("Email required if married")
    return self
```

---

## 11. Computed Fields

### Purpose

* অন্য ফিল্ড থেকে হিসাব করা মান
* ইনপুটে থাকে না

```python
from pydantic import computed_field
```

```python
@computed_field
def bmi(self) -> float:
    return self.weight / (self.height ** 2)
```

---

## 12. Nested Models

### Example: Address Model

```python
class Address(BaseModel):
    city: str
    zip_code: int
```

### Patient Model with Nested Address

```python
class Patient(BaseModel):
    name: str
    address: Address
```

👉 Validation automatically nested structure-এ কাজ করে

---

## 13. Serialization (Output Conversion)

### Dictionary Output

```python
patient.model_dump()
```

### JSON Output

```python
patient.model_dump_json()
```

### Include / Exclude Fields

```python
patient.model_dump(exclude={"email"})
patient.model_dump(include={"name", "age"})
```

---

## 14. Why Pydantic is Production-Ready

* Centralized validation
* Clean, readable code
* Less bugs
* API docs auto-generate (FastAPI)
* Strong typing + flexibility

---

## 15. Real-world Usage Flow (FastAPI Example)

1. Request আসে
2. Pydantic model validate করে
3. Invalid হলে 422 error
4. Valid হলে business logic চলে

---

## 🔑 Final Summary

* Pydantic = Validation + Schema + Safety
* Boilerplate code দূর করে
* Large-scale application-এর জন্য must-have
* FastAPI শেখার আগে Pydantic বোঝা খুব জরুরি

---

