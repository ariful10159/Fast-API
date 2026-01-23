ঠিক আছে। নিচে **নোট আকারে**, পরিষ্কারভাবে সাজিয়ে দিলাম। সব টপিক রাখা হয়েছে, শুধু **time বাদ দেওয়া হয়েছে**, যাতে পড়ে মনে রাখা সহজ হয়।

---

## HTTP Methods in FastAPI | Video 3 | CampusX

### (Patient Management System প্রজেক্ট)

---

## 1. ভূমিকা (Introduction)

* Instructor: **Nitish Singh**
* এটি FastAPI প্লেলিস্টের তৃতীয় ভিডিও
* আগের দুইটি ভিডিওতে আলোচনা করা হয়েছে:

  * API কী
  * FastAPI-এর বিস্তারিত পরিচিতি
* এই ভিডিওতে:

  * HTTP Methods ব্যাখ্যা
  * একটি বাস্তব প্রজেক্ট শুরু

---

## 2. প্রজেক্ট ওভারভিউ

### 2.1 সমস্যা (Problem Statement)

* ডাক্তাররা সাধারণত রোগীর প্রেসক্রিপশন ও রেকর্ড কাগজে রাখেন
* সমস্যা:

  * কাগজ হারিয়ে যাওয়া
  * পুরোনো ডাটা খুঁজে পাওয়া কঠিন
  * ডাক্তার ও রোগী উভয়ের জন্য ঝামেলা

### 2.2 প্রস্তাবিত সমাধান (Proposed Solution)

* একটি স্টার্টআপ আইডিয়া
* পুরো সিস্টেম অনলাইনে নিয়ে আসা
* ডাক্তারদের জন্য একটি **API** তৈরি করা
* API ব্যবহার করে ডাক্তাররা:

  * রোগীর প্রোফাইল মেইনটেইন করতে পারবেন
  * নতুন রেকর্ড তৈরি
  * পুরোনো রেকর্ড দেখা
  * রেকর্ড আপডেট
  * রেকর্ড ডিলিট

### 2.3 API-এর মূল কাজ (API Functionality)

এই প্রজেক্টে একাধিক endpoint থাকবে:

* **Create New Patient**

  * নতুন রোগীর তথ্য ফর্মের মাধ্যমে নেওয়া
  * ডাটা JSON ফাইলে সংরক্ষণ

* **View All Patients**

  * সব রোগীর তথ্য একসাথে দেখা

* **View Specific Patient**

  * patient ID ব্যবহার করে নির্দিষ্ট রোগীর তথ্য দেখা

* **Update Patient Record**

  * বিদ্যমান রোগীর তথ্য পরিবর্তন (যেমন: ওজন)

* **Delete Patient Record**

  * patient ID দিয়ে রোগীর রেকর্ড মুছে ফেলা

### 2.4 টেকনোলজি নির্বাচন

* এই বেসিক প্রজেক্টে:

  * ডাটাবেস ব্যবহার করা হয়নি
  * সহজ রাখার জন্য **JSON ফাইল** ব্যবহার করা হয়েছে

---

## 3. HTTP Methods

### 3.1 User Interaction অনুযায়ী Software এর ধরন

#### Static Software

* খুব কম user interaction
* শুধু তথ্য দেখার জন্য
* উদাহরণ:

  * ক্যালেন্ডার অ্যাপ
  * ঘড়ি (Clock)

#### Dynamic Software

* User এবং software-এর মধ্যে দুই দিক থেকে interaction
* User ডাটা দিতে পারে, পরিবর্তন করতে পারে
* উদাহরণ:

  * Microsoft Excel
  * Microsoft Word

---

### 3.2 CRUD Operations

Dynamic software-এ মূলত চার ধরনের কাজ হয়, একে বলে **CRUD**:

* **Create**

  * নতুন ডাটা যোগ করা

* **Retrieve**

  * বিদ্যমান ডাটা দেখা

* **Update**

  * পুরোনো ডাটা পরিবর্তন করা

* **Delete**

  * ডাটা মুছে ফেলা

---

## 4. Websites এবং HTTP

### 4.1 Website কীভাবে কাজ করে

