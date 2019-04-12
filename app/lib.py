import uuid


def create_book(title, author, price, available, tags_str):

    tags = convert_tags_from_str_to_set(tags_str)

    return {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'price': price,
        'available': available,
        'tags': tags
    }


def convert_tags_from_str_to_set(tags_str):
    if not tags_str:
        return set()

    tags = set(map(str.strip, tags_str.split(',')))
    return tags


def generate_empty_id():
    return uuid.UUID(int=0)


def create_empty_book():
    return {
        'id': generate_empty_id(),
        'title': '',
        'author': '',
        'price': 0,
        'available': True,
        'tags': set()
    }


def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def update_book(book, title, author, price, available, tags_str):

    tags = convert_tags_from_str_to_set(tags_str)

    book['title'] = title
    book['author'] = author
    book['price'] = price
    book['available'] = available
    book['tags'] = tags


def list_books(container, page, page_size):
    # page_size = 50
    start = (page - 1) * page_size  # для первой страницы стартуем с 0
    finish = start + page_size
    return container[start:finish]


def search_books(container, search):  # search - строка поиска
    if search[0] == '#':
        search_tag = search[1:]
        return search_books_by_tag(container, search_tag)

    search_lowercased = search.strip().lower()  # 1. search.strip() 2. (результат search.strip()).lower()
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue  # не даёт идти дальше на 30 строку

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue  # пока не нужно, но на будущее пригодиться, если будем добавлять новые возможности

    return result


def search_books_by_tag(container, search_tag):
    search_tag_lowercased = search_tag.strip().lower()
    result = []
    for book in container:
        book_tags_lowercased = map(str.lower, book['tags'])
        if search_tag_lowercased in book_tags_lowercased:
            result.append(book)

    return result


def search_book_by_id(container, book_id):
    for book in container:
        if book['id'] == book_id:
            return book


def remove_book_by_id(container, book_id):
    result = []
    for book in container:
        if book['id'] != book_id:
            result.append(book)
    return result
