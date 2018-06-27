from flask import Flask, request, redirect, render_template
from DB import *

app = Flask(__name__)


@app.route('/')
def index():
    db = DB()
    users = db.get_all('users')
    return render_template('index.html', users=users)


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/store')
def store():
    db = DB()
    data = {'name': request.args.get('name'), 'email': request.args.get('email')}
    db.store('users', data)
    return redirect('/')


@app.route('/edit/<id>')
def edit(id):
    db = DB()
    user = db.find('users', id)
    return render_template('update.html', user=user)


@app.route('/update')
def update():
    id = request.args.get("id")
    data = {'name': request.args.get('name'), 'email': request.args.get('email')}
    db = DB()
    db.update('users', id, data)
    return redirect('/')


@app.route('/remove')
def remove():
    db = DB()
    db.remove('users', request.args.get('id'))
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
