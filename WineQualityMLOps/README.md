Steps:

Create new Conda Environment
```bash
conda create -n WneQuality python=3.7 -y
```
Activate the Environment WIneQuality
```bash
conda activate WineQuaality
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