from flask import Flask, redirect, url_for, render_template, request

from spamModel.spam_detector import SpamDetector

app = Flask(__name__)

spam_detector = SpamDetector()

@app.route("/")                                         #Home page routing
def home():
    return render_template("index.html")

@app.route('/response', methods=['GET', 'POST'])
def response():
    if request.method == 'POST':
        prediction = spam_detector.predict([request.form.get("test")])      #request.form.get gives a string, need to change to list with brackets to use the function
        return render_template("index.html", name=prediction[0])            # brackets indicate the first element
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)         #Allows server to not have to be rerun after every change becasue is automatically detecting the changes