<<<<<<< HEAD
#!/bin/bash
# Day 10 - DVC Init & Data Versioning

# --- Install DVC ---
pip install dvc==3.49.0

# --- Install DVC with S3 support ---
pip install "dvc[s3]==3.49.0"

# --- Initialize DVC in a git repo ---
git init
dvc init

# --- Check what dvc init created ---
ls -la .dvc/

# --- Create a sample dataset ---
mkdir -p data/raw
echo "id,feature1,feature2,label" > data/raw/train.csv
echo "1,0.5,1.2,0" >> data/raw/train.csv
echo "2,1.3,0.8,1" >> data/raw/train.csv

# --- Add the dataset to DVC ---
dvc add data/raw/train.csv

# --- See what was created ---
cat data/raw/train.csv.dvc
cat data/.gitignore

# --- Commit the pointer file to git ---
git add data/raw/train.csv.dvc data/.gitignore .dvc/
git commit -m "Track train.csv with DVC"

# --- Configure a local remote for testing ---
dvc remote add -d localremote /tmp/dvc-storage
dvc remote list

# --- Push data to remote ---
dvc push

# --- Simulate a fresh clone ---
rm data/raw/train.csv

# --- Pull data back ---
dvc pull

# --- Check DVC status ---
dvc status

# --- Update the dataset and track the new version ---
echo "3,2.1,0.3,1" >> data/raw/train.csv
dvc add data/raw/train.csv
git add data/raw/train.csv.dvc
git commit -m "Add row 3 to train.csv"
dvc push
=======
#!/bin/bash

# Add commands here
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
