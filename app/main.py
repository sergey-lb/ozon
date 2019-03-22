import os
import waitress
from flask import Flask, render_template, request

from app.lib import create_book, add_book, search_books


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

    add_book(library, war_and_piece)
    add_book(library, anna_karenina)
    add_book(library, pushkin)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            results = search_books(library, search)
            return render_template('index.html', books=results, search=search)

        return render_template('index.html', books=library)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
