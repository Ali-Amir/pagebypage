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
    if path[-3:] == 'css':
        return send_from_directory('css', path)
    print path
    return send_from_directory('fonts', path)

def setup_db():
	if books.count() == 0:
		book = {'author': 'Ernest Hemingway', 'title':'The Old Man and the Sea'}
		books.insert_one(book)
	if pages.count() == 0:
		page_1 = {'book_id': '558fbdd7207d5be0f4f1c621',
				  'url':'https://drive.google.com/file/d/0ByVj29dKGJcAcFk3Y0V6bFAyNWc/view?usp=sharing',
				  'num_copies': 1}
		page_2 = {'book_id': '558fbdd7207d5be0f4f1c621',
				  'url': 'https://drive.google.com/file/d/0ByVj29dKGJcAaFdrbEc3VlkzR0U/view?usp=sharing',
				  'num_copies': 1}
		page_3 = {'book_id': '558fbdd7207d5be0f4f1c621',
				  'url': 'https://drive.google.com/file/d/0ByVj29dKGJcAdFc0WG1PcExHeFU/view?usp=sharing',
				  'num_copies': 1}
		page_4 = {'book_id': '558fbdd7207d5be0f4f1c621',
				  'url': 'https://drive.google.com/file/d/0ByVj29dKGJcAU3pXbXBLa2VfQ28/view?usp=sharing',
				  'num_copies': 1}
		pages.insert_many([page_1, page_2, page_3, page_4])

if __name__ == "__main__":
	setup_db()
	app.run()
