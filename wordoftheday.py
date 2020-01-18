
import requests
from bs4 import BeautifulSoup


class load():

    def __init__(self, date=''):

        self.url = 'https://www.merriam-webster.com/word-of-the-day/' + date
        resp = requests.get(self.url)
        html = resp.content

        soup = BeautifulSoup(html, features="html.parser")
        self.string = soup.h1.string


if __name__ == "__main__":
    word = load()
    print(word.string)
    print(word.url)
