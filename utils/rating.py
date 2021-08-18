
def page_rating(rating_dict: dict):
    # обработка страницы с рейтингом
    rating_lst = []
    i = 0
    if not rating_dict:
        return f'На данный момент рейтинг пуст'
    for key, item in rating_dict.items():
        book, downloaded = item
        link = key
        if i == 0:
            text = f'🏆  <b>ТОП 10 КНИГ по скачиванию</b>  🏆\n\n\n' \
                   f'🥇 <b>{book}</b>\n' \
                   f'Описание: /{link}\n\n'
            rating_lst.append(text)
        elif i == 1:
            text = f'🥈 <b>{book}</b>\n' \
                   f'Описание: /{link}\n\n'
            rating_lst.append(text)
        elif i == 2:
            text = f'🥉 <b>{book}</b>\n' \
                   f'Описание: /{link}\n\n'
            rating_lst.append(text)
        elif i > 2:
            text = f'📕<b>{book}</b>\n' \
                   f'Описание: /{link}\n\n'
            rating_lst.append(text)
        i += 1
    return ' '.join(rating_lst)