#import dependancies
from flask import Flask, render_template, redirect
import pymongo
from scrape_mars import scrape

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries

@app.route("/")
def home():
    mars_data = dict(collection.find_one())
    # print(mars_data)
    return render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def web_scrape():
    # collection.drop({})
    mars_data = scrape()
    collection.insert_one(mars_data)
    # return  render_template('index.html')
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)