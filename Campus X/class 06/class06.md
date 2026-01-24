
## 1. “Create” Endpoint-এর উদ্দেশ্য ও পরিকল্পনা 

### Create Endpoint কী?

Create endpoint ব্যবহার করে **নতুন resource** (এখানে নতুন patient) ডাটাবেসে যোগ করা হয়।

### এই ভিডিওর মূল লক্ষ্য:

Client যেন নতুন patient data পাঠিয়ে JSON ফাইল ডাটাবেসে  record যোগ করতে পারে।

### সম্পূর্ণ Flow:

1. Client একটি **HTTP POST request** পাঠাবে
2. Request body-তে JSON format-এ patient data থাকবে
3. Data **Pydantic model** দিয়ে validate হবে
4. Data valid হলে JSON ফাইলে save হবে

> Basic Concept:
>
> * **POST Method** → নতুন data create করতে ব্যবহৃত হয়
> * **JSON** → API-তে data আদান-প্রদানের সবচেয়ে common format

---

## 2. Request Body Concept 

### Request Body কী?

Request body হলো HTTP request-এর সেই অংশ, যেখানে client server-এ data পাঠায়।

### কোথায় ব্যবহৃত হয়:

* POST → নতুন resource তৈরি
* PUT → existing resource update

### কোথায় ব্যবহৃত হয় না:

* GET request
  → GET শুধুমাত্র data retrieve করে, body ব্যবহার করে না

### উদাহরণ:

Client request body-তে পাঠাতে পারে:

* name
* gender
* city
* age
* height
* weight

> Basic Concept:
>
> * Header → meta info
> * Body → actual data
> * URL → resource location

---

## 3. Pydantic Model দিয়ে Data Validation 

### 4.1 Pydantic কী?

Pydantic হলো একটি Python library যা:

* Data validation করে
* Data parsing করে
* Type safety নিশ্চিত করে

FastAPI স্বয়ংক্রিয়ভাবে Pydantic model ব্যবহার করে request validate করে।

---

### 3.2 Patient Model তৈরি 

### Basic Fields:

* id : str
* name : str
* city : str
* age : int
* gender : str
* height : float
* weight : float

> Advanced Note:
>
> * Type hint ভুল হলে FastAPI নিজেই error দেয়
> * Manual validation কোড লেখার দরকার হয় না

---

### 3.3 Advanced Validation ও Metadata 

### Field Metadata:

* description
* example

এগুলো Swagger UI-তে documentation হিসেবে দেখা যায়।

### Validation Rules:

* age > 0 এবং age < 120
* height > 0
* weight > 0
* gender শুধুমাত্র:

  * "Male"
  * "Female"
  * "Others"

এখানে **Literal type** ব্যবহার করা হয়েছে।

> Basic Concept:
>
> * Validation না হলে FastAPI 422 error দেয়
> * Client ভুল data পাঠালে API crash করে না

---

### 3.4 Computed Fields: BMI ও Verdict 

### Computed Field কী?

Computed field হলো এমন field:

* Client পাঠায় না
* API নিজে calculate করে

### এখানে Computed Fields:

1. **BMI**

   * Formula: weight / (height²)
2. **Verdict**

   * Underweight
   * Normal
   * Overweight
   * Obese

### Advanced Detail:

* এক computed field অন্য computed field-এর উপর depend করতে পারে
* Pydantic automatically dependency handle করে

> Real-world Benefit:
>
> * Client-side calculation দরকার নেই
> * Data consistency বজায় থাকে

---

## 4. “Create” Endpoint Implementation 

### 4.1 Endpoint Define করা 

* `@app.post("/create")`
* async function ব্যবহার করা হয়
* Parameter হিসেবে Patient model দেওয়া হয়

> FastAPI magic:
>
> * Request body → Pydantic model
> * Validation → Automatic

---

### 4.2 Existing Data Load করা 

* JSON ফাইল থেকে existing patient data পড়া হয়
* আলাদা `load_data()` function ব্যবহার করা হয়

> Best Practice:
>
> * File handling logic endpoint-এর বাইরে রাখা

---

### 4.3 Duplicate Patient ID Check 

* নতুন ID আগে আছে কিনা চেক
* থাকলে:

  * HTTPException
  * Status code: 400

> Basic Concept:
>
> * Duplicate data → data integrity সমস্যা
> * Early validation গুরুত্বপূর্ণ

---

### 4.4 নতুন Patient Add করা 

* Pydantic object → dictionary
* `model_dump()` ব্যবহার
* Computed fields automatically যুক্ত হয়

> Advanced Note:
>
> * `exclude='id'` ব্যবহার করে nested structure বানানো

---

### 4.5 JSON ফাইলে Data Save করা 

* `save_data()` utility function
* `json.dump()` ব্যবহার
* File write mode-এ খোলা হয়

> Best Practice:
>
> * Read এবং Write logic আলাদা রাখা

---

### 4.6 Response Return করা 

* Status Code: **201 Created**
* Message: “Patient Created Successfully”

> HTTP Concept:
>
> * 201 → resource successfully created
> * 400 → client error
> * 422 → validation error

---

## 5. Endpoint Testing 

### Swagger UI ব্যবহার:

* Auto-generated documentation
* POST endpoint green color-এ দেখা যায়

### Test Cases:

1. Existing ID → 400 error
2. New ID → 201 success
3. JSON file verify করা

   * BMI
   * Verdict auto calculated

---

## 6. Overall Learning Outcome

* POST request handling
* Request body concept
* Pydantic validation
* Computed fields
* Clean API design
* JSON-based lightweight database handling

