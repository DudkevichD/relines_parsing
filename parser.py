import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests.exceptions import MissingSchema

URL = 'https://hh.ru/'
# URL = 'https://yandex.by/search/?lr=26009&text=python&src=suggest_B'
USER = UserAgent().random
HEADERS = {'user-agent': USER}


def get_html(url, params=None):
    '''
    :param url:
    :param params:
    :return: Функция возвращает извлеченные данные из ресурса url
    '''
    try:
        requests_ = requests.get(url, headers=HEADERS, params=params)
        return requests_
    except MissingSchema as error:
        print(f'Произошла ошибка, {error}')


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # return soup.head
    return soup.h2


def parse():
    '''
    :return: Функция возвращает конечные данные
    '''
    if get_html(URL):
        html_ = get_html(URL)
        if html_.status_code == 200:
            print(get_content(html_.text))
        else:
            return f'Произошла ошибка, код состояния HTTP {html_.status_code}'
    else:
        pass


print(parse())
