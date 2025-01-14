def check_args(item: str, value: str):
    text = ''
    if value == 'author':
        author = item
        if not author:
            text = 'Ничего нет 😕\n' \
                   'Попробуй так:\n' \
                   '/author <i>ФИО автора</i>'
        elif len(author) <= 2:
            text = '❗Слишком короткий запрос. Попробуй еще раз❗'

    elif value == 'book':
        if len(item) <= 2:
            text = '❗Слишком короткое название, попробуй еще раз❗'

    elif value == 'series':
        series = item
        if not series:
            text = 'Ничего нет 😕\n' \
                   'Попробуй так:\n' \
                   '/series <i>название книжной серии</i>'
        elif len(series) <= 2:
            text = '❗Слишком короткое название, попробуй еще раз❗'

    return text
