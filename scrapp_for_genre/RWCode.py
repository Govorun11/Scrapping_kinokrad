import json
from typing import Dict


class RWCode:

    @staticmethod
    def code_reading() -> str:
        with open('index2.html', encoding='utf-8') as file:
            src = file.read()
        return src

    @staticmethod
    def code_writing(src: str):
        with open('index2.html', 'a', encoding='utf-8') as file:
            file.write(src)

    @staticmethod
    def code_writing_to_json(data: Dict) -> None:
        with open('index2.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
