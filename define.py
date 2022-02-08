import requests
from bs4 import BeautifulSoup


def define(word):
    web = requests.get('https://www.lexico.com/definition/'+word)

    data = web.content
    soup = BeautifulSoup(data, features="html.parser")

    tag = soup.find_all("words")

    for i in tag:
        print("Clue: {}".format(i.text))
        break