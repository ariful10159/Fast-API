
## 1. Import করা অংশ

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated
```

এখানে মূলত যা দরকার:

* **BaseModel** → ডাটা validate করার জন্য
* **EmailStr** → ইমেইল ঠিক আছে কিনা চেক করে
* **field_validator** → নিজের বানানো validation function লেখার জন্য
* **List, Dict** → list ও dictionary টাইপ বোঝাতে

(AnyUrl, Field, Optional, Annotated এখানে ব্যবহার হয়নি, তাই ignore করলেও চলবে)

---

## 2. Patient class (ডাটার structure)

```python
class Patient(BaseModel):
```

এটা একটা **Pydantic Model**
সহজ ভাষায়: রোগীর ডাটা কেমন হবে, সেটা এখানে define করা হয়েছে।

---

### 2.1 ফিল্ডগুলো

```python
name: str
email: EmailStr
age: int
weight: float
married: bool
allergies: List[str]
contact_details: Dict[str, str]
```

মানে:

* `name` → string
* `email` → অবশ্যই valid email
* `age` → integer
* `weight` → float
* `married` → True / False
* `allergies` → string এর list
* `contact_details` → key-value dictionary

Pydantic এগুলো **automatic check** করবে।

---

## 3. Custom Email Validator

```python
@field_validator('email')
@classmethod
def email_validator(cls, value):
```

👉 এই function শুধু **email ফিল্ডের জন্য** চলবে

```python
valid_domains = ['hdfc.com', 'icici.com']
domain_name = value.split('@')[-1]
```

* ইমেইলকে `@` দিয়ে ভাগ করা হচ্ছে
* domain অংশ বের করা হচ্ছে
  যেমন: `abc@icici.com` → `icici.com`

```python
if domain_name not in valid_domains:
    raise ValueError('Not a valid domain')
```

* যদি domain allowed list এ না থাকে → error

```python
return value
```

* সব ঠিক থাকলে email return করে

📌 মানে:
**শুধু hdfc.com বা icici.com ইমেইল allowed**

---

## 4. Name Transformer

```python
@field_validator('name')
@classmethod
def transform_name(cls, value):
    return value.upper()
```

👉 নাম automatically **CAPITAL LETTER** এ convert হবে

* input: `ariful`
* output: `ARIFUL`

---

## 5. Age Validator

```python
@field_validator('age', mode='after')
@classmethod
def validate_age(cls, value):
```

`mode='after'` মানে:

* আগে string → int conversion হবে
* তারপর validation চলবে

```python
if 0 < value < 100:
    return value
else:
    raise ValueError('Age should be in between 0 and 100')
```

👉 বয়স 0–100 এর মধ্যে না হলে error

---

## 6. update_patient_data ফাংশন

```python
def update_patient_data(patient: Patient):
```

এই ফাংশন **Patient object** নেয়

```python
print(patient.name)
print(patient.age)
print(patient.allergies)
print(patient.married)
print('updated')
```

Validated data print করে

---

## 7. patient_info (Raw data)

```python
patient_info = {
    'name':'ariful',
    'email':'abc@icici.com',
    'age': '30',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details':{'phone':'2353462'}
}
```

খেয়াল করো:

* `age` string `'30'`
* Pydantic এটাকে int এ convert করবে

---

## 8. Patient object তৈরি (সবচেয়ে গুরুত্বপূর্ণ লাইন)

```python
patient1 = Patient(**patient_info)
```

এখানেই সব ঘটে:

✅ টাইপ conversion
✅ email domain check
✅ age check
✅ name uppercase করা

সব ঠিক থাকলে object তৈরি হবে
ভুল থাকলে এখানেই error আসবে

---

## 9. Function call

```python
update_patient_data(patient1)
```

Output হবে:

```text
NITISH
30
['pollen', 'dust']
True
updated
```

---

## একদম সহজ করে বললে

* এই কোড **API তে আসা user data safe করার জন্য**
* Pydantic নিশ্চিত করে:

  * ভুল email ঢুকবে না
  * বয়স ভুল হবে না
  * নাম format ঠিক থাকবে
* Backend development এ এটা খুব common pattern

---
