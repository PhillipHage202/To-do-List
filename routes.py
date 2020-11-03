from flask import render_template , redirect, url_for
from application import db, app
from application.models import Todo

@app.route('/')
def index ():
    all_todos = Todo.query.all()
    return render_template ('index.html', all_todos=all_todos

@app.route ('/add')
def add():
    new_todo = Todo(To_do='New Todo')
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for ('index') )

@app.route ('/complete/<int:todo_id>')
def complete (todo_id)
    todo_update = To_do.query.get (todo_id)
    todo_update.complete = True
    db.session.commit ()
    return redirect (url_for ('index')

@app.route ('/update/<task>')
def update (task):
    todo_update = To_do.query.first()
    todo_update.task = task
    db.session.commit()
    return redirect (url_for ('index')

@app.route ('/delete')
def delete ():
    todo_delete = To_do.query.first()
    db.session.delete(todo_delete)
    db.session.commit()
    return redirect (url_for ('index')
