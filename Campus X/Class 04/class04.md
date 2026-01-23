
## **1. Path Parameters**

### ধারণা ও উদ্দেশ্য

* Path parameter হলো **URL-এর dynamic অংশ**, যা নির্দিষ্ট resource চিহ্নিত করতে ব্যবহৃত হয়।
* উদাহরণ: patient P003-এর তথ্য fetch করা, সব রোগী নয়।

### URL Syntax

* উদাহরণ:

  ```
  localhost:8000/view/3
  ```

  এখানে `3` হলো dynamic path parameter।
* এটি পরিবর্তন করা যায় (যেমন 4 বা 5) যাতে ভিন্ন resource retrieve করা যায়।

### ব্যবহার (Use Cases)

* **Data Retrieval:** নির্দিষ্ট আইটেম fetch করা
* **Update Operations:** নির্দিষ্ট resource modify করা
* **Delete Operations:** কোন resource remove করা হবে তা নির্ধারণ করা

### কোড ডেমো: Endpoint তৈরি

* Route define করা হয়:

  ```python
  @app.get("/patient/{patient_id}")
  ```

  `{patient_id}` হলো path parameter
* Function-এ receive করা হয়:

  ```python
  def view_patient(patient_id: str):
  ```

  * ID string (উদাহরণ: P001, P002)
* Function সব patient data load করে চেক করে parameter-এর ID আছে কি না
* যদি থাকে → ডাটা return করা হয়
* যদি না থাকে → "Patient Not Found" মেসেজ return করা হয়

### Endpoint Testing

* Browser বা interactive documentation `/docs` থেকে test করা যায়:

  ```
  http://localhost:8000/patient/P003
  http://localhost:8000/patient/P005
  ```

---

## **2. Path Function (Metadata ও Validation)**

### উদ্দেশ্য

* **Path()** function ব্যবহার করা হয় metadata, validation rules এবং documentation hints যোগ করার জন্য
* API-এর usability ও readability বৃদ্ধি পায়

### বৈশিষ্ট্য

* Title ও description যোগ করা যায়
* উদাহরণ দেখানো যায় (e.g., P01)
* Validation rules যোগ করা যায়:

  * Greater/less than for numbers
  * min_length / max_length for strings
  * Regular expressions

### Implementation

* Import করা হয়:

  ```python
  from fastapi import Path
  ```
* Function definition:

  ```python
  patient_id: str = Path(..., description="ID of the patient in the DB", example="P01")
  ```

  * `...` মানে parameter **required**
* API documentation (/docs) UI-তে description ও example দেখা যায়



---

## **Path() Function in FastAPI**

`Path()` হলো FastAPI-এর একটি helper function যা **path parameters**-এর জন্য extra information দেয়। এর মূল কাজ হলো:

1. **Metadata যোগ করা** → API documentation (Swagger UI) readable করা
2. **Validation rules** প্রয়োগ করা → parameter safe ও correct রাখা
3. **Default values ও example** দেখানো → client বুঝতে পারে parameter কীভাবে use করতে হবে

Syntax:

```python
from fastapi import Path

@app.get("/patient/{patient_id}")
def get_patient(
    patient_id: str = Path(..., title="Patient ID", description="ID of the patient in DB", example="P01")
):
    return {"patient_id": patient_id}
```

---

## **Path() Options – বিস্তারিত**

| Option        | Purpose                                          | Example / Notes                           |
| ------------- | ------------------------------------------------ | ----------------------------------------- |
| `...`         | Makes the parameter **required**                 | `Path(...)`                               |
| `title`       | Adds a title in the documentation                | `title="Patient ID"`                      |
| `description` | Adds a description in Swagger UI                 | `description="ID of the patient in DB"`   |
| `example`     | Shows an example value in docs                   | `example="P01"`                           |
| `ge`          | "Greater than or equal to" (for numbers)         | `ge=1` → value must be ≥ 1                |
| `gt`          | "Greater than" (for numbers)                     | `gt=0` → value must be > 0                |
| `le`          | "Less than or equal to" (for numbers)            | `le=100` → value ≤ 100                    |
| `lt`          | "Less than" (for numbers)                        | `lt=100` → value < 100                    |
| `min_length`  | Minimum string length                            | `min_length=2` → string ≥ 2 characters    |
| `max_length`  | Maximum string length                            | `max_length=10` → string ≤ 10 characters  |
| `regex`       | Regular expression pattern for string validation | `regex="^P\d{2}$"` → matches "P01", "P23" |

---

### **Example 1: Numeric Validation**

```python
@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(..., title="Item ID", ge=1, le=100)
):
    return {"item_id": item_id}
```

* এখানে `item_id` অবশ্যই 1 থেকে 100 এর মধ্যে হতে হবে।
* 0 বা 101 দিলে automatic validation error হবে।

