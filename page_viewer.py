from flask import render_template

def main(pageId):
    try:
      return render_template('page_viewer.html', page_title="Test Page Viewer")
    except Exception as e:
      print e
