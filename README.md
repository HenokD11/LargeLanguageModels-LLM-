# Large Language Models - LLM
# About

A client has a system that collects news artifacts from web pages, tweets, facebook posts, etc. The client is interested in scoring a given new artifact against a topic. 

The client needs the news items to get scored in the range from 0 to 10; a score of 0 means the news item is totally NOT relevant while a score of 10 means the news item is very relevant. 

The range of results between 0 and 10 signifies the  degree of relevance of the news item to the topic. 

The task is to prompt engineer GPT3-like LLMs for downstream task like news scoring and named entity extraction.

# Objective 

Prompt engineer Large Language Models for news scoring and Named Entity Extraction

# Data

The data used for this project can be found [News scoring](https://docs.google.com/spreadsheets/d/19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J/edit#gid=293715615) and [named_entity](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt)

# Repository overview
Structure of the repository -

    ├── models  (contains trained model)
    ├── .github  (github workflows for CI/CD, CML)
    ├── screenshots  (Important screenshots)
    ├── mlruns  (contains MLflow runs)
    ├── train (contains training scripts) 
    ├── assets  (contains assets)
    ├── data    (contains data of train, store, and test)
    ├── scripts (contains the main script)	
    │   ├── logger.py (logger for the project)
    overview)
    │   ├── plot.py (handles plots)
    │   ├── preprocess.py (Data preprocessing)
    ├── notebooks	
    |   ├── api_connection.ipynb(setting up api connection with CO:here)
    │   ├── eda.ipynb (overview of the Data)
    │   ├── preprocess.ipynb (Preparing the data)
    │   ├── model.ipynb (LLM model)
    ├── tests 
    │   ├── test_preprocess.py (test for the the preprocess testing script)
    ├── README.md (contains the project description)
    ├── requirements.txt (contains the required packages)
    |── LICENSE (license of the project)
    ├── setup.py (contains the setup of the project)
    └── .dvc (contains the dvc configuration)

# Requirements

The project requires the following: python3 Pip3

# Usage

Local Development

1. Activate environement or create one:

```conda create -n <env-name> && conda activate <env-name>```

2. Install required packages

```pip install -r requirements.txt```

3. Run the app

```python3 wsgi.py```

# Contributers

```Henok Desalegn```

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.