---

### **Example 2: String Validation with Regex**

```python
@app.get("/patients/{patient_id}")
def get_patient(
    patient_id: str = Path(..., title="Patient ID", min_length=3, max_length=5, regex="^P\d{2}$", example="P01")
):
    return {"patient_id": patient_id}
```

* ID শুরু হবে "P" দিয়ে, পরে দুইটি সংখ্যা থাকবে (e.g., P01, P23)
* String length 3–5 এর মধ্যে হতে হবে
* Swagger UI-তে example দেখাবে "P01"

---

### **Summary**

* `Path()` হলো **path parameter-এর validation + documentation** tool
* Number/ string উভয়ের জন্য ব্যবহার করা যায়
* Swagger UI-তে title, description, example automatic দেখানো হয়
* Invalid value দিলে FastAPI automatic **422 Unprocessable Entity** response দেয়



---

## **3. HTTP Status Codes**

### সংজ্ঞা

* তিন অঙ্কের সংখ্যা যা client request-এর ফলাফল server থেকে জানায়

### Communication Flow

* Client request পাঠায়
* Server process করে response দেয়, যা **HTTP status code** সহ আসে
* Code বোঝায় কি ঘটেছে: success, error, error type

### Major Categories

* **2xx (Success):** Request সফল (e.g., 200 OK)
* **3xx (Redirection):** অতিরিক্ত action প্রয়োজন
* **4xx (Client Error):** Request ভুল বা পূরণ করা যায়নি (e.g., 404 Not Found)
* **5xx (Server Error):** Server valid request fulfill করতে পারেনি (e.g., 500 Internal Server Error)

### সাধারণ কোড

* 200 OK → Request সফল
* 201 Created → Resource তৈরি হয়েছে
* 204 No Content → Request সফল, কোন content return নেই
* 400 Bad Request → ভুল ডাটা বা missing fields
* 401 Unauthorized → Authentication প্রয়োজন
* 403 Forbidden → Authentication আছে কিন্তু authorization নেই
* 404 Not Found → Resource নেই
* 500 Internal Server Error → Generic server error
* 503 Service Unavailable → Server down বা overload

### HTTPException দিয়ে Error Handling উন্নত করা

* আগের কোডে 404 Resource missing হলেও status code 200 return হতো → ভুল
* FastAPI তে ব্যবহার:

  ```python
  from fastapi import HTTPException

  raise HTTPException(status_code=404, detail="Patient Not Found")
  ```
* ফলে proper 404 status code এবং custom error message return হয়

---

## **4. Query Parameters**

### ধারণা

* Query parameter হলো **optional key-value pair**, যা URL-এর শেষে `?` এর পরে যোগ করা হয়
* URL path পরিবর্তন না করে extra data server-এ পাঠানো যায়

### উদাহরণ: Sorting

* রোগীর data sort করতে: weight, height, BMI
* Order: ascending / descending
* এই parameters optional

### URL Structure

```
http://localhost:8000/view?sort_by=height&order=descending
```

* `?` → base URL থেকে parameters আলাদা করে
* `&` → multiple parameters আলাদা করে

### ব্যবহার

* Filtering, sorting, searching, pagination

### কোড ডেমো: Sorting Endpoint

* Route:

  ```python
  @app.get("/sort")
  ```
* Function:

  ```python
  def sort_patients(sort_by: str, order: str = "ascending"):
  ```
* **Query()** function ব্যবহার করে:

  * Default value, validation, metadata যোগ করা যায়
  * উদাহরণ:

    ```python
    order: str = Query("ascending", description="Sort order")
    ```

### Implementation Details

* Validation: `sort_by` হতে হবে "height", "weight", "BMI"
* Order হতে হবে "ascending" বা "descending"
* ভুল হলে HTTPException 400 return
* Data load এবং sort:

  * All patient data load করা হয়
  * `sorted()` ব্যবহার করে dictionary values sort করা হয়
  * Key = sort_by
  * Reverse argument = order

### Endpoint Testing

* URL examples:

  ```
  http://localhost:8000/sort?sort_by=height&order=descending
  ```
* Optional parameter missing হলে default ব্যবহার হয়
* Invalid parameter → 400 Bad Request

---

## **শেষ কথা**

* **Path Parameters:** Dynamic, required parts of URL, resource retrieval/update/delete-এর জন্য
* **Query Parameters:** Optional, searching/filtering/pagination এর জন্য
* একই endpoint-এ দুটোই একসাথে ব্যবহার করা যায়

---

http://127.0.0.1:8000/sort?sort_by=height&order=desc

http://127.0.0.1:8000/sort?sort_by=bmi&order=desc

http://127.0.0.1:8000/docs#/default/sort_patients_sort_get


