from flask import render_template

from antiques import app, route


@route(app, ['/', '/index'])
def index():
    print 'a'
    return render_template('home/index.html', title='Market')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Sorry!"), 404
