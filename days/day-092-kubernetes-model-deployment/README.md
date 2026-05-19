<<<<<<< HEAD
# Day 92 - Kubernetes Model Deployment

## Objective

Deploy an ML serving API to Kubernetes with a Deployment, Service, and Ingress — with proper health checks, resource limits, and rolling update strategy.

## Background

Kubernetes is the standard platform for running production ML workloads. It handles scaling, self-healing, rolling updates, and resource management. This day covers the core Kubernetes objects needed to deploy an ML API.

## Topics Covered

- Kubernetes Deployment for ML APIs
- Service types: ClusterIP, NodePort, LoadBalancer
- Ingress for external access
- Liveness and readiness probes
- Resource requests and limits
- Rolling updates and rollbacks
- ConfigMaps and Secrets for configuration

## Tools Used

- `kubectl` — Kubernetes CLI
- `Kubernetes` — Container orchestration platform

## Prerequisites

- Days 1–85 completed
- Kubernetes cluster running (minikube, kind, or cloud)
- ML API Docker image built and pushed

## Setup

```bash
cd days/day-092-kubernetes-model-deployment

# Create namespace
kubectl create namespace ml-serving

# Deploy
kubectl apply -f src/k8s/

# Check status
kubectl get all -n ml-serving
```

## Kubernetes Manifests

### Deployment

```yaml
# src/k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-api
  namespace: ml-serving
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ml-api
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: ml-api
    spec:
      containers:
        - name: ml-api
          image: ml-api:v1.0.0
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: "100m"
              memory: "256Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
```

### Service

```yaml
# src/k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: ml-api
  namespace: ml-serving
spec:
  selector:
    app: ml-api
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

## Key Commands

```bash
# Deploy
kubectl apply -f src/k8s/

# Check status
kubectl get pods -n ml-serving
kubectl rollout status deployment/ml-api -n ml-serving

# Port-forward for local testing
kubectl port-forward service/ml-api 8080:80 -n ml-serving

# Scale
kubectl scale deployment ml-api --replicas=5 -n ml-serving

# Rolling update
kubectl set image deployment/ml-api ml-api=ml-api:v2.0.0 -n ml-serving

# Rollback
kubectl rollout undo deployment/ml-api -n ml-serving

# View logs
kubectl logs -f deployment/ml-api -n ml-serving
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Always set both `livenessProbe` and `readinessProbe` — without them, Kubernetes sends traffic to pods that aren't ready
- `maxUnavailable: 0` in the rolling update strategy ensures zero-downtime deployments
- Resource `requests` affect scheduling; `limits` affect runtime behavior — set both
- Use `ClusterIP` for internal services; `LoadBalancer` or `Ingress` for external access
- `kubectl rollout undo` is your emergency rollback — it's instant

## Common Pitfalls

- Not setting resource limits — one pod can consume all node resources
- Missing readiness probe — traffic goes to pods before the model is loaded
- Using `latest` image tag — Kubernetes may not pull the new image

## References

- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Kubernetes Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

## Next Steps

- Day 93: Kubernetes HPA — autoscaling based on CPU and custom metrics
=======
# Day 92 - Kubernetes Model Deployment

## Objective
Document hands-on implementation and learnings for this MLOps task.

## Topics Covered
- TODO

## Tools Used
- Python
- Docker
- Kubernetes
- MLflow

## Commands

```bash
# Add commands here
```

## Learnings
- TODO

## Screenshots
Add screenshots here.

## References
- Official Documentation
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
