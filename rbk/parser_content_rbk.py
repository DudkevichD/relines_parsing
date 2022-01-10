import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from rbk.parser_urls_rbk import parse_urls_rbk

USER = UserAgent().random
HEADERS = {'user-agent': USER}
URL = parse_urls_rbk()

print(len(URL))


def get_html(url, params=None):
    requests_ = requests.get(url, headers=HEADERS, params=params)
    print(url)
    return requests_


def get_content(html, img=None):
    soup = BeautifulSoup(html, 'html.parser')
    soup.find('a', class_='article__header__category')
    theme = soup.find('a', class_='article__header__category').get_text()
    date = soup.find('span', class_='article__header__date').get_text()
    title = soup.find('h1').get_text()
    preface = soup.find('div', class_='article__header__yandex').get_text()
    # text = soup.find('div', class_='article__text article__text_free').get_text('\n', strip='True')
    overview = soup.find('div', class_='article__text__overview').get_text(strip='True')
    if img:
        foto = {
            'foto_url': soup.find('div', class_='article__main-image__wrap').find('img').get('src'),
            'photo_description': soup.find('div', class_='article__main-image__wrap').find('img').get('alt'),
            'author': soup.find('span', class_='article__main-image__author').get_text(strip='True'),
        }

    else:
        foto = {
            'foto_url': '',
            'photo_description': '',
            'author': ''
        }
    text = soup.find('div', class_='article__text article__text_free').find('p').get_text()
    text_1 = soup.find('div', class_='article__text article__text_free').find('p')
    for element in text_1.next_elements:
        text += element.get_text()
        if element == ' body_median ':
            break

    print(preface)


def parse_urls_rbk(img=None):
    html_ = get_html(URL[9])
    if html_.status_code == 200:
        return get_content(html_.text, img)


parse_urls_rbk(1)
