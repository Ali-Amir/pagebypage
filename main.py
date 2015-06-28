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
    return main_page.main(db)

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

def setup_db():
    books.drop()
    pages.drop()
    if books.count() == 0:
        book = []
        book.append({'author': 'Ernest Hemingway', 'title':'The Old Man and the Sea', 'book_id': '558fbdd7207d5be0f4f1c621'})
        book.append({'author': 'Ernest Hemingway', 'title':'A Beautiful Mind', 'book_id': '1'})
        book.append({'author': 'Ernest Hemingway', 'title':'Tom Sawyer', 'book_id': '2'})
        book.append({'author': 'Ernest Hemingway', 'title':'Ender''s Game', 'book_id': '3'})
        book.append({'author': 'Ernest Hemingway', 'title':'The Hitchhiker''s Guid to the Galaxy', 'book_id': '4'})
        book.append({'author': 'Ernest Hemingway', 'title':'The Master and Margarita', 'book_id': '5'})
        book.append({'author': 'Ernest Hemingway', 'title':'The Lean Startup', 'book_id': '6'})
        book.append({'author': 'Ernest Hemingway', 'title':'Beginning Programming for Dummies', 'book_id': '7'})
        book.append({'author': 'Ernest Hemingway', 'title':'A Game of Thrones', 'book_id': '8'})
        book.append({'author': 'Ernest Hemingway', 'title':'Pride and Prejudice', 'book_id': '9'})
        book.append({'author': 'Ernest Hemingway', 'title':'Harry Potter and the Sorcerer\'s Stone', 'book_id': '10'})
        book.append({'author': 'Ernest Hemingway', 'title':'Introduction to Algorithms', 'book_id': '11'})
        book.append({'author': 'Ernest Hemingway', 'title':'Cracking the Coding Interview', 'book_id': '12'})
        book.append({'author': 'Ernest Hemingway', 'title':'Fifty Shades of Grey', 'book_id': '13'})
        books.insert_many(book)

    if pages.count() == 0:
        thum_0 = {'book_id': '558fbdd7207d5be0f4f1c621', 'page': 0,
                    'url':'images/558fbdd7207d5be0f4f1c621_0.jpg',
                    'num_copies': 1}
        page_1 = {'book_id': '558fbdd7207d5be0f4f1c621', 'page': 1,
                    'url':'https://raw.githubusercontent.com/Ali-Amir/pagebypage/master/books/558fbdd7207d5be0f4f1c621_1.jpg',
                    'num_copies': 1}
        page_2 = {'book_id': '558fbdd7207d5be0f4f1c621', 'page': 2,
                    'url': 'https://raw.githubusercontent.com/Ali-Amir/pagebypage/master/books/558fbdd7207d5be0f4f1c621_2.jpg',
                    'num_copies': 1}
        page_3 = {'book_id': '558fbdd7207d5be0f4f1c621', 'page': 3,
                    'url': 'https://raw.githubusercontent.com/Ali-Amir/pagebypage/master/books/558fbdd7207d5be0f4f1c621_3.jpg',
                    'num_copies': 1}
        page_4 = {'book_id': '558fbdd7207d5be0f4f1c621', 'page': 4,
                    'url': 'https://raw.githubusercontent.com/Ali-Amir/pagebypage/master/books/558fbdd7207d5be0f4f1c621_4.jpg',
                    'num_copies': 1}
        pgs = [thum_0, page_1, page_2, page_3, page_4]
        for idx in range(1, 14):
            thum = {'book_id': '%d'%idx, 'page': 0,
                    'url':'images/%d_0.jpg'%idx,
                    'num_copies': 1}
            pgs.append(thum)
        pages.insert_many(pgs)

if __name__ == "__main__":
	setup_db()
	app.run(debug=True)
