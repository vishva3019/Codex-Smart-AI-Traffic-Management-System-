# Codex-Smart-AI-Traffic-Management-System-
# 🚦 CODEX AI Traffic Management System

An **AI-powered smart traffic analysis platform** that uses Azure Maps and backend intelligence to provide real-time route insights, congestion prediction, and environmental impact analysis.

---

## 🌟 Overview

CODEX is a modern traffic intelligence system designed to:

* Analyze real-time routes using **Azure Maps API**
* Simulate **AI-based traffic delay**
* Provide **environmental impact metrics (CO₂ & fuel usage)**
* Deliver smart recommendations for efficient travel

---

## 🧠 Key Features

* 🔐 **Secure Login System** (Frontend + Backend API)
* 🗺️ **Real-Time Route Visualization** using Azure Maps
* 🚗 **AI Traffic Delay Simulation**

  * Peak hour detection
  * Distance-based congestion
  * Dynamic randomness for realism
* 🌍 **Environmental Impact Analysis**

  * Carbon footprint (CO₂)
  * Fuel consumption estimation
* 🤖 **AI-Based Optimization Suggestions**
* ⚡ **Interactive Dashboard UI**
* 📡 **Live Data Integration with Backend (Flask API)**

---

## 🏗️ Tech Stack

### Frontend

* HTML5
* CSS3 (Glassmorphism UI)
* JavaScript (Vanilla JS)
* Azure Maps SDK

### Backend

* Python (Flask)
* REST API
* Azure Maps API Integration

---

## 📂 Project Structure

```
CODEX-AI-Traffic/
│
├── frontend/
│   ├── login.html
│   ├── dashboard.html
│   ├── analysis.html
│
├── backend/
│   ├── app.py
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/codex-ai-traffic.git
cd codex-ai-traffic
```

---

### 2️⃣ Backend Setup (Flask)

```
cd backend
pip install flask flask-cors requests
python app.py
```

Backend will run on:

```
http://127.0.0.1:8080
```

---

### 3️⃣ Run Frontend

Simply open:

```
login.html
```

in your browser.

---

## 🔑 Configuration

Replace your Azure Maps key in:

* `dashboard.html`
* `analysis.html`
* `app.py`

```
AZURE_MAPS_KEY = "YOUR_KEY_HERE"
```

---

## 🚀 How It Works

1. User logs in via **Login Page**
2. Selects source & destination in **Dashboard**
3. Route is fetched using Azure Maps
4. Data is stored and sent to backend
5. Backend applies **AI delay simulation**
6. Results displayed in **Analysis Page**

---

## 🧪 AI Traffic Logic

The system enhances real-time data using:

* ⏰ Peak hour detection (8–11 AM, 5–9 PM)
* 📍 Distance-based congestion modeling
* 🎲 Random variation for realism
* 🔗 Hybrid of Azure + AI prediction

---

## 📊 Sample Output

* Distance: 16.49 km
* Estimated Time: 19 min
* Traffic Delay: 8–18 min (dynamic)
* Fuel Usage: Calculated based on distance + delay

---

## 🌍 SDG Alignment

This project supports:

* **SDG 11** – Sustainable Cities & Communities
* **SDG 13** – Climate Action

---

## 🔮 Future Enhancements

* 📊 Traffic analytics dashboard (charts)
* 🎥 Vehicle detection using OpenCV
* 🔴 Live congestion heatmaps
* ☁️ Deployment on Microsoft Azure
* 🔐 JWT Authentication system

---

## 👨‍💻 Author

**Vishvanth A**

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Show Your Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Share it

---
