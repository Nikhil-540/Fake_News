from flask import Flask, render_template, request
from model import classify_article_with_model  # Import your model function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        article_text = request.form["article_text"]
        result = classify_article_with_model(article_text)
        return render_template("result.html", result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
