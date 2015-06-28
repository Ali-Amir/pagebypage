from flask import Flask, send_from_directory
from pymongo import MongoClient
import main_page
import page_viewer

# default to http://localhost:27017
client = MongoClient()
db = client.database
books = db.books
pages = db.pages

app = Flask(__name__)

@app.route("/")
def main():
    return main_page.main()

@app.route("/<path:path>")
def send_css(path):
    if path[-3:] == 'css':
        return send_from_directory('css', path)
    if path[-3:] == 'jpg' or path[-3:] == 'png':
        print "stuff"
        return send_from_directory('', path)
    print path
    return send_from_directory('fonts', path)

@app.route("/page?pageId=<pageId>")
def getPage(pageId):
  print "runnning"
  return page_viewer.main(pageId)

if __name__ == "__main__":
	app.run()
