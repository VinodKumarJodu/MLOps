Steps:

Create new Conda Environment
```bash
conda create -n WineQuality python=3.7 -y
```
Activate the Environment WineQuality
```bash
conda activate WineQuality
```
Create requirements.txt file
Install the requirements.txt
```bash
pip install -r requirements.txt
```
Download the Data From below url
s://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Initialise GIT
```bash
git init
```
Initialise DVC
```bash
dvc init
```
Add the data to dvc
```bash
dvc add data_given/winequality.csv
```
Add the data to github repository
```bash
git add . && git commit -m "Adding Data to github"
git remote add origin https://github.com/VinodKumarJodu/MLOps.git
git branch -M main
git push origin main
```
