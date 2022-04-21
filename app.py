import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db, render_as_batch=True)

book_genres = db.Table(
    "book_genres",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id")),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id")),
)

book_authors = db.Table(
    "book_authors",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id")),
    db.Column("author_id", db.Integer, db.ForeignKey("authors.id")),
)


class Book(db.Model):

    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    total_pages = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    isbn = db.Column(db.String(13), nullable=True)
    published = db.Column(db.Date, nullable=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    authors = db.relationship("Author", secondary=book_authors, backref="books")
    genres = db.relationship("Genre", secondary=book_genres, backref="books")

    def __init__(self, title, total_pages, rating, isbn, published, publisher_id):
        self.title = title
        self.total_pages = total_pages
        self.rating = rating
        self.isbn = isbn
        self.published = published
        self.publisher_id = publisher_id

    def __repr__(self):
        return f"{self.title}"


class Publisher(db.Model):
    __tablename__ = "publishers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    books = db.relationship("Book", backref="publisher")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=True)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(255), nullable=False)

    def __init__(self, genre):
        self.genre = genre

    def __repr__(self):
        return f"{self.genre}"
