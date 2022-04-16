'''
scrape movies into files .csv, .json
Good luck, man!)
'''
import os
import requests

from bs4 import BeautifulSoup
from all_film_in_pages.rwcode import RWHtmlCode, RWJsonCode, RWCSVCode


def main(max_page: int):
    page = 1
    while page <= max_page:
        url = f'https://kinokrad.co/page/{page}/'
        req = requests.get(url)
        src = req.text

        RWHtmlCode.write_code(page, src)
        RWHtmlCode.read_code(page)
        soup = BeautifulSoup(src, 'lxml')

        all_shorbox_in_page = soup.find_all(class_='shorbox')
        all_films_in_page = dict()

        for shorbox in all_shorbox_in_page:
            shorbox_data = list()
            film_name = shorbox.find('div', class_='postertitle').find('h2').find('a').text
            film_href = shorbox.find('div', class_='postertitle').find('h2').find('a').get('href')
            all_films_in_page[film_name] = film_href
            all_godshort = shorbox.find('div', class_='shortboxh').find_all('div', class_='godshort')

            for godshort in all_godshort:
                shorbox_data.append(godshort.find('span', class_='orange').text)

            film_year = shorbox_data[0]
            film_country = shorbox_data[1]
            film_genre = shorbox_data[2]
            film_director = shorbox_data[3]

            if not os.path.exists(f'all_films_on_{max_page}_pages.csv'):
                table_headers = soup.find('div', class_='shortboxh').find_all('div', class_='godshort')
                name_head = 'Название фильма'
                href_head = 'Ссылка фильма'
                year_head = table_headers[0].find('span').text
                country_head = table_headers[1].find('span').text
                genre_head = table_headers[2].find('span').text
                director_head = table_headers[3].find('span').text

                writing_row = (name_head, href_head, year_head, country_head, genre_head, director_head)
                RWCSVCode._write_code(writing_row, max_page)

            appending_row = (film_name, film_href, film_year, film_country, film_genre, film_director)
            RWCSVCode._append_code(appending_row, max_page)

        RWJsonCode._writing_json_code(page, all_films_in_page)
        page += 1


if __name__ == '__main__':
    main(10)
