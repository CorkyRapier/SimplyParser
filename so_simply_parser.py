from bs4 import BeautifulSoup
import requests

url = "https://habr.com/ru/search/?q=python&target_type=posts&order=date"

request = requests.get(url)

soup = BeautifulSoup(request.text, "html.parser")

teme = soup.find_all("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2")

# link = soup.find_all('a', class_="tm-article-snippet__title-link")

parser_file_txt = open('text.txt', 'w')

for temes in teme:
    temes = temes.find('a')
    if temes is not None:
        sublink = temes.get('href')
        # print(str(temes.text) + ' ' + 'https://habr.com' + str(sublink))
        # print('-------------------------------------------------')
        parser_file_txt.write(str(temes.text) + ' ||| ' + 'https://habr.com' + str(sublink) + '\n')
        parser_file_txt.write('------------------------------------------------------------' + '\n')

parser_file_txt.close()
