### FastAPI পরিচিতি :

* FastAPI কে সংজ্ঞায়িত করা হয়েছে একটি আধুনিক ও উচ্চ পারফরম্যান্সের Python web framework হিসেবে, যা API তৈরি করার জন্য ব্যবহৃত হয় (1:18)।
* FastAPI মূলত দুটি জনপ্রিয় Python লাইব্রেরির উপর তৈরি:

  * **Starlette**: API কীভাবে HTTP request গ্রহণ করবে এবং HTTP response পাঠাবে, সেটি পরিচালনা করে। এটি client এবং API-এর মধ্যে মূল যোগাযোগ ব্যবস্থা সামলায় (2:52)।
  * **Pydantic**: ডেটা ভ্যালিডেশনের জন্য ব্যবহৃত হয়। API-তে আসা ডেটা সঠিক টাইপ ও ফরম্যাটে আছে কিনা তা নিশ্চিত করে। এর ফলে ডেভেলপারদের হাতে করে অনেক validation কোড লিখতে হয় না (4:28)।

---

### FastAPI-এর মূল দর্শন :

FastAPI তৈরি করা হয়েছে পুরোনো Python framework (যেমন Flask)-এর দুটি বড় সমস্যার সমাধানের জন্য:

* পারফরম্যান্স সমস্যা (ধীর response, বেশি latency)
* ডেভেলপার এক্সপেরিয়েন্স (অনেক boilerplate কোড লিখতে হয়) 

এ থেকেই FastAPI-এর দুটি মূল দর্শন এসেছে:

#### 1. Fast to Run (উচ্চ পারফরম্যান্স) :

* FastAPI দিয়ে তৈরি API খুব দ্রুত কাজ করে, একসাথে অনেক ব্যবহারকারী সামলাতে পারে এবং latency কম হয়।

**Traditional Flask (Synchronous)** :

* Flask ব্যবহার করে WSGI (Web Server Gateway Interface) প্রোটোকল , যেমন Gunicorn ।
* WSGI synchronous, অর্থাৎ এক সময় একটিমাত্র request প্রসেস করে ।
* এতে blocking architecture তৈরি হয় এবং বড় স্কেলে কাজ করতে সমস্যা হতে পারে ।
* Flask-এর API কোডও synchronous ।

**FastAPI (Asynchronous)** :

* FastAPI ব্যবহার করে ASGI (Asynchronous Server Gateway Interface)।
* ASGI একসাথে একাধিক request প্রসেস করতে পারে ।
* Starlette ব্যবহার করে ASGI ইমপ্লিমেন্ট করা হয়েছে ।
* FastAPI সাধারণত Uvicorn server ব্যবহার করে, যা asynchronous ।
* FastAPI async/await সাপোর্ট করে, ফলে I/O-based কাজের সময় অন্য request ব্লক হয় না ।

**Restaurant উদাহরণ** :

* Flask হলো এমন একজন ওয়েটারের মতো, যে এক অর্ডার নেয়, রান্না শেষ না হওয়া পর্যন্ত অপেক্ষা করে, তারপর সেটি পরিবেশন করে এবং এরপর নতুন অর্ডার নেয়।
* FastAPI হলো এমন একজন ওয়েটারের মতো, যে অর্ডার নিয়ে রান্নাঘরে দিয়ে দেয়, তারপর সঙ্গে সঙ্গে আরেকটি অর্ডার নেয় এবং যেগুলো প্রস্তুত হয় সেগুলো পরিবেশন করে।

#### 2. Fast to Code (দ্রুত ডেভেলপমেন্ট) :

* FastAPI ডেভেলপারদের কম কোড লিখে দ্রুত API বানাতে সাহায্য করে।

**Automatic Input Validation** :

* Pydantic-এর কারণে ইনপুট ডেটা স্বয়ংক্রিয়ভাবে ভ্যালিডেট হয়, তাই হাতে করে validation চেক লেখার দরকার কমে যায়।

**Auto-generated Interactive Documentation** :

* API কোড লেখার সাথে সাথেই FastAPI স্বয়ংক্রিয়ভাবে সুন্দর ও interactive documentation তৈরি করে ।
* এই ডকুমেন্টেশন `/docs` endpoint-এ পাওয়া যায় ।
* এখানে endpoint গুলোর ব্যাখ্যা থাকে এবং ব্রাউজার থেকেই API টেস্ট করা যায় ।

**Modern Integration সুবিধা** :

* FastAPI আধুনিক অ্যাপের জন্য তৈরি।
* Machine Learning (scikit-learn, TensorFlow, PyTorch), authentication (OAuth), database (SQLAlchemy) এবং deployment (Docker, Kubernetes) এর সাথে সহজে কাজ করে ।

---

### Installation এবং Code Demo :

**Setup**:

* প্রথমে virtual environment তৈরি করা হয়  এবং সেটি activate করা হয় ।

**Installation**:

* `pip` দিয়ে প্রয়োজনীয় প্যাকেজ ইনস্টল করা হয়: `fastapi`, `uvicorn`, `pydantic` ।
* এখানে বলা হয়, Starlette নিজে থেকেই ইনস্টল হয়ে যায় ।

**Hello World API**:

* একটি `main.py` ফাইল তৈরি করা হয়।
* `FastAPI` ক্লাস থেকে একটি `app` অবজেক্ট বানানো হয় ।
* `/` রুটের জন্য একটি GET endpoint তৈরি করা হয় `@app.get("/")` দিয়ে ।
* এটি একটি সাধারণ “Hello World” মেসেজ রিটার্ন করে ।



**Endpoint টেস্ট করা**:

* ব্রাউজার দিয়ে API দেখা হয় ।
* নতুন endpoint যোগ করার উদাহরণ দেখানো হয়, যেমন `/about` ।

**Interactive Documentation**:

* `/docs` endpoint-এ স্বয়ংক্রিয়ভাবে তৈরি হওয়া ডকুমেন্টেশন দেখানো হয় ।
* এখানে ব্রাউজার থেকেই API explore ও test করা যায় ।
