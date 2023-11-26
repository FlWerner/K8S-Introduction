---Build Demo in Docker---
docker build -t demo:5 .

---Build Demo with MiniKube---
minikube image build -t demo:4 .--> laufende nummer anpassen

--Start Deployment--
kubectl apply -f deployment.yaml

--Get Kubernetes Service
kubectl get svc

--Port-Forwarding--
kubectl port-forward service/servicehra 8080:8080

--Scale Deployment--
kubectl scale --replicas=4 deployment/hra
