
# FastAPI Patient Management System

## Update (PUT) & Delete (DELETE) Endpoints — Clean Notes

---

## 1. প্রজেক্ট ও ভিডিওর ওভারভিউ 

এই ভিডিওটি CampusX FastAPI সিরিজের অংশ, যেখানে একটি **Patient Management System API** তৈরি করা হচ্ছে।
এই ভিডিওতে মূলত **Update** এবং **Delete** functionality যোগ করা হয়েছে, যার মাধ্যমে পুরো **CRUD cycle** সম্পূর্ণ হয়।

### CRUD মানে কী?

* **Create** → নতুন data যোগ করা
* **Retrieve** → data দেখা
* **Update** → existing data পরিবর্তন করা
* **Delete** → data মুছে ফেলা

---

## 2. Existing Endpoints রিক্যাপ 

ভিডিও শুরুতে আগের তৈরি করা endpoint গুলো রিভিউ করা হয়:

### 2.1 View Endpoint 

* সব patient-এর সম্পূর্ণ তথ্য দেখায়
* JSON ফাইল ডাটাবেস থেকে data read করে

### 2.2 Patient Endpoint 

* Path parameter ব্যবহার করে
* নির্দিষ্ট ID-র patient-এর তথ্য দেখায়

> Basic Concept:
> Path parameter URL-এর অংশ হয়
> উদাহরণ: `/patient/P001`

---

### 2.3 Sort Endpoint 

* Query parameter ব্যবহার করে
* Weight, height বা BMI অনুযায়ী patient list sort করে

> Basic Concept:
> Query parameter URL-এর শেষে থাকে
> উদাহরণ: `?sort_by=weight`

---

### 2.4 Create Endpoint 

* POST method ব্যবহার করে
* নতুন patient JSON ডাটাবেসে যোগ করে
* Pydantic দিয়ে data validation হয়

---

## 3. Update Endpoint (PUT Method) 

---

## 3.1 Update Endpoint কী এবং কেন? 

Update endpoint ব্যবহার করা হয় **existing patient-এর তথ্য পরিবর্তন করার জন্য**।

### Update Endpoint-এ কী লাগে?

1. **Patient ID** → Path parameter
2. **Updated data** → Request body

> PUT vs PATCH (Basic Concept):
>
> * PUT → সাধারণত full update বোঝায়
> * PATCH → partial update
>   এই প্রজেক্টে PUT ব্যবহার করলেও partial update implement করা হয়েছে

---

## 3.2 Partial Update-এর জন্য Pydantic Model 

### কেন নতুন model দরকার?

Create model-এ সব field required
Update-এ সব field সবসময় দরকার হয় না

### PatientUpdate Model:

* সব field **Optional**
* Client শুধু যেটা পরিবর্তন করতে চায় সেটাই পাঠাতে পারে

> Advanced Concept:
> Optional field মানে field না থাকলেও error হবে না

---

## 3.3 Update Logic – Step by Step 

### Step 1: Existing Data Load করা

* JSON ফাইল থেকে সব patient data পড়া হয়

### Step 2: Patient ID Validate করা

* দেওয়া ID আছে কিনা চেক করা হয়
* না থাকলে error return

### Step 3: Existing Patient Data Extract করা

* ID অনুযায়ী patient-এর পুরনো তথ্য বের করা হয়

### Step 4: Data Update করা

* পুরনো data-এর উপর নতুন data overwrite করা হয়

> Best Practice:
>
> * Update করার আগে data validate করা বাধ্যতামূলক

---

## 3.4 BMI ও Verdict Recalculation (Tricky Part) 

### সমস্যা:

* BMI ও verdict computed fields
* Height বা weight update হলে BMI ও verdict ভুল হয়ে যেতে পারে

### সমাধান:

1. Updated dictionary-টিকে আবার Pydantic object-এ convert করা হয়
2. তারপর সেটিকে dictionary-তে রূপান্তর করা হয়

এর ফলে:

* BMI নতুন করে calculate হয়
* Verdict নতুন করে generate হয়

> Advanced Concept:
>
> * Computed fields dependency chain ঠিকভাবে maintain হয়

---

## 3.5 Update Endpoint Error Handling 

### Case 1: Patient ID পাওয়া যায়নি

* Error message return
* API crash করে না

### Case 2: Valid ID

* Data successfully update হয়
* Success response পাঠানো হয়

> HTTP Concept:
>
> * Client error → 4xx
> * Successful update → 200 OK

---

## 4. Delete Endpoint (DELETE Method) 

---

## 4.1 Delete Endpoint Concept 

Delete endpoint ব্যবহার করা হয় **existing patient record সম্পূর্ণভাবে মুছে ফেলার জন্য**।

### Delete Endpoint-এ কী লাগে?

* শুধু **Patient ID**
* Request body দরকার হয় না

> REST Rule:
> DELETE request সাধারণত body নেয় না

---

## 4.2 Delete Logic 

### Step by Step:

1. JSON ফাইল থেকে data load
2. Patient ID আছে কিনা চেক
3. ID থাকলে সেই record delete
4. Updated data JSON ফাইলে save

---

## 4.3 Delete Success ও Error Handling 

### Case 1: ID Exists

* Patient সফলভাবে delete হয়
* Success message return

### Case 2: ID Not Found

* Error response return
* Data unchanged থাকে

> Data Integrity:
>
> * ভুল ID delete করলে database corrupt হয় না

---

## 5. Project Completion & Next Steps

এই ভিডিওর মাধ্যমে:

* Patient Management API সম্পূর্ণ হলো
* CRUD operations fully implemented

### Next Topic:

* FastAPI দিয়ে **Machine Learning Model Serve করা**
* API + ML integration

---

## 6. Overall Learning Summary

এই ভিডিও থেকে যা শেখা যায়:

* PUT method দিয়ে partial update
* Optional Pydantic model design
* Computed fields recalculation
* DELETE method implementation
* Clean error handling
* Real-world CRUD API design pattern

---

