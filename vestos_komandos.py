from app import db, Book, Publisher, Author, Genre
from datetime import date

pub1 = Publisher("Baltos Lankos")

pub2 = Publisher("Alma Littera")

pub3 = Publisher("Margi raštai")

book1 = Book("Kliudžiau", 200, 3.79, "9789986094814", date(2018, 1, 1), 3)

genre1 = Genre("Apysaka")

genre2 = Genre("Apsakymai")

author1 = Author("Jonas", "Biliūnas")

db.session.add_all([pub1, pub2, pub3, genre1, genre2, author1, book1])

db.session.commit()

book = Book.query.get(1)
book

author = Author.query.get(1)
author

genres = Genre.query.all()
genres

book.authors.append(author)
book.authors

for genre in genres:
    book.genres.append(genre)

book.genres
