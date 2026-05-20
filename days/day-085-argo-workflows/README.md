# Day 85 - Argo Workflows

## Objective

Build a Kubernetes-native ML pipeline using Argo Workflows, with steps for data preparation, training, evaluation, and conditional deployment.

## Background

Argo Workflows is a container-native workflow engine for Kubernetes. Each step in the workflow runs in its own container, making it easy to use different tools for different steps (e.g., Python for training, Go for data processing). It's the foundation for many ML platforms including Kubeflow Pipelines.

## Topics Covered

- Argo Workflows architecture: Workflow, Template, Step, DAG
- Writing workflow YAML
- Passing parameters between steps
- DAG vs Steps templates
- Conditional execution
- Artifacts (passing files between steps)
- Installing Argo on Kubernetes

## Tools Used

- `Argo Workflows` — Kubernetes-native workflow engine
- `kubectl` — Kubernetes CLI
- `argo` — Argo CLI

## Prerequisites

- Days 1–76 completed
- Kubernetes cluster running (minikube, kind, or cloud)
- kubectl configured

## Setup

```bash
# Install Argo Workflows
kubectl create namespace argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.5.5/install.yaml

# Port-forward the UI
kubectl -n argo port-forward deployment/argo-server 2746:2746
```

Then open `https://localhost:2746`.

## Example ML Pipeline Workflow

```yaml
# src/ml-pipeline.yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: ml-pipeline-
spec:
  entrypoint: ml-pipeline
  arguments:
    parameters:
      - name: n-estimators
        value: "100"
      - name: accuracy-threshold
        value: "0.90"

  templates:
    - name: ml-pipeline
      dag:
        tasks:
          - name: prepare-data
            template: prepare-data

          - name: train-model
            dependencies: [prepare-data]
            template: train-model
            arguments:
              parameters:
                - name: n-estimators
                  value: "{{workflow.parameters.n-estimators}}"

          - name: evaluate-model
            dependencies: [train-model]
            template: evaluate-model
            arguments:
              parameters:
                - name: accuracy-threshold
                  value: "{{workflow.parameters.accuracy-threshold}}"

    - name: prepare-data
      container:
        image: python:3.11-slim
        command: [python, -c]
        args:
          - |
            from sklearn.datasets import load_iris
            import pandas as pd
            X, y = load_iris(return_X_y=True, as_frame=True)
            X['label'] = y
            X.to_parquet('/tmp/data.parquet')
            print("Data prepared")

    - name: train-model
      inputs:
        parameters:
          - name: n-estimators
      container:
        image: python:3.11-slim
        command: [python, -c]
        args:
          - |
            import joblib
            import pandas as pd
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split

            df = pd.read_parquet('/tmp/data.parquet')
            X, y = df.drop('label', axis=1), df['label']
            X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

            model = RandomForestClassifier(n_estimators={{inputs.parameters.n-estimators}}, random_state=42)
            model.fit(X_train, y_train)
            joblib.dump(model, '/tmp/model.joblib')
            print("Model trained")

    - name: evaluate-model
      inputs:
        parameters:
          - name: accuracy-threshold
      container:
        image: python:3.11-slim
        command: [python, -c]
        args:
          - |
            import joblib, json, sys
            import pandas as pd
            from sklearn.metrics import accuracy_score
            from sklearn.model_selection import train_test_split

            df = pd.read_parquet('/tmp/data.parquet')
            X, y = df.drop('label', axis=1), df['label']
            _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = joblib.load('/tmp/model.joblib')
            accuracy = accuracy_score(y_test, model.predict(X_test))
            threshold = {{inputs.parameters.accuracy-threshold}}

            print(f"Accuracy: {accuracy:.4f}")
            if accuracy < threshold:
                print(f"FAIL: {accuracy:.4f} < {threshold}")
                sys.exit(1)
            print(f"PASS: {accuracy:.4f} >= {threshold}")
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Each Argo step runs in its own container — you can use different images for different steps
- DAG templates define dependencies explicitly; Steps templates define sequential steps
- Artifacts (files) can be passed between steps via S3, GCS, or a PVC
- `{{workflow.parameters.name}}` accesses workflow-level parameters
- `{{inputs.parameters.name}}` accesses step-level parameters

## Common Pitfalls

- Passing large files between steps via parameters — use artifacts instead
- Not setting resource limits on containers — one step can starve others
- Using `generateName` without a unique suffix — workflow names must be unique

## References

- [Argo Workflows docs](https://argoproj.github.io/argo-workflows)
- [Argo Workflows examples](https://github.com/argoproj/argo-workflows/tree/main/examples)

## Next Steps

- Day 86: Argo DAG Pipelines — complex dependency graphs
