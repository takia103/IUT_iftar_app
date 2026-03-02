# 🍽 Iftar Microservice Ordering System

## 📌 Overview
This is a microservice-based Iftar meal ordering system.
Students can log in, select platters, track live order status, and collect meals.
Admin can monitor service health.

---

## 🚀 Features

- Student Authentication (Database Based)
- Budget Deduction System
- Live Order Status Tracking
- Separate Microservices Architecture
- Admin Health Monitoring
- Modern UI Design

---

## 🏗 Architecture

System contains 4 microservices:

- Gateway (Main UI + API Gateway)
- Identity Service (Login + Budget)
- Order Service (Order Processing)
- Stock Service (Inventory Simulation)

All services communicate via HTTP REST APIs.

---

## 🛠 Technologies Used

- Python
- Flask
- SQLite
- HTML / CSS / JavaScript
- REST API

---

## 📂 Project Structure

```
iftar-system/
│
├── gateway/
│   ├── app.py
│   ├── template/
│   └── static/
│
├── identity_service/
│   ├── app.py
│   └── students.db
│
├── order_service/
│   └── app.py
│
├── stock_service/
│   └── app.py
```

---

## ⚙ Installation Guide

1. Clone the repository

```
git clone <your-repo-link>
cd iftar-system
```

2. Install dependencies

```
pip install flask requests pyjwt werkzeug
```

3. Initialize Database

```
cd identity_service
python init_db.py
```

---

## ▶ How to Run

Open 4 separate terminals:

### Terminal 1
```
cd identity_service
python app.py
```

### Terminal 2
```
cd order_service
python app.py
```

### Terminal 3
```
cd stock_service
python app.py
```

### Terminal 4
```
cd gateway
python app.py
```

---

## 🌐 Access System

Open browser:

```
http://localhost:5000
```

Test Login:

Student ID: 240021127  
Password: rezwan  

---

## 📡 API Endpoints

### Identity Service
- POST /login
- POST /deduct

### Order Service
- POST /order
- GET /status/<id>

---

## 📊 Future Improvements

- Docker Support
- JWT Authentication Validation
- Real Stock Deduction
- Metrics & Monitoring Dashboard
- Payment Gateway Integration

---

## 👩‍💻 Developed For
Microservices Architecture Project

## Demo Video
https://drive.google.com/file/d/17onqc8K74S7IirPlb1ta39gHeLw8g2lN/view
