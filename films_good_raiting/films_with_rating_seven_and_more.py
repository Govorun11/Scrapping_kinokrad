import requests

from bs4 import BeautifulSoup
from films_good_raiting.ReaddWriteCodeRaiting import ReadWrite


class GoodRaitMovies:
    HEADERS = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 '
                      'Mobile Safari/537.36'
    }

    def __init__(self, page: int = 1) -> None:
        self.page = page
        self.url = f'https://kinokrad.co/page/{page}/'
        self.req = requests.get(self.url, headers=self.HEADERS)
        self.src = self.req.text
        self.soup = BeautifulSoup(self.src, 'lxml')



    def good_raiting_movies(self):
        all_films_in_page = self.soup.find_all('div', class_='shorposterbox')
        film_with_good_rating = [film for film in all_films_in_page
                                 if int(film.find('li', class_='current-rating').text) >= 7]

        for film in film_with_good_rating:
            name_film = film.find('div', class_='postertitle').find('h2').find('a')
            film_rating = film.find('li', class_='current-rating').text
            film_href = name_film.get('href')
            short_text = film.find('div', class_='shorttext').text.strip()
            print(f'{name_film.text} - {film_rating}*,\n'
                  f'{film_href}\n'
                  f'{short_text}\n')


movie = GoodRaitMovies(5)
rwcode = ReadWrite()
if __name__ == '__main__':
    rwcode.code_writing(movie.src)
    movie.good_raiting_movies()

