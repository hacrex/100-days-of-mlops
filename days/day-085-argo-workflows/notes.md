<<<<<<< HEAD
# Day 85 — Implementation Notes

## What I Did

Installed Argo Workflows on a local Kubernetes cluster (kind), wrote a DAG-based ML pipeline, and submitted it via the Argo CLI.

## Argo Concepts

| Concept | Description |
|---------|-------------|
| Workflow | A single execution of a pipeline |
| WorkflowTemplate | A reusable workflow definition |
| Template | A step definition (container, DAG, steps, script) |
| DAG | Directed Acyclic Graph — defines step dependencies |
| Artifact | Files passed between steps (stored in S3/GCS/PVC) |
| Parameter | Values passed to templates |

## Template Types

```yaml
# 1. Container template — runs a Docker container
- name: my-step
  container:
    image: python:3.11-slim
    command: [python, src/train.py]

# 2. Script template — inline script
- name: my-script
  script:
    image: python:3.11-slim
    command: [python]
    source: |
      print("Hello from Argo")

# 3. DAG template — defines dependencies
- name: my-dag
  dag:
    tasks:
      - name: step-a
        template: my-step
      - name: step-b
        dependencies: [step-a]
        template: my-script

# 4. Steps template — sequential steps
- name: my-steps
  steps:
    - - name: step-a
        template: my-step
    - - name: step-b
        template: my-script
```

## Passing Artifacts Between Steps

```yaml
templates:
  - name: train
    outputs:
      artifacts:
        - name: model
          path: /tmp/model.joblib
    container:
      image: python:3.11-slim
      command: [python, src/train.py]

  - name: evaluate
    inputs:
      artifacts:
        - name: model
          path: /tmp/model.joblib
    container:
      image: python:3.11-slim
      command: [python, src/evaluate.py]
```

## Conditional Execution

```yaml
- name: deploy
  dependencies: [evaluate]
  template: deploy-model
  when: "{{tasks.evaluate.outputs.parameters.accuracy}} > 0.90"
```

## Observations

- Argo's UI is excellent — you can see the DAG visually, view logs per step, and retry failed steps
- The YAML syntax is verbose but very explicit — no magic
- Artifacts require an S3-compatible store (MinIO works locally)
- For local development, using a shared PVC is simpler than S3 for artifacts
=======
# Notes

Add your implementation notes here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
