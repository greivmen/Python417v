from flask import Flask, render_template, request, flash, g, abort
import os
import sqlite3
from fdatabase import FDataMenu

DATABASE = 'menu.db'
DEBUG = True
SECRET_KEY = 'defbba5cf05fa076684cf46d6f14b4dcb5160714'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'menu.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('mn_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataMenu(db)
    return render_template('index.html', menu=dbase.get_menu(), posts=dbase.get_posts_annonce())


@app.route('/add_post', methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataMenu(db)
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'])
            if not res:
                flash("Ошибка добавления игры", category="error")
            else:
                flash("Игра добавлена успешна ", category="success")
        else:
            flash("Ошибка добавления игры", category="error")
    return render_template('add_post.html', title="Добавление игры", menu=dbase.get_menu())


@app.route("/add_post2", methods=["POST", "GET"])
def add_post2():
    db = get_db()
    dbase = FDataMenu(db)
    return render_template('add_post2.html', title="Ожидание релиза:", menu=dbase.get_menu())


@app.route("/add_post3", methods=["POST", "GET"])
def add_post3():
    db = get_db()
    dbase = FDataMenu(db)
    return render_template('add_post3.html', title="О жизни:", menu=dbase.get_menu())


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDataMenu(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)
    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataMenu(db)
    return render_template('page404.html', title="Страница не наедена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()
