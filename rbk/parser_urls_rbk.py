import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = 'https://www.rbc.ru/'
USER = UserAgent().random
HEADERS = {'user-agent': USER}


def get_html(url, params=None):
    requests_ = requests.get(url, headers=HEADERS, params=params)
    return requests_


def get_urls(html):
    links = []
    soup = BeautifulSoup(html, 'html.parser')

    main_link = soup.find('a', class_='main__big__link js-yandex-counter')
    main_link = main_link.get('href')
    links.append(main_link)

    list_links = soup.find('div', class_='main__list')
    for link in list_links.find_all('a'):
        import re
        pattern = r'from=from_main_'
        if re.search(pattern, str(link)):
            links.append(link.get('href'))
    return links


def parse_urls_rbk():
    html_ = get_html(URL)
    if html_.status_code == 200:
        return get_urls(html_.text)


