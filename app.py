from flask import Flask, request, url_for, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection configuration
client = MongoClient("mongodb://root:3yGWpZ7jeS@34.78.116.136:27017/")
db = client["profile-app"]
url_collection = db["default"]

@app.route("/", methods=["GET"])
def index():
    urls = list(url_collection.find())
    return render_template("index.html", urls=urls)


@app.route("/submit", methods=["POST"])
def add_url():
    url = request.form["url"]
    title = request.form.get("title")  # Get the title, if provided
    description = request.form.get("description")  # Get the description, if provided

    # Create a dictionary for the URL document
    url_doc = {
            "url": url,
            "title": title,
            "description": description
        }

    url_collection.insert_one(url_doc)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port="6544")
