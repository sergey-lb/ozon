from app.lib import create_book, add_book, search_books, list_books


def test_create_book():
    # A -> Arrange
    data = {
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'available': True,
        'tags': 'война, любовь, толстой'
    }

    expected = {
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'available': True,
        'tags': {'война', 'любовь', 'толстой'}
    }

    # A -> Act
    result = create_book(data['title'], data['author'], data['price'], data['available'], data['tags'])

    # A -> Assert
    assert expected == result


def test_add_one_book_to_empty_library():
    library = []
    book = create_book(
        'Война и мир',
        'Толстой',
        1000,
        True,
        'война, любовь, толстой'
    )

    add_book(library, book)

    assert len(library) == 1
    assert book in library


def test_search_books_by_title():
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

    add_book(library, war_and_piece)
    add_book(library, anna_karenina)

    expected = [anna_karenina]

    result = search_books(library, 'каре')

    assert result == expected


def test_search_books_by_author():
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

    expected = [war_and_piece, anna_karenina]

    result = search_books(library, 'толстой')

    assert result == expected


def test_search_books_by_tag():
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

    expected = [war_and_piece, anna_karenina]

    result = search_books(library, '#любовь')

    assert result == expected


def test_list_books():
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

    expected1 = [war_and_piece, anna_karenina]
    expected2 = [pushkin]

    result1 = list_books(library, 1, 2)
    result2 = list_books(library, 2, 2)

    assert result1 == expected1
    assert result2 == expected2
