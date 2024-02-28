import os
from flask import Flask, render_template, url_for, redirect, request
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
    todo_form, new_todo = add_to_do()

    if request.method == "POST":
        return redirect(url_for('home'))
    return render_template('index.html', all_todos=todos, todo_form=todo_form)


def add_to_do() -> (AddTodoForm, Todo):
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
    active_task = db.session.execute(db.select(Todo).where(Todo.done == False)).scalars().all()
    print("task: ", active_task)
    todo_form, new_todo = add_to_do()
    return render_template('index.html', all_todos=active_task, todo_form=todo_form)

@app.route("/completed", methods=["GET", "POST"])
def get_completed_task():
    completed_task = db.session.execute(db.select(Todo).where(Todo.done == True)).scalars().all()
    print("task: ", completed_task)
    todo_form, new_todo = add_to_do()
    return render_template('index.html', all_todos=completed_task, todo_form=todo_form)

@app.route("/update", methods=["POST"])
def update_task():
    # Get the ID from the request body
    request_data = request.get_json()
    id = request_data.get('id')

    task_to_update = db.session.execute(db.select(Todo).where(Todo.id == id)).scalar()
    print("done? ", task_to_update.done)
    task_to_update.done = not task_to_update.done
    print("and now? ", task_to_update.done)
    db.session.commit()

    #return ok status as json
    return {"status": "ok"}


@app.route("/delete/<int:task_id>", methods=["GET"])
def delete_todo(task_id):
    # Get the ID from the request body
    print(task_id)
    task_to_delete = db.get_or_404(Todo, task_id)
    print("task to delete ", task_to_delete.name)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
