# 🚀 Flask API + Docker + Kubernetes + Helm  (DockAPI)🐳☸️

This project demonstrates deploying a simple **Flask API** using **Docker**, **Minikube Kubernetes Cluster**, and **Helm** charts.

---

## 📁 Project Structure
`Project/
├── app/
│ └── app.py
│ └── requirements.txt
├── Dockerfile
├── helm/
│ └── flask-api/
│ ├── templates/
│ │ ├── deployment.yaml
│ │ └── service.yaml
│ │ └── test-connection.yaml
│ ├── values.yaml
│ ├── Chart.yaml
│ └── templates/_helpers.tpl
├── .gitignore
├── README.md
└── redeploy.bat
`

---

## 🧪 Features

- ✅ Simple REST API built with Flask
- 🐳 Docker containerization
- ☸️ Kubernetes deployment with Helm charts
- 🚀 Tested with Minikube on Windows
- 🔄 Easy redeployment using `redeploy.bat`

---

## ⚙️ Setup Instructions

🔧 1. Build Docker Image
`docker build -t flask-api:latest .`

📦 2. Load Image into Minikube
minikube image load flask-api:latest

⎈ 3. Deploy via Helm
helm upgrade --install flask-api helm/flask-api

🌐 4. Access the API
minikube service flask-api --url
- Then open the URL in your browser.

🛠️ Redeploy on Code Change
-Modify app.py, then run: 
./redeploy.bat


 
