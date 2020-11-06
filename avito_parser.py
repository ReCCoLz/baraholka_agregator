from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import urllib

main_search_link_avito = 'https://www.avito.ru/novosibirsk?cd=1&q='
avito_link = 'https://www.avito.ru/'


def translate(name):
    letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
               'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
               'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
               'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
               'ю': 'u', 'я': 'ja', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
               'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
               'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
               'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
               'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
               '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
               ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
               '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
               'Є': 'e', '—': ''}
    for key in letters:
        name = name.replace(key, letters[key])
    return name


# def town_link():
#     town = str(input())
#     avito_link_2 = avito_link + transliterate(town)
#     return avito_link_2, town

reques = str(input('Введите ваш город и желаемый товар через слэш ("/") \n'))
reques = reques.split('/')
print(reques)


def user_request(name):
    final_avito_link = 'https://www.avito.ru/' + translate(name[0]).lower() + '?cd=1&q=' + name[1].lower()
    return final_avito_link


def get_url(link):
    rs = urlopen(link)
    root = BeautifulSoup(rs, 'html.parser')
    print(root)


print(get_url(avito_link))
print(user_request(reques))
