import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from rbk.parser_urls_rbk import parse_urls_rbk

USER = UserAgent().random
HEADERS = {'user-agent': USER}
URL = parse_urls_rbk()


def get_html(url, params=None):
    requests_ = requests.get(url, headers=HEADERS, params=params)
    return requests_


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')




def parse_urls_rbk():
    html_ = get_html(URL)
    if html_.status_code == 200:
        return get_content(html_.text)
