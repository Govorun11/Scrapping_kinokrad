import csv
import json
from typing import Dict


class RWHtmlCode:

    @staticmethod
    def write_code(page, src) -> None:
        with open(f'{page}_page_code.html', 'w', encoding='utf-8') as file:
            file.write(src)

    @staticmethod
    def read_code(page) -> str:
        with open(f'{page}_page_code.html', encoding='utf-8') as file:
            src = file.read()
        return src


class RWJsonCode:

    @staticmethod
    def _writing_json_code(page: int, all_films_in_page: Dict) -> None:
        with open(f'{page}_all_films.json', 'w', encoding='utf-8') as file:
            json.dump(all_films_in_page, file, indent=4, ensure_ascii=False)

    @staticmethod
    def reading_json_code(page) -> Dict:
        with open(f'{page}_all_films.json', encoding='utf-8') as file:
            all_films_in_page = json.load(file)
        return all_films_in_page


class RWCSVCode:

    @staticmethod
    def _write_code(row, max_page) -> None:
        with open(f'all_films_on_{max_page}_pages.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    @staticmethod
    def _append_code(row, max_page) -> None:
        with open(f'all_films_on_{max_page}_pages.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row)
