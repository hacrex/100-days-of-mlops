<<<<<<< HEAD
#!/bin/bash
# Day 92 - Kubernetes Model Deployment

# --- Apply all manifests ---
kubectl apply -f src/k8s/

# --- Apply individual manifests ---
kubectl apply -f src/k8s/deployment.yaml
kubectl apply -f src/k8s/service.yaml
kubectl apply -f src/k8s/ingress.yaml

# --- Check deployment status ---
kubectl get deployments -n ml-serving
kubectl rollout status deployment/ml-api -n ml-serving

# --- Check pods ---
kubectl get pods -n ml-serving
kubectl describe pod <pod-name> -n ml-serving

# --- View pod logs ---
kubectl logs -f deployment/ml-api -n ml-serving

# --- Port-forward for local testing ---
kubectl port-forward service/ml-api 8080:80 -n ml-serving

# --- Test the deployed model ---
curl http://localhost:8080/health
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# --- Scale the deployment ---
kubectl scale deployment ml-api --replicas=5 -n ml-serving

# --- Rolling update ---
kubectl set image deployment/ml-api ml-api=ml-api:v2.0.0 -n ml-serving
kubectl rollout status deployment/ml-api -n ml-serving

# --- Rollback ---
kubectl rollout undo deployment/ml-api -n ml-serving

# --- View rollout history ---
kubectl rollout history deployment/ml-api -n ml-serving

# --- Delete everything ---
kubectl delete -f src/k8s/
=======
#!/bin/bash

# Add commands here
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
