from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("xg.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.is_json:
        # API request
        data = request.get_json()
        input_text = data.get("text", "")
    else:
        # HTML form request
        input_text = request.form["text"]

    transformed = vectorizer.transform([input_text])
    prediction = model.predict(transformed)[0]
    result = "spam" if prediction == 1 else "not spam"

    if request.is_json:
        return jsonify({"prediction": result})
    else:
        return render_template("index.html", input_text=input_text, prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
