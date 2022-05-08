# Вывод фильмов если жанр == genre.
import requests

from bs4 import BeautifulSoup
from typing import List, Dict

from scrapp_for_genre.RWCode import RWCode


class FindMovieByGenre:
    HEADERS: Dict = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 '
                      'Mobile Safari/537.36'
    }

    def __init__(self, genre: str, page: int = 1) -> None:
        self.genre = genre
        self.page = page
        self.url = f'https://kinokrad.co/page/{page}/'
        self.REQ = requests.get(self.url, headers=self.HEADERS)
        self.SRC = self.REQ.text
        self.soup = BeautifulSoup(self.SRC, "lxml")
        self.all_film_by_genre = {}

    def finder_by_genre(self) -> Dict:
        all_films: List = self.soup.find_all('div', class_='shorposterbox')

        for film in all_films:
            genre_of_film = film.find('div', class_='godshort janr').find('span', class_='orange').find_all('a')

            for genre in genre_of_film:
                if genre.text == self.genre:
                    film_name = film.find('div', class_='postertitle').find('a')
                    film_href = film_name.get('href')
                    self.all_film_by_genre[film_name.text] = film_href
        return self.all_film_by_genre


read_write_code = RWCode()
comedy = FindMovieByGenre('комедия', 2)

if __name__ == '__main__':
    read_write_code.code_writing(comedy.SRC)
    read_write_code.code_writing_to_json(comedy.finder_by_genre())
