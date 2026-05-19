#!/bin/bash
# Day 85 - Argo Workflows

# --- Install Argo Workflows on Kubernetes ---
kubectl create namespace argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.5.5/install.yaml

# --- Wait for Argo to be ready ---
kubectl wait --for=condition=available deployment/workflow-controller -n argo --timeout=120s

# --- Install the Argo CLI ---
# macOS
brew install argo

# Linux
curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v3.5.5/argo-linux-amd64.gz
gunzip argo-linux-amd64.gz
chmod +x argo-linux-amd64
sudo mv argo-linux-amd64 /usr/local/bin/argo

# --- Submit a workflow ---
argo submit -n argo --watch src/ml-pipeline.yaml

# --- List workflows ---
argo list -n argo

# --- Get workflow details ---
argo get -n argo <workflow-name>

# --- View workflow logs ---
argo logs -n argo <workflow-name>

# --- Delete a workflow ---
argo delete -n argo <workflow-name>

# --- Port-forward the Argo UI ---
kubectl -n argo port-forward deployment/argo-server 2746:2746

# --- Submit with parameters ---
argo submit -n argo src/ml-pipeline.yaml \
  -p n_estimators=200 \
  -p max_depth=5

# --- Retry a failed workflow ---
argo retry -n argo <workflow-name>
