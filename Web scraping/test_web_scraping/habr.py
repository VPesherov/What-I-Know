'div class="tm-articles-list"'
"article"
"""
<h2 class="tm-title tm-title_h2"><a href="/ru/companies/beeline_cloud/articles/751712/" class="tm-title__link" data-test-id="article-snippet-title-link" data-article-link="true"><span>На пороге «нейрозимы» и глобального кризиса — что разработчики систем ИИ думают о будущем технологии</span></a></h2>
"""

"""
<time datetime="2023-08-01T16:29:40.000Z" title="2023-08-01, 19:29">29 минут назад</time>
"""

"""
div id="post-content-body"
"""


import requests
# данная библиотека подкинет в наши данные что мы не бот а что мы пользователь
import fake_headers
from bs4 import BeautifulSoup
from pprint import pprint

# генерируем информацию - что мы пользователь и зашли с браузера firefox и ОС - винда
headers_gen = fake_headers.Headers(browser='firefox', os='win')

# делаем запрос к сайт и подкидываем ему в заголовках - что мы человек
response = requests.get('https://habr.com/ru/all/', headers=headers_gen.generate())
# также получаем наш html
html_data = response.text

'''
Тэг со всеми нашими статьями
div class="tm-articles-list"
'''

habr_main = BeautifulSoup(html_data, 'lxml')

# все наши статьи
article_list_tag = habr_main.find(name='div', class_='tm-articles-list')

# каждая статья помечена тэгом article -> найдём все такие статьи
article_tags = article_list_tag.find_all('article')

# сюда будем складывать все наши статьи
article_parsed = []

# пройдёмся в цикле по каждому тэгу article
for article_tag in article_tags:
    # найдём все наши заголовки - они начинаются с тэга h2
    header_tag = article_tag.find('h2')
    # все ссылки начинаются с тэга а
    a_tag = header_tag.find('a')
    # дата публикации содержится в тэге time
    time_tag = article_tag.find('time')

    # берём текст заголовок нашей статьи
    header_text = header_tag.text
    # у нашего тэга а есть свойство href - которое и содержит ссылку - достаём её
    link = a_tag['href']
    link = f'https://habr.com{link}'
    # в тэге time - если свойство datetime - где и содержится наше время публикации
    publication_time = time_tag['datetime']

    # теперь возьмём текст с публикации для этого нужно перейти на новую ссылку
    article_response = requests.get(link, headers=headers_gen.generate())
    # по аналогии создаём запрос и парсим его
    article = BeautifulSoup(article_response.text, 'lxml')
    # ищем тэг див с нужным свойством
    article_body_tag = article.find(name='div', id='post-content-body')
    # получаем текст
    article_body_text = article_body_tag.text

    # помещаем их в наш список словарей
    article_parsed.append({
        'header': header_text,
        'link': link,
        'publication_time': publication_time,
        'article_text': article_body_text[:20] # сократив статьи чтоб было понятнее
    })

pprint(article_parsed)