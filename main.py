from flask import Flask, send_from_directory
from pymongo import MongoClient

# default to http://localhost:27017
client = MongoClient()
db = client.database
books = db.books
pages = db.pages

app = Flask(__name__)

import main_page

@app.route("/")
def main():
    return main_page.main()

@app.route("/<path:path>")
def send_css(path):
    return send_from_directory('css', path)

if __name__ == "__main__":
	app.run()
