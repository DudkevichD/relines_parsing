import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests.exceptions import MissingSchema

URL = 'https://www.rbc.ru/politics/10/01/2022/61dc695e9a79475bd37805d1?from=from_main_1'
USER = UserAgent().random
HEADERS = {'user-agent': USER}


def get_html(url, params=None):
    try:
        requests_ = requests.get(url, headers=HEADERS, params=params)
        return requests_
    except MissingSchema as error:
        print(f'Произошла ошибка, {error}')


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.body


def content_parsing(content):
    print(content.find('div', class_='l-col-main').get_text('\n', strip='True'))
    content = content.find('div', class_='l-col-main')
    list_tags = []
    for tag in content.find_all(True):
        list_tags.append(tag.name)
    print(list_tags)

    return 1


def parse():
    if get_html(URL):
        html_ = get_html(URL)
        if html_.status_code == 200:
            all_content = get_content(html_.text)
            final_data = content_parsing(all_content)
            return final_data
        else:
            return f'Произошла ошибка, код состояния HTTP {html_.status_code}'
    else:
        pass


parse()