* Website এক ধরনের বিশেষ software
* Softwareটি সার্ভারে ইনস্টল থাকে
* Client (browser) ইন্টারনেটের মাধ্যমে access করে
* Client ও server-এর যোগাযোগ হয় **HTTP protocol** দিয়ে

### 4.2 Static ও Dynamic Website

#### Static Website

* খুব কম interaction
* শুধু তথ্য দেখানো হয়
* উদাহরণ:

  * ব্লগ
  * সরকারি ওয়েবসাইট

#### Dynamic Website

* অনেক বেশি interaction
* User ডাটা তৈরি, পরিবর্তন, ডিলিট করতে পারে
* উদাহরণ:

  * Instagram
  * Facebook
  * Zomato

### 4.3 Dynamic Website-এ CRUD

Dynamic website-এর সব কাজ CRUD-এর মধ্যেই পড়ে:

* Instagram পোস্ট করা → Create
* ফিড দেখা → Retrieve
* প্রোফাইল এডিট → Update
* কমেন্ট ডিলিট → Delete

---

## 5. HTTP Methods এবং CRUD-এর সম্পর্ক

HTTP request-এর সাথে একটি **HTTP Method (verb)** থাকে, যা বলে দেয় কী ধরনের কাজ হবে:

* **GET**

  * Retrieve কাজের জন্য
  * ডাটা আনার জন্য

* **POST**

  * Create কাজের জন্য
  * নতুন ডাটা পাঠানোর জন্য

* **PUT**

  * Update কাজের জন্য
  * বিদ্যমান ডাটা পরিবর্তনের জন্য

* **DELETE**

  * Delete কাজের জন্য
  * ডাটা মুছে ফেলার জন্য

---

## 6. HTTP Methods Demo (Conceptual)

* **GET Request**

  * কোনো পেজ বা ডাটা দেখার সময় ব্যবহার হয়
  * Browser server-এ GET request পাঠায়

* **POST Request**

  * লগইন বা ফর্ম সাবমিট করার সময় ব্যবহার হয়
  * Username, password server-এ পাঠানো হয়

---

## 7. কোডসহ প্রজেক্ট ডেমো (FastAPI)

### 7.1 Project Setup

* আগের ভিডিওর একই প্রজেক্ট ফোল্ডার ব্যবহার
* FastAPI, Pydantic, Uvicorn ইনস্টল করা ছিল
* Virtual environment অ্যাক্টিভেট করা হয়

### 7.2 patients.json ফাইল

* `patients.json` নামে একটি ফাইল তৈরি
* ৫ জন রোগীর ডাটা রাখা হয়
* এটি একটি **mock database** হিসেবে কাজ করে

### 7.3 আগের Endpoint পরিবর্তন

* `hello` এবং `about` endpoint পরিবর্তন করা হয়
* আরও অর্থবহ response দেওয়া হয়

### 7.4 load_data() Function

* একটি helper function তৈরি করা হয়
* কাজ:

  * JSON ফাইল থেকে সব রোগীর তথ্য পড়া
  * সেই ডাটা return করা
* Python-এর `json` module ব্যবহার করা হয়

---

### 7.5 `/view` Endpoint

* HTTP Method: **GET**
* কাজ:

  * `load_data()` function কল করা
  * সব রোগীর তথ্য আনা
  * Client-এর কাছে response হিসেবে পাঠানো

---

### 7.6 Application Run এবং Testing

* Uvicorn দিয়ে FastAPI অ্যাপ রান করা হয়
* Browser থেকে `/view` endpoint access করা হয়
* সব রোগীর ডাটা দেখা যায়
* `/docs` এ গিয়ে Swagger UI-তে:

  * নতুন GET endpoint
  * তার কাজ দেখা যায়

---

## 8. ভবিষ্যৎ পরিকল্পনা (Outro)

পরবর্তী ভিডিওগুলোতে যোগ করা হবে:

* নির্দিষ্ট রোগীর তথ্য দেখার endpoint
* বিভিন্ন parameter অনুযায়ী রোগীর ডাটা sort করার endpoint

---

চাও তো আমি এটাকে

* **PDF নোট স্টাইল**,
* **Exam short notes**,
* অথবা **Interview-ready summary** বানিয়ে দিতে পারি।
