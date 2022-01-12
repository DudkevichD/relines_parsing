import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from fake_useragent import UserAgent
from rbk.parser_urls_rbk import parse_urls_rbk

USER = UserAgent().random
HEADERS = {'user-agent': USER}
URL = parse_urls_rbk()
CLASS_CONTENT = SoupStrainer(attrs={
    'class': ['l-col-center-590 article__content'],
})


def get_html(url, params=None):
    requests_ = requests.get(url, headers=HEADERS, params=params)
    return requests_


def get_content(html, img=None):
    soup = BeautifulSoup(html, 'html.parser', parse_only=CLASS_CONTENT)
    soup.extend('span')
    soup.find('a', class_='article__header__category')
    if soup.find('a', class_='article__header__category'):
        theme = soup.find('a', class_='article__header__category').get_text()
    else:
        theme = '-'
    if soup.find('span', class_='article__header__date'):
        date = soup.find('span', class_='article__header__date').get_text()
    else:
        date = '-'
    title = soup.find('h1').get_text()
    if soup.find('div', class_='article__header__yandex'):
        preface = soup.find('div', class_='article__header__yandex').get_text()
    else:
        preface = '-'

    if soup.find('div', class_='article__text__overview'):
        overview = soup.find('div', class_='article__text__overview').get_text(strip='True')
    else:
        overview = '-'

    foto = foto = {
        'foto_url': '-',
        'photo_description': '-',
        'author': '-'
    }

    if img:

        if soup.find('div', class_='article__main-image__wrap'):
            foto['foto_url'] = soup.find('div', class_='article__main-image__wrap').find('img').get('src')

        if soup.find('div', class_='article__main-image__wrap'):
            foto['photo_description'] = soup.find('div', class_='article__main-image__wrap').find('img').get('alt')

        if soup.find('span', class_='article__main-image__author'):
            foto['author'] = soup.find('span', class_='article__main-image__author').get_text(strip='True')

    text = '-'
    if soup.find(class_='article__text article__text_free'):

        tags_p = (soup.find(class_='article__text article__text_free').find_all('p'))
        for tag_p in tags_p:
            if tag_p.span is not None:
                continue
            text += tag_p.get_text(strip='True')
            text += '\n'

    new = {
        'theme': theme,
        'date': date,
        'title': title,
        'preface': preface,
        'overview': overview,
        'foto': foto,
        'text': text,
    }

    return new


def parse_urls_rbk(img=None):
    dict = {}
    n = 0
    for url in URL:
        n += 1
        html_ = get_html(url)
        if html_.status_code == 200:
            dict[n] = get_content(html_.text, img)


    return dict
