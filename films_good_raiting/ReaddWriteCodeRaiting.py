class ReadWrite:
    def code_writing(self, src):
        with open('index3.html', 'w', encoding='utf-8') as file:
            file.write(src)


    def code_reading(self):
        with open('index3.html', encoding='utf-8') as file:
            src = file.read()
        return src