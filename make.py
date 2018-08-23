from flask import Flask, render_template
import os
from build.libs.post import Post

POST_FILE_EXTENSTION = '.md'

app = Flask('__name__')

@app.route('/')
def index():
    return "Hello!"

@app.route('/blog/<path:path>')
def post(path):
    path = os.path.join('posts', path + POST_FILE_EXTENSTION)
    this_post = Post(path)
    return render_template('post.html',post = this_post)


if __name__ == '__main__':
    app.run(port=2700, debug = True)