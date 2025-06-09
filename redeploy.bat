@echo off
echo 🔧 Building Docker image...
docker build -t flask-api:latest .

echo 📦 Loading image into Minikube...
minikube image load flask-api:latest

echo 🚀 Redeploying with Helm...
helm upgrade --install flask-api helm/flask-api

echo 🌐 Fetching service URL...
minikube service flask-api --url

pause
