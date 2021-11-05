from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/scrape_mars")


@app.route("/")
def index():
    marsData = mongo.db.collection.find_one()
    return render_template("index.html", marsData = marsData)


@app.route("/scrape")
def scraper():
    marsInfo = mars_scrape.scrape_info

    mongo.db.collection.update({}, marsInfo, upsert=true)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
