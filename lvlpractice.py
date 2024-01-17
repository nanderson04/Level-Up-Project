from flask import Flask, redirect, url_for, render_template, request

from spamModel.spam_detector import SpamDetector

app = Flask(__name__)

spam_detector = SpamDetector()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/response', methods=['GET', 'POST'])
def response():
    if request.method == 'POST':
        fname = spam_detector.predict(request.form.get("fname"))
        return render_template("index.html", name=fname)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)         #Allows server to not have to be rerun after every change becasue is automatically detecting the changes