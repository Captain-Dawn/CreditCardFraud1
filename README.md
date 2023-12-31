# End to end CreditCardFraud1 Detection Project

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src/config
5. Update the components in src/components
6. Update the pipline
7. Update the main.py
8. Update the app.py ### at the end


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/tejas05in/CreditCardFraud1.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p env python=3.8 -y
```

```bash
conda activate env/
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow & Dagshub

Integrated but diabled by default


<!-- ## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui -->

<!-- ### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/tejas05in/CreditCardFraud1.mlflow \
MLFLOW_TRACKING_USERNAME=tejas05in \
MLFLOW_TRACKING_PASSWORD=9efcb5c7b79d0e949378459b922b1462a80fa413 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/tejas05in/CreditCardFraud1.mlflow

export MLFLOW_TRACKING_USERNAME=tejas05in 

export MLFLOW_TRACKING_PASSWORD=9efcb5c7b79d0e949378459b922b1462a80fa413

``` -->

### Dockerhub
#### Dokcer Image can be downloaded using:
```bash
docker pull tejas05in/ccfdapp
```
