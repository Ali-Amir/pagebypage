from flask import render_template

def main(db):
  thumbnails = render_thumbnails(db)
  return render_template('index.html', thumbnails = thumbnails)

def render_thumbnails(db):
  thumb_templ = '<tr>'
  results = db.books.find({})
  cnt = 0
  for result in results:
    thumbnail_url = db.pages.find_one({'book_id': result['book_id'], 'page': 0})['url']
    cnt += 1
    if cnt == 8:
      cnt = 1
      thumb_templ += '</tr><tr><td><a href="?book=' + \
                     result['book_id'] + \
                     ',page=1"><div class="thumbnail-image" style="background:url(\'' + \
                     thumbnail_url + \
                     '\');background-size:contain"></div></a><p>' + \
                     result['title']+'</p></td>'
    else:
      thumb_templ += '<td><a href="?book='+result['book_id'] + \
                     ',page=1"><div class="thumbnail-image" style="background:url(\'' + \
                     thumbnail_url + '\');background-size:contain"></div></a><p>'+result['title']+'</p></td>'
  thumb_templ += '</tr>'
  return thumb_templ
