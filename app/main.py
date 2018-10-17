from app import app
import view
from app import db
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix = '/blog')

if '__main__' == __name__:
    app.run()