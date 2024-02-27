from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# configuration for the "todo" table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    # date = db.Column(db.DateTime, nullable=False)

