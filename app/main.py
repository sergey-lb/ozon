import os

import waitress
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from app.lib import create_book, add_book, search_books, search_book_by_id, create_empty_book, update_book, \
    remove_book_by_id, generate_empty_id


def start():
    app = Flask(__name__)

    library = []

    war_and_piece = create_book(
        'Война и мир',
        'Толстой',
        1000,
        True,
        'война, любовь, толстой'
    )

    anna_karenina = create_book(
        'Анна Каренина',
        'Толстой',
        500,
        False,
        'поезд, любовь, толстой'
    )

    pushkin = create_book(
        'Собрание сочинений',
        'Пушкин',
        500,
        True,
        'пушкин, сказки, стихи'
    )

    library = add_book(library, war_and_piece)
    library = add_book(library, anna_karenina)
    library = add_book(library, pushkin)

    @app.route('/')
    def index():
        empty_id = generate_empty_id()
        search = request.args.get('search')
        if search:
            results = search_books(library, search)
            return render_template('index.html', books=results, search=search, empty_id=empty_id)

        return render_template('index.html', books=library, empty_id=empty_id)

    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(library, book_id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<book_id>/edit')
    def book_edit(book_id):
        book = None
        empty_id = str(generate_empty_id())
        if book_id == empty_id:
            book = create_empty_book()
        else:
            book = search_book_by_id(library, book_id)
        return render_template('book-edit.html', book=book)

    @app.route('/books/<book_id>/save', methods=['POST'])
    def book_save(book_id):
        nonlocal library

        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        available = bool(int(request.form['available']))
        tags = request.form['tags']

        empty_id = str(generate_empty_id())
        if book_id == empty_id:
            book = create_book(title=title, author=author, price=price, available=available, tags_str=tags)
            library = add_book(library, book)
        else:
            book = search_book_by_id(library, book_id)
            update_book(book, title=title, author=author, price=price, available=available, tags_str=tags)

        return redirect(url_for('book_details', book_id=book['id']))

    @app.route('/books/<book_id>/remove', methods=['POST'])
    def book_remove(book_id):
        nonlocal library
        library = remove_book_by_id(library, book_id)
        return redirect(url_for('index'))

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
