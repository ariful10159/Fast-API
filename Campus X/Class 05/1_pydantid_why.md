## 1. Import করা অংশ

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
```

এখানে যা করা হয়েছে:

* **BaseModel** → Pydantic-এর মূল ক্লাস। ডাটা ভ্যালিডেশন ও টাইপ চেকের জন্য।
* **EmailStr** → ইমেইল সঠিক ফরম্যাটে আছে কিনা চেক করে।
* **AnyUrl** → URL (যেমন LinkedIn লিংক) সঠিক কিনা চেক করে।
* **Field** → ফিল্ডের উপর extra validation ও metadata যোগ করার জন্য।
* **List, Dict, Optional** → টাইপ hint এর জন্য।
* **Annotated** → টাইপের সাথে Field-এর extra তথ্য যুক্ত করতে ব্যবহৃত হয়।

---

## 2. Patient মডেল তৈরি

```python
class Patient(BaseModel):
```

এটা একটা **Pydantic Model**। এখানে রোগীর ডাটার structure define করা হয়েছে।

---

### 2.1 name ফিল্ড

```python
name: Annotated[str, Field(
    max_length=50,
    title='Name of the patient',
    description='Give the name of the patient in less than 50 chars',
    examples=['Nitish', 'Amit']
)]
```

* টাইপ: `str`
* সর্বোচ্চ ৫০ অক্ষর
* title, description, examples → API documentation এর জন্য
* বেশি হলে error দেবে

---

### 2.2 email ফিল্ড

```python
email: EmailStr
```

* অবশ্যই valid email হতে হবে
* ভুল ইমেইল দিলে error হবে

---

### 2.3 linkedin_url ফিল্ড

```python
linkedin_url: AnyUrl
```

* অবশ্যই valid URL হতে হবে
* যেমন `http://linkedin.com/...`

---

### 2.4 age ফিল্ড

```python
age: int = Field(gt=0, lt=120)
```

* বয়স integer হবে
* 0 এর বেশি এবং 120 এর কম হতে হবে

---

### 2.5 weight ফিল্ড

```python
weight: Annotated[float, Field(gt=0, strict=True)]
```

* টাইপ: float
* 0 এর বেশি হতে হবে
* `strict=True` মানে string দিলে convert করবে না
  (যেমন `"75.2"` দিলে error হবে)

---

### 2.6 married ফিল্ড

```python
married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
```

* টাইপ: boolean (True/False)
* optional, না দিলে `None` হবে

---

### 2.7 allergies ফিল্ড

```python
allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
```

* List of string
* optional
* সর্বোচ্চ ৫টা allergy রাখা যাবে

---

### 2.8 contact_details ফিল্ড

```python
contact_details: Dict[str, str]
```

* key-value আকারে ডাটা
* যেমন: phone, address ইত্যাদি

---

## 3. update_patient_data ফাংশন

```python
def update_patient_data(patient: Patient):
```

* এই ফাংশন **Patient টাইপের object** নেয়

```python
print(patient.name)
print(patient.age)
print(patient.allergies)
print(patient.married)
print('updated')
```

* patient object থেকে ডাটা বের করে print করছে

---

## 4. patient_info ডিকশনারি

```python
patient_info = {
    'name':'nitish',
    'email':'abc@gmail.com',
    'linkedin_url':'http://linkedin.com/1322',
    'age': '30',
    'weight': 75.2,
    'contact_details':{'phone':'2353462'}
}
```

খেয়াল করো:

* `age` এখানে string `'30'`
* Pydantic এটা automaticভাবে `int` এ convert করে নেয়

---

## 5. Patient object তৈরি

```python
patient1 = Patient(**patient_info)
```

* dictionary unpack করে Patient model এ পাঠানো হয়েছে
* সব validation এখানে হয়
* ভুল হলে এখানেই error দেবে

---

## 6. ফাংশন কল

```python
update_patient_data(patient1)
```

* validated Patient object ফাংশনে পাঠানো হয়েছে
* output হবে:

```text
nitish
30
None
None
updated
```

---

## সংক্ষেপে বললে

* এই কোডটি **FastAPI / Backend API তে request body validate করার জন্য** ব্যবহার হয়
* Pydantic নিশ্চিত করে:

  * ডাটা সঠিক টাইপের
  * ভুল input ঢুকতে না পারে
  * API clean ও safe থাকে
---


কোড **এক্সিকিউশন শুরু হয় এই লাইন থেকে** 👇

```python
patient1 = Patient(**patient_info)
```

এবং এরপরের লাইনটি:

```python
update_patient_data(patient1)
```

---
