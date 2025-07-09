# ML Network Intrusion Detector

> A machine learning-based system trained to classify network connections as **normal** or **malicious**, helping to detect potential intrusions.

---

## Project Goal

Develop and evaluate supervised learning models for **predictive classification** in network intrusion detection.

---

## Dataset

* **Source:** Public dataset from [Kaggle](https://www.kaggle.com/)
* **Preprocessing:**

  * Applied **OneHotEncoding** on 3 categorical columns
  * Applied **StandardScaler** on 3 numerical columns

---

##  Tech Stack

* **Languages/Libraries:** Python, NumPy, Pandas, Seaborn, Matplotlib, Scikit-Learn
* **Deployment:** Docker (build and run from Dockerfile)

---

## ML Models

Three classification models were trained and compared:

* `LogisticRegression`
* `SVC` (Support Vector Classifier)
* `DecisionTreeClassifier`

---

## Evaluation Metrics

Models were evaluated based on:

* **Precision**
* **Recall**
* **F1-Score** (Primary)
* **ROC-AUC Curve**

---

## How to Run

Make sure you have Docker installed. Then run:

```bash
# Step 1: Build Docker image
sudo docker build --tag main-server-image .

# Step 2: Run the container
sudo docker run -p 8080:8080 main-server-image
```

> The project structure is locked and **should not be modified**.

---

## 📌 Notes

* This project serves as a foundational component for future AI-based cybersecurity tools.
* Feel free to reuse the preprocessing logic or evaluation strategies for other network security datasets.
