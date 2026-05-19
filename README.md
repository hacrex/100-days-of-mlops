<<<<<<< HEAD
# 100 Days of MLOps 🚀

A complete hands-on MLOps learning repository covering the full spectrum of production ML engineering — from environment setup to Kubernetes-native ML platforms.

> Inspired by the [KodeKloud 100 Days of MLOps](https://kodekloud.com) curriculum.

---

## What This Is

A daily practice log where each day covers one concrete MLOps skill. Every day folder contains:
- A focused README with objectives, commands, and learnings
- Working source code / configs in `src/`
- Shell commands in `commands.sh`
- Pinned dependencies in `requirements.txt`
- Implementation notes in `notes.md`

---

## Repository Structure

```
100-days-of-mlops/
├── days/                    # Daily practice folders (day-001 through day-100)
├── capstones/               # End-to-end project capstones
│   ├── end-to-end-ml-system/
│   ├── argo-workflows-pipeline/
│   ├── monitoring-retraining/
│   └── observability-stack/
├── docs/
│   ├── roadmap.md           # Full 100-day learning roadmap
│   └── tools-used.md        # Tool reference guide
├── assets/
│   ├── banners/
│   ├── diagrams/
│   └── screenshots/
├── scripts/
│   ├── setup.sh             # Bootstrap dev environment
│   ├── install.sh           # Install all dependencies
│   └── cleanup.sh           # Remove generated artifacts
└── templates/
    └── daily-readme-template.md
```

---

## Progress Tracker

| Day | Topic | Status |
|-----|-------|--------|
| [001](days/day-001-python-venv) | Python Virtual Environments | ✅ |
| [002](days/day-002-jupyter-setup) | Jupyter Notebook Setup | ✅ |
| [003](days/day-003-uv-lockfile-fix) | uv Package Manager & Lockfiles | ✅ |
| [004](days/day-004-ml-project-structure) | ML Project Structure | ✅ |
| [005](days/day-005-makefile-automation) | Makefile Automation | ✅ |
| 006 | Pre-commit Hooks | ⏳ |
| 007 | Code Formatting (Black, isort) | ⏳ |
| 008 | Type Hints & mypy | ⏳ |
| 009 | Logging Best Practices | ⏳ |
| [010](days/day-010-dvc-init) | DVC Init & Data Versioning | ✅ |
| 011 | DVC Pipelines | ⏳ |
| 012 | DVC Remote Storage (S3) | ⏳ |
| 013 | DVC Metrics & Plots | ⏳ |
| 014 | Data Validation with Great Expectations | ⏳ |
| 015 | Pandas Profiling | ⏳ |
| 016 | Feature Engineering Pipelines | ⏳ |
| 017 | Dataset Versioning Strategies | ⏳ |
| 018 | Data Lineage | ⏳ |
| 019 | Schema Registry | ⏳ |
| [020](days/day-020-mlflow-tracking) | MLflow Experiment Tracking | ✅ |
| 021 | MLflow Projects | ⏳ |
| 022 | MLflow Model Registry | ⏳ |
| 023 | MLflow Serving | ⏳ |
| 024 | Hyperparameter Tuning (Optuna) | ⏳ |
| 025 | Cross-Validation Strategies | ⏳ |
| 026 | Model Evaluation Metrics | ⏳ |
| 027 | Experiment Comparison | ⏳ |
| 028 | Weights & Biases Intro | ⏳ |
| 029 | Model Explainability (SHAP) | ⏳ |
| 030 | Reproducible Training Runs | ⏳ |
| [031](days/day-031-scikit-training) | Scikit-learn Training Pipeline | ✅ |
| 032 | Pipelines & ColumnTransformer | ⏳ |
| 033 | Custom Transformers | ⏳ |
| 034 | Model Persistence (joblib/pickle) | ⏳ |
| 035 | ONNX Export | ⏳ |
| 036 | Model Cards | ⏳ |
| 037 | Bias & Fairness Checks | ⏳ |
| 038 | A/B Testing Framework | ⏳ |
| 039 | Shadow Deployment | ⏳ |
| 040 | Canary Releases | ⏳ |
| [041](days/day-041-feast-feature-store) | Feast Feature Store | ✅ |
| 042 | Feast Online Store | ⏳ |
| 043 | Feast Offline Store | ⏳ |
| 044 | Feature Pipelines | ⏳ |
| 045 | Point-in-Time Joins | ⏳ |
| 046 | Feature Monitoring | ⏳ |
| 047 | Hopsworks Feature Store | ⏳ |
| 048 | Feature Store Patterns | ⏳ |
| 049 | Real-time Feature Serving | ⏳ |
| [050](days/day-050-docker-training-env) | Docker Training Environment | ✅ |
| 051 | Multi-stage Docker Builds | ⏳ |
| 052 | Docker Compose for ML | ⏳ |
| 053 | Container Registry (ECR/GCR) | ⏳ |
| 054 | Docker Layer Caching | ⏳ |
| 055 | Distroless & Slim Images | ⏳ |
| 056 | BentoML Serving | ⏳ |
| [057](days/day-057-flask-serving) | Flask Model Serving | ✅ |
| 058 | FastAPI Model Serving | ⏳ |
| 059 | Async Inference | ⏳ |
| 060 | Batch Inference | ⏳ |
| 061 | gRPC Serving | ⏳ |
| 062 | Triton Inference Server | ⏳ |
| 063 | TorchServe | ⏳ |
| 064 | TF Serving | ⏳ |
| 065 | Model Caching & Warm-up | ⏳ |
| 066 | Load Testing (Locust) | ⏳ |
| [067](days/day-067-prometheus-grafana) | Prometheus + Grafana Monitoring | ✅ |
| 068 | Custom Prometheus Metrics | ⏳ |
| 069 | Alertmanager Rules | ⏳ |
| 070 | Grafana Dashboards as Code | ⏳ |
| 071 | OpenTelemetry Tracing | ⏳ |
| 072 | Jaeger Distributed Tracing | ⏳ |
| 073 | ELK Stack Logging | ⏳ |
| 074 | Model Drift Detection | ⏳ |
| 075 | Data Drift (Evidently AI) | ⏳ |
| [076](days/day-076-ml-ci-cd) | ML CI/CD Pipelines | ✅ |
| 077 | GitHub Actions for ML | ⏳ |
| 078 | GitLab CI for ML | ⏳ |
| 079 | Automated Model Testing | ⏳ |
| 080 | Model Validation Gates | ⏳ |
| 081 | GitOps with ArgoCD | ⏳ |
| 082 | Helm Charts for ML | ⏳ |
| 083 | Kustomize | ⏳ |
| 084 | Secrets Management (Vault) | ⏳ |
| [085](days/day-085-argo-workflows) | Argo Workflows | ✅ |
| 086 | Argo DAG Pipelines | ⏳ |
| 087 | Argo Events | ⏳ |
| 088 | Kubeflow Pipelines | ⏳ |
| 089 | Kubeflow Katib (AutoML) | ⏳ |
| 090 | Kubeflow Serving (KServe) | ⏳ |
| 091 | Vertex AI Pipelines | ⏳ |
| [092](days/day-092-kubernetes-model-deployment) | Kubernetes Model Deployment | ✅ |
| 093 | Kubernetes HPA for ML | ⏳ |
| 094 | GPU Scheduling in K8s | ⏳ |
| 095 | Istio Service Mesh | ⏳ |
| 096 | Knative Serving | ⏳ |
| 097 | Multi-cluster ML | ⏳ |
| 098 | Cost Optimization | ⏳ |
| 099 | ML Platform Design | ⏳ |
| [100](days/day-100-observability-capstone) | Observability Capstone | ✅ |

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Environment | Python, uv, venv, conda |
| Experiment Tracking | MLflow, Weights & Biases |
| Data Versioning | DVC |
| Feature Store | Feast |
| Serving | Flask, FastAPI, BentoML, TorchServe |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes, Argo Workflows, Kubeflow |
| CI/CD | GitHub Actions, ArgoCD |
| Monitoring | Prometheus, Grafana, Evidently AI |
| Observability | OpenTelemetry, Jaeger, ELK |
| Data Quality | Great Expectations |
| Secrets | HashiCorp Vault |

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/100-days-of-mlops.git
cd 100-days-of-mlops

# Bootstrap your environment
chmod +x scripts/setup.sh
./scripts/setup.sh

# Navigate to a specific day
cd days/day-001-python-venv
cat README.md
```

---

## Capstone Projects

| Project | Description | Status |
|---------|-------------|--------|
| [End-to-End ML System](capstones/end-to-end-ml-system) | Full training → serving pipeline | ⏳ |
| [Argo Workflows Pipeline](capstones/argo-workflows-pipeline) | Kubernetes-native ML pipeline | ⏳ |
| [Monitoring & Retraining](capstones/monitoring-retraining) | Drift detection + auto-retraining | ⏳ |
| [Observability Stack](capstones/observability-stack) | Full observability for ML systems | ⏳ |

---

## Connect

- GitHub: [your-username](https://github.com/your-username)
- LinkedIn: [your-profile](https://linkedin.com/in/your-profile)
=======

# 100 Days of MLOps

A complete hands-on MLOps learning repository inspired by the KodeKloud 100 Days of MLOps curriculum.

## Topics Covered

- Python for ML
- DVC
- MLflow
- Docker
- FastAPI
- Flask
- BentoML
- Kubernetes
- Argo Workflows
- Kubeflow
- CI/CD for ML
- Monitoring & Observability
- Feature Stores
- Data Quality
- GitOps

## Repository Structure

```bash
days/
capstones/
docs/
assets/
scripts/
templates/
```

## Goals

- Build production-grade ML systems
- Learn AI infrastructure
- Combine DevOps + MLOps
- Create reproducible ML workflows
- Understand Kubernetes-native ML platforms

## Progress Tracker

| Day | Topic | Status |
|------|------|------|
| 1 | Python Virtual Environment | ⏳ |
| 2 | Jupyter Notebook Setup | ⏳ |
| 3 | uv Lockfile | ⏳ |
| 4 | ML Project Structure | ⏳ |

## Tech Stack

- Python
- MLflow
- DVC
- Docker
- Kubernetes
- Argo
- Kubeflow
- Prometheus
- Grafana
- Feast
- Great Expectations
- Vault

## Connect

- GitHub
- LinkedIn
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
