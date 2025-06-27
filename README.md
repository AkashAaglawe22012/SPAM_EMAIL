# 📧 Spam Email Detection

This project demonstrates how to classify emails as **spam** or **ham (not spam)** using Natural Language Processing (NLP), machine learning (ML), and deep learning (DNN). It includes data exploration, text preprocessing with NLTK, model building, evaluation, and performance comparison.

---

## 📂 Project Structure

* **Data Reading & Inspection**: Load CSV data, check structure and null values.
* **Visualization**: Includes pie chart, histogram, and heatmap to understand class distribution and feature relationships.
* **Text Preprocessing**: Clean email text using NLTK — lowercase, tokenization, stopword removal, punctuation stripping.
* **Modeling**:

  * **Machine Learning**: Logistic Regression, XGBoost, K-Nearest Neighbors (KNN)
  * **Deep Learning**: Artificial Neural Network (ANN)
* **Evaluation**:

  * Confusion Matrix
  * Classification Report (precision, recall, F1-score)
  * Accuracy Comparison

---

## 🛠 Technologies Used

* **Python 3.11**
* **Pandas, NumPy** – data manipulation
* **Matplotlib, Seaborn** – visualizations
* **NLTK** – text preprocessing
* **Scikit-learn** – ML models and evaluation
* **XGBoost** – gradient boosting model
* **Keras / TensorFlow** – ANN implementation

---

## 📈 Key Findings

* Logistic Regression and XGBoost delivered the **highest accuracy and F1-score**.
* ANN performed reasonably well but required more tuning and computational power.
* Preprocessing significantly improved model performance.

---

## 📊 Example Visualizations

* 📌 Pie Chart: Spam vs Ham distribution
* 📏 Histogram: Text length distribution
* 🌡️ Heatmap: Feature correlation

---

## 🚀 How to Run

1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run the notebook or script
4. Run = python app.py








Feel free to contribute or raise issues. Spam detection saves inboxes! 📬
