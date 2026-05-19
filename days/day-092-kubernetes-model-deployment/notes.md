<<<<<<< HEAD
# Day 92 — Implementation Notes

## What I Did

Deployed the Flask ML API from Day 57 to Kubernetes with a Deployment, Service, and Ingress. Practiced rolling updates and rollbacks.

## Kubernetes Manifests

### Namespace

```yaml
# src/k8s/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ml-serving
```

### Deployment

```yaml
# src/k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-api
  namespace: ml-serving
  labels:
    app: ml-api
    version: v1.0.0
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
        version: v1.0.0
    spec:
      containers:
        - name: ml-api
          image: ml-api:v1.0.0
          ports:
            - containerPort: 8080
          env:
            - name: MODEL_PATH
              value: /models/model.joblib
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
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```

### Ingress

```yaml
# src/k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ml-api
  namespace: ml-serving
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: ml-api.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: ml-api
                port:
                  number: 80
```

## Rolling Update Strategy

```
maxSurge: 1       → At most 1 extra pod during update (4 pods total during rollout)
maxUnavailable: 0 → No pods go down before new ones are ready (zero-downtime)
```

## Liveness vs Readiness Probes

| Probe | Purpose | Failure Action |
|-------|---------|----------------|
| Liveness | Is the container alive? | Restart the container |
| Readiness | Is the container ready to serve traffic? | Remove from Service endpoints |
| Startup | Has the container started? | Restart if not started in time |

## Resource Requests vs Limits

- **Requests**: What Kubernetes uses for scheduling (guaranteed)
- **Limits**: Maximum the container can use (throttled/OOM-killed if exceeded)

For ML models: set memory limit generously (models can be large), CPU limit conservatively.

## Observations

- The readiness probe is critical — without it, traffic is sent to pods before the model is loaded
- Rolling updates with `maxUnavailable: 0` ensure zero downtime
- Resource limits prevent one pod from starving others on the same node
=======
# Notes

Add your implementation notes here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
