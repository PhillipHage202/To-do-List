from flask import render_template
from application.models import Todo

@app.route('/add')
def add ():
    new_todo= Todo(To_do= 'New To'
    db.session.add (new_todo)
    db.session.commit ()
    return "Added new To do"

@app.route('/update/<name>')
def update (name):

