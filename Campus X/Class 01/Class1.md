## API কী? (Software perspective) 

* **Definition:**
  API হলো এমন একটি ব্যবস্থা যার মাধ্যমে **দুটি software component** (যেমন front end ও back end) নির্দিষ্ট নিয়ম, protocol এবং data format ব্যবহার করে একে অপরের সাথে যোগাযোগ করে ।

* **Restaurant উদাহরণ:**

  * Customer = Frontend
  * Kitchen = Backend
  * Waiter = API
  * Menu card = Protocol

  Waiter customer এর order kitchen এ নিয়ে যায় এবং খাবার এনে দেয় ।

* **Website উদাহরণ:**

  * User যখন Udemy-তে course search করে
  * Frontend API দিয়ে backend-এ request পাঠায়
  * Backend database থেকে data নিয়ে
  * API দিয়ে frontend-এ পাঠায়
  * Frontend সেটা user-কে দেখায় (10:07–11:01)

* এই যোগাযোগ সাধারণত

  * **HTTP protocol**
  * **JSON data format**
    ব্যবহার করে (11:09–11:29)।


![API illustration](image.png)


## API কেন দরকার:  Monolithic Architecture এর সমস্যা 
### API আসার আগের সময় (Monolithic Architecture) 

* আগে পুরো application এক জায়গায় থাকত

  * Frontend
  * Backend
  * Database
* সব কিছু একই folder বা project-এ থাকত (IRCTC website উদাহরণ) 
* এটাকে বলা হয় **Monolithic Architecture** 
* এক জায়গায় সমস্যা হলে পুরো system প্রভাবিত হতো 

---

### সমস্যা ১: Third-party এর সাথে data শেয়ার করা 

* IRCTC এর মতো কোম্পানি তাদের train data
  MakeMyTrip, Yatra ইত্যাদিকে দিতে চাইত।
* Direct database access দেওয়া **খুব risky**।
* Backend এর ভিতরের function বাইরে থেকে access করা সম্ভব ছিল না।

**API Solution:**

* Backend কে frontend থেকে আলাদা করা হয়।

* Backend একটি independent application হয়।

* সামনে একটি API layer বসানো হয় (যেমন `/trains`)।

* Third-party সেই API hit করে data পায়।

* Backend database থেকে data এনে API দিয়ে ফেরত দেয়।

* এতে secure data sharing সম্ভব হয় এবং নতুন income source তৈরি হয়।

* API সাধারণত ব্যবহার করে:

  * **HTTP protocol**
  * **JSON format**

* JSON universal, তাই Python, Java, PHP সব language-ই বুঝতে পারে।

---

### সমস্যা ২: একাধিক Frontend (Web, Android, iOS) 

* Smartphone আসার পর:

  * Website
  * Android app
  * iOS app
    সব দরকার হলো।
* আলাদা আলাদা monolithic app বানানো:

  * খরচ বেশি
  * Team বেশি লাগে
  * Update সব জায়গায় একসাথে হয় না

**API Solution:**

* একটাই database
* একটাই backend
* API দিয়ে সব frontend connect
* Data সব জায়গায় same থাকে
* Maintenance সহজ হয়
* Cost কমে যায়

---

## Machine Learning (ML) এ API এর ভূমিকা 

* ML-এ সবচেয়ে গুরুত্বপূর্ণ জিনিস হলো **ML model** 
* Model train হয়ে গেলে সেটা সাধারণত **binary file** আকারে save থাকে 
* আগে ML app-গুলোও monolithic architecture ব্যবহার করত।
* API ব্যবহার করলে:

  * ML model + backend আলাদা থাকে
  * API দিয়ে public access দেওয়া যায়
  * Website বা mobile app API hit করে prediction পায়
* যেমন:

  * Chatbot
  * Recommendation system
  * ML based web/app service

---

