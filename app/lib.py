def create_book(title, author, price, availability, tags_str):

    tags = set(map(str.strip, tags_str.split(',')))

    return {
        'title': title,
        'author': author,
        'price': price,
        'available': availability,
        'tags': tags
    }


def add_book(container, book):  # не чистая функция
    container.append(book)
    # return container # TODO: вернуться к этому вопросу позже


def list_books(container, page, page_size):
    # page_size = 50
    start = (page - 1) * page_size  # для первой страницы стартуем с 0
    finish = start + page_size
    return container[start:finish]


def search_books(container, search):  # search - строка поиска
    if search[:1] == '#':
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
