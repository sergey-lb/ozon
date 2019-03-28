from app.lib import create_book, add_book, search_books, list_books, generate_empty_id, create_empty_book, update_book, \
    search_book_by_id, remove_book_by_id


def test_generate_empty_id():
    expected = '00000000-0000-4000-8000-000000000000'
    result = str(generate_empty_id())

    assert expected == result


def test_create_empty_book():
    expected = {
        'id': generate_empty_id(),
        'title': '',
        'author': '',
        'price': 0,
        'available': True,
        'tags': set()
    }

    result = create_empty_book()

    assert expected == result


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

    data_with_empty_tags = {
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'available': True,
        'tags_str': ''
    }

    expected_for_data_with_empty_tags = {
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'available': True,
        'tags': set()
    }

    # A -> Act
    result = create_book(data['title'], data['author'], data['price'], data['available'], data['tags'])
    del result['id']

    result_with_empty_tags = create_book(**data_with_empty_tags)
    del result_with_empty_tags['id']

    # A -> Assert
    assert result == expected
    assert result_with_empty_tags == expected_for_data_with_empty_tags


def test_update_book():

    data = {
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'available': True,
        'tags_str': 'война, любовь, толстой'
    }

    expected = {
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'available': True,
        'tags': {'война', 'любовь', 'толстой'}
    }

    book = create_empty_book()
    update_book(book, **data)

    del book['id']

    assert book == expected


def test_remove_book_by_id():
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

    expected = library[:]
    del expected[1]

    result = remove_book_by_id(library, anna_karenina['id'])

    assert result == expected


def test_add_one_book_to_empty_library():
    library = []
    book = create_book(
        'Война и мир',
        'Толстой',
        1000,
        True,
        'война, любовь, толстой'
    )

    library = add_book(library, book)

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

    library = add_book(library, war_and_piece)
    library = add_book(library, anna_karenina)

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

    library = add_book(library, war_and_piece)
    library = add_book(library, anna_karenina)
    library = add_book(library, pushkin)

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

    library = add_book(library, war_and_piece)
    library = add_book(library, anna_karenina)
    library = add_book(library, pushkin)

    expected = [war_and_piece, anna_karenina]

    result = search_books(library, '#любовь')

    assert result == expected


def test_search_book_by_id():
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

    library = add_book(library, war_and_piece)
    library = add_book(library, anna_karenina)

    expected = anna_karenina

    result = search_book_by_id(library, anna_karenina['id'])

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

    library = add_book(library, war_and_piece)
    library = add_book(library, anna_karenina)
    library = add_book(library, pushkin)

    expected_on_first_page = [war_and_piece, anna_karenina]
    expected_on_second_page = [pushkin]

    first_page_result = list_books(library, 1, 2)
    second_page_result = list_books(library, 2, 2)

    assert first_page_result == expected_on_first_page
    assert second_page_result == expected_on_second_page
