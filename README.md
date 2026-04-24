# Crop Recommendation System

**Live Demo:** [click here](https://crop-recommendation-ml-yf8y.onrender.com)

---

## Overview

This project builds a machine learning model to recommend the most suitable crop based on soil nutrients and environmental conditions. The model is deployed using Flask to provide real-time predictions through a simple web interface.

---

## Dataset

* Source: [kaggle dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset/data)

The dataset contains:

* Soil nutrients: Nitrogen (N), Phosphorus (P), Potassium (K)
* Environmental factors: temperature, humidity, pH, rainfall
* Target: crop label

---

## Approach

* Data preprocessing using a pipeline (scaling + model)
* Model comparison:
  * Logistic Regression
  * Decision Tree
  * Random Forest
* Random Forest selected based on highest performance and stability
* Model and label encoder exported for deployment

---

## Features

* Input-based crop prediction
* Real-time inference using Flask
* End-to-end pipeline from training to deployment

---

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Flask

---

## Run Locally

```bash
git clone https://github.com/Roushan-77/crop-recommendation-ml.git
cd crop-recommendation-ml

pip install -r requirements.txt
python main.py
```
