# 100 Days of MLOps — Learning Roadmap

A structured 100-day plan to go from Python environment basics to production-grade ML systems on Kubernetes.

---

## Phase 1: Environment & Tooling (Days 1–10)

**Goal:** Build a solid, reproducible Python development environment for ML projects.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 1 | Python Virtual Environments | venv, pip, isolation |
| 2 | Jupyter Notebook Setup | JupyterLab, kernels, extensions |
| 3 | uv Package Manager | uv, lockfiles, fast installs |
| 4 | ML Project Structure | cookiecutter, src layout, conventions |
| 5 | Makefile Automation | targets, phony rules, workflow automation |
| 6 | Pre-commit Hooks | pre-commit, hooks, automated checks |
| 7 | Code Formatting | Black, isort, Ruff |
| 8 | Type Hints & mypy | type annotations, static analysis |
| 9 | Logging Best Practices | structlog, log levels, handlers |
| 10 | DVC Init & Data Versioning | dvc init, .dvc files, remote storage |

---

## Phase 2: Data Management (Days 11–19)

**Goal:** Version, validate, and manage ML datasets reliably.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 11 | DVC Pipelines | dvc run, stages, DAGs |
| 12 | DVC Remote Storage | S3, GCS, Azure Blob |
| 13 | DVC Metrics & Plots | metrics.json, dvc plots |
| 14 | Great Expectations | data validation, expectations, checkpoints |
| 15 | Pandas Profiling | ydata-profiling, EDA automation |
| 16 | Feature Engineering Pipelines | sklearn Pipeline, ColumnTransformer |
| 17 | Dataset Versioning Strategies | snapshots, deltas, partitioning |
| 18 | Data Lineage | tracking data origins and transformations |
| 19 | Schema Registry | Avro, Protobuf, schema evolution |

---

## Phase 3: Experiment Tracking (Days 20–30)

**Goal:** Track, compare, and reproduce ML experiments systematically.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 20 | MLflow Experiment Tracking | runs, params, metrics, artifacts |
| 21 | MLflow Projects | MLproject file, reproducible runs |
| 22 | MLflow Model Registry | staging, production, versioning |
| 23 | MLflow Serving | mlflow models serve, REST API |
| 24 | Hyperparameter Tuning (Optuna) | trials, pruning, study |
| 25 | Cross-Validation Strategies | k-fold, stratified, time-series split |
| 26 | Model Evaluation Metrics | precision, recall, AUC, calibration |
| 27 | Experiment Comparison | parallel coordinates, metric plots |
| 28 | Weights & Biases | wandb.init, sweeps, artifacts |
| 29 | Model Explainability (SHAP) | shap values, force plots, summary plots |
| 30 | Reproducible Training Runs | seeds, determinism, environment pinning |

---

## Phase 4: Model Training & Packaging (Days 31–40)

**Goal:** Build robust training pipelines and package models for deployment.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 31 | Scikit-learn Training Pipeline | estimators, fit/predict, pipelines |
| 32 | Pipelines & ColumnTransformer | preprocessing, feature unions |
| 33 | Custom Transformers | BaseEstimator, TransformerMixin |
| 34 | Model Persistence | joblib, pickle, versioned artifacts |
| 35 | ONNX Export | onnx, onnxruntime, cross-framework |
| 36 | Model Cards | documentation, bias reporting |
| 37 | Bias & Fairness Checks | fairlearn, demographic parity |
| 38 | A/B Testing Framework | traffic splitting, statistical significance |
| 39 | Shadow Deployment | mirroring traffic, offline comparison |
| 40 | Canary Releases | gradual rollout, rollback strategy |

---

## Phase 5: Feature Stores (Days 41–49)

**Goal:** Build and serve features consistently across training and inference.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 41 | Feast Feature Store | feast init, feature views, entities |
| 42 | Feast Online Store | Redis, DynamoDB, low-latency serving |
| 43 | Feast Offline Store | BigQuery, Redshift, historical features |
| 44 | Feature Pipelines | ingestion, transformation, scheduling |
| 45 | Point-in-Time Joins | training dataset generation, leakage prevention |
| 46 | Feature Monitoring | drift, freshness, completeness |
| 47 | Hopsworks Feature Store | alternative feature store platform |
| 48 | Feature Store Patterns | shared features, feature reuse |
| 49 | Real-time Feature Serving | streaming features, Kafka integration |

---

## Phase 6: Containerization & Serving (Days 50–66)

