<<<<<<< HEAD
# Tools & Technologies Reference

A quick reference for every tool used across the 100 days.

---

## Environment & Package Management

| Tool | Purpose | Install |
|------|---------|---------|
| [Python](https://python.org) | Primary language | `brew install python` / official installer |
| [venv](https://docs.python.org/3/library/venv.html) | Virtual environments | Built into Python 3.3+ |
| [uv](https://github.com/astral-sh/uv) | Fast Python package manager | `pip install uv` |
| [pip](https://pip.pypa.io) | Package installer | Bundled with Python |
| [conda](https://conda.io) | Environment + package manager | Miniconda installer |
| [pyenv](https://github.com/pyenv/pyenv) | Python version management | `brew install pyenv` |

## Code Quality

| Tool | Purpose | Install |
|------|---------|---------|
| [Black](https://black.readthedocs.io) | Code formatter | `pip install black` |
| [isort](https://pycqa.github.io/isort) | Import sorter | `pip install isort` |
| [Ruff](https://docs.astral.sh/ruff) | Fast linter | `pip install ruff` |
| [mypy](https://mypy.readthedocs.io) | Static type checker | `pip install mypy` |
| [pre-commit](https://pre-commit.com) | Git hook manager | `pip install pre-commit` |

## Data Versioning

| Tool | Purpose | Install |
|------|---------|---------|
| [DVC](https://dvc.org) | Data & model versioning | `pip install dvc` |
| [DVC S3](https://dvc.org/doc/user-guide/data-management/remote-storage/amazon-s3) | S3 remote storage | `pip install dvc-s3` |

## Data Quality

| Tool | Purpose | Install |
|------|---------|---------|
| [Great Expectations](https://greatexpectations.io) | Data validation | `pip install great-expectations` |
| [ydata-profiling](https://ydata-profiling.ydata.ai) | Automated EDA | `pip install ydata-profiling` |
| [Evidently AI](https://evidentlyai.com) | ML monitoring & drift | `pip install evidently` |

## Experiment Tracking

| Tool | Purpose | Install |
|------|---------|---------|
| [MLflow](https://mlflow.org) | Experiment tracking, model registry | `pip install mlflow` |
| [Weights & Biases](https://wandb.ai) | Experiment tracking, sweeps | `pip install wandb` |
| [Optuna](https://optuna.org) | Hyperparameter optimization | `pip install optuna` |

## ML Frameworks

| Tool | Purpose | Install |
|------|---------|---------|
| [scikit-learn](https://scikit-learn.org) | Classical ML | `pip install scikit-learn` |
| [PyTorch](https://pytorch.org) | Deep learning | `pip install torch` |
| [TensorFlow](https://tensorflow.org) | Deep learning | `pip install tensorflow` |
| [XGBoost](https://xgboost.readthedocs.io) | Gradient boosting | `pip install xgboost` |
| [LightGBM](https://lightgbm.readthedocs.io) | Gradient boosting | `pip install lightgbm` |

## Feature Stores

| Tool | Purpose | Install |
|------|---------|---------|
| [Feast](https://feast.dev) | Open-source feature store | `pip install feast` |
| [Hopsworks](https://hopsworks.ai) | Managed feature store | `pip install hopsworks` |

## Model Serving

| Tool | Purpose | Install |
|------|---------|---------|
| [Flask](https://flask.palletsprojects.com) | Lightweight web framework | `pip install flask` |
| [FastAPI](https://fastapi.tiangolo.com) | Async web framework | `pip install fastapi uvicorn` |
| [BentoML](https://bentoml.com) | ML model serving framework | `pip install bentoml` |
| [TorchServe](https://pytorch.org/serve) | PyTorch model server | `pip install torchserve` |
| [Triton Inference Server](https://developer.nvidia.com/triton-inference-server) | Multi-framework inference | Docker image |

## Containerization

| Tool | Purpose | Install |
|------|---------|---------|
| [Docker](https://docker.com) | Container runtime | Official installer |
| [Docker Compose](https://docs.docker.com/compose) | Multi-container apps | Bundled with Docker Desktop |
| [Buildkit](https://docs.docker.com/build/buildkit) | Advanced Docker builds | Built into Docker 23+ |

## Orchestration

| Tool | Purpose | Install |
|------|---------|---------|
| [Kubernetes](https://kubernetes.io) | Container orchestration | `kubectl` + cluster |
| [Argo Workflows](https://argoproj.github.io/workflows) | Kubernetes-native workflow engine | Helm chart |
| [Argo Events](https://argoproj.github.io/events) | Event-driven automation | Helm chart |
| [ArgoCD](https://argo-cd.readthedocs.io) | GitOps continuous delivery | Helm chart |
| [Kubeflow](https://kubeflow.org) | ML platform on Kubernetes | Manifests / Helm |
| [KServe](https://kserve.github.io) | Kubernetes model serving | Helm chart |
| [Knative](https://knative.dev) | Serverless on Kubernetes | Operator |

## Monitoring & Observability

| Tool | Purpose | Install |
|------|---------|---------|
| [Prometheus](https://prometheus.io) | Metrics collection | Helm chart / Docker |
| [Grafana](https://grafana.com) | Metrics visualization | Helm chart / Docker |
| [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager) | Alert routing | Bundled with Prometheus |
| [OpenTelemetry](https://opentelemetry.io) | Observability framework | `pip install opentelemetry-sdk` |
| [Jaeger](https://jaegertracing.io) | Distributed tracing | Docker / Helm |
| [Elasticsearch](https://elastic.co) | Log storage & search | Docker / Helm |
| [Logstash](https://elastic.co/logstash) | Log processing | Docker / Helm |
| [Kibana](https://elastic.co/kibana) | Log visualization | Docker / Helm |

## CI/CD

| Tool | Purpose | Config file |
|------|---------|-------------|
| [GitHub Actions](https://github.com/features/actions) | CI/CD pipelines | `.github/workflows/*.yml` |
| [GitLab CI](https://docs.gitlab.com/ee/ci) | CI/CD pipelines | `.gitlab-ci.yml` |

## Infrastructure & Secrets

| Tool | Purpose | Install |
|------|---------|---------|
| [Helm](https://helm.sh) | Kubernetes package manager | `brew install helm` |
| [Kustomize](https://kustomize.io) | Kubernetes config management | Built into kubectl |
| [HashiCorp Vault](https://vaultproject.io) | Secrets management | Docker / Helm |
| [Istio](https://istio.io) | Service mesh | `istioctl` |

## Utilities

| Tool | Purpose | Install |
|------|---------|---------|
| [Make](https://www.gnu.org/software/make) | Build automation | `brew install make` |
| [Locust](https://locust.io) | Load testing | `pip install locust` |
| [SHAP](https://shap.readthedocs.io) | Model explainability | `pip install shap` |
| [Fairlearn](https://fairlearn.org) | Fairness assessment | `pip install fairlearn` |
=======
# Tools Used

Document all tools and technologies here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
