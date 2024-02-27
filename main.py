import os
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_bootstrap import Bootstrap5

from forms import AddTodoForm
from todo import Todo, db

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
db.init_app(app)

todo = Todo()

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    result = db.session.execute(db.select(Todo))
    todos = result.scalars().all()
    # print(todo_form.validate_on_submit(), todo_form.todo.data)
    todo_form, new_todo = add()

    if request.method == "POST":
        return redirect(url_for('home'))
    return render_template('index.html', all_todos=todos, todo_form=todo_form)


def add() -> (AddTodoForm, Todo):
    todo_form = AddTodoForm()
    new_todo = None
    if todo_form.validate_on_submit():
        new_todo = Todo(name=todo_form.todo.data, done=False)
        db.session.add(new_todo)
        db.session.commit()
        print(new_todo)
    return todo_form, new_todo


@app.route("/active", methods=["GET", "POST"])
def get_active_task():
    active_task = db.session.execute(db.select(Todo).where(not Todo.done)).scalar()
    print("task: ", active_task)
    todo_form, new_todo = add()
    return render_template('index.html', all_todos=active_task, todo_form=todo_form)


def get_completed_task():
    pass


if __name__ == "__main__":
    app.run(debug=True)