**Goal:** Package ML models in containers and serve them at scale.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 50 | Docker Training Environment | Dockerfile, build args, volumes |
| 51 | Multi-stage Docker Builds | builder pattern, minimal images |
| 52 | Docker Compose for ML | multi-service stacks, networking |
| 53 | Container Registry | ECR, GCR, image tagging |
| 54 | Docker Layer Caching | cache optimization, build speed |
| 55 | Distroless & Slim Images | security, image size reduction |
| 56 | BentoML Serving | bentoml save, bentoml serve |
| 57 | Flask Model Serving | REST API, request/response, health checks |
| 58 | FastAPI Model Serving | async, Pydantic, OpenAPI docs |
| 59 | Async Inference | background tasks, queues |
| 60 | Batch Inference | batch prediction, scheduling |
| 61 | gRPC Serving | protobuf, streaming, performance |
| 62 | Triton Inference Server | multi-framework, dynamic batching |
| 63 | TorchServe | PyTorch model serving |
| 64 | TF Serving | TensorFlow SavedModel serving |
| 65 | Model Caching & Warm-up | latency reduction, pre-loading |
| 66 | Load Testing (Locust) | throughput, latency, SLOs |

---

## Phase 7: Monitoring & Observability (Days 67–75)

**Goal:** Observe, alert on, and understand ML system behavior in production.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 67 | Prometheus + Grafana | scraping, PromQL, dashboards |
| 68 | Custom Prometheus Metrics | Counter, Gauge, Histogram, Summary |
| 69 | Alertmanager Rules | alerting rules, routing, silences |
| 70 | Grafana Dashboards as Code | JSON model, provisioning |
| 71 | OpenTelemetry Tracing | spans, traces, context propagation |
| 72 | Jaeger Distributed Tracing | trace visualization, sampling |
| 73 | ELK Stack Logging | Elasticsearch, Logstash, Kibana |
| 74 | Model Drift Detection | statistical tests, PSI, KS test |
| 75 | Data Drift (Evidently AI) | evidently reports, test suites |

---

## Phase 8: CI/CD & GitOps (Days 76–84)

**Goal:** Automate the ML lifecycle from code commit to production deployment.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 76 | ML CI/CD Pipelines | pipeline stages, triggers, artifacts |
| 77 | GitHub Actions for ML | workflows, matrix builds, caching |
| 78 | GitLab CI for ML | .gitlab-ci.yml, runners, stages |
| 79 | Automated Model Testing | unit tests, integration tests, smoke tests |
| 80 | Model Validation Gates | threshold checks, promotion criteria |
| 81 | GitOps with ArgoCD | app of apps, sync policies |
| 82 | Helm Charts for ML | chart structure, values, templating |
| 83 | Kustomize | overlays, patches, bases |
| 84 | Secrets Management (Vault) | dynamic secrets, Kubernetes auth |

---

## Phase 9: ML Orchestration (Days 85–91)

**Goal:** Build and run production ML pipelines on Kubernetes-native platforms.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 85 | Argo Workflows | workflow YAML, templates, DAGs |
| 86 | Argo DAG Pipelines | dependencies, parallel steps |
| 87 | Argo Events | event sources, sensors, triggers |
| 88 | Kubeflow Pipelines | KFP SDK, components, runs |
| 89 | Kubeflow Katib (AutoML) | hyperparameter search, NAS |
| 90 | Kubeflow Serving (KServe) | InferenceService, canary, explainers |
| 91 | Vertex AI Pipelines | managed pipelines, Vertex components |

---

## Phase 10: Kubernetes & Production (Days 92–100)

**Goal:** Deploy, scale, and operate ML systems on Kubernetes in production.

| Day | Topic | Key Skills |
|-----|-------|------------|
| 92 | Kubernetes Model Deployment | Deployment, Service, Ingress |
| 93 | Kubernetes HPA for ML | CPU/custom metrics autoscaling |
| 94 | GPU Scheduling in K8s | NVIDIA device plugin, resource limits |
| 95 | Istio Service Mesh | traffic management, mTLS, observability |
| 96 | Knative Serving | scale-to-zero, revisions, traffic splitting |
| 97 | Multi-cluster ML | federation, cross-cluster serving |
| 98 | Cost Optimization | spot instances, bin packing, rightsizing |
| 99 | ML Platform Design | platform thinking, self-service, abstractions |
| 100 | Observability Capstone | full-stack observability for ML systems |

---

## Capstone Projects

After completing the 100 days, four capstone projects tie everything together:

1. **End-to-End ML System** — Training pipeline → model registry → serving → monitoring
2. **Argo Workflows Pipeline** — Kubernetes-native ML pipeline with DAG orchestration
3. **Monitoring & Retraining** — Drift detection triggering automated retraining
4. **Observability Stack** — Full Prometheus + Grafana + Jaeger + ELK for an ML system
