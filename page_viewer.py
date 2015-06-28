from flask import render_template
import math

def main(db, book_id, page_id):
    try:
      prev_url = '/page/' + str(book_id) + '/' + str(max(int(page_id)-1, 0))
      next_url = '/page/' + str(book_id) + '/' + str(int(page_id)+1)
      print book_id
      print page_id
      url = db.pages.find_one({'book_id': str(book_id), 'page': int(page_id)})['url']
      return render_template('page_viewer.html', page_title="Test Page Viewer", url=url, prev_url=prev_url, next_url=next_url)
    except Exception as e:
      print e
