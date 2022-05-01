import src.globals


class Vigener(src.globals.Defines):
    # Usable field

    code_str = ''
    decode_str = ''

    # Codding funcs

    def codding(self, s, key_):
        """Кодировка входного символа"""
        for i in range(0, len(self.dictionary)):
            if s in self.dictionary[i]:
                s = self.dictionary[i][key_ % src.globals.length(self.dictionary[i])]
                return s
        return None

    def symb_code(self, symb) -> int:
        """Функция, возвращающая код символа из словаря"""
        for i in range(0, len(self.dictionary)):
            if symb in self.dictionary[i]:
                gh = self.dictionary[i].index(symb)
                return gh

    def code_this(self, stringo, key) -> str:
        """Функция кодировки входной строки с помощью шифра Виженера"""
        shifr = key * ((len(stringo) // 2) + 1)
        listik = list(zip(stringo, shifr))
        i = 0
        for symbol in stringo:
            if not self.isalpha(symbol) is None:
                symbol = self.codding(symbol, self.symb_code(listik[i][0]) + self.symb_code(listik[i][1]))
                self.code_str += symbol
            else:
                self.code_str += symbol
            i += 1
        return self.code_str

    def decode(self, _str, key):
        """Функция декодировки входной строки с помощью шифра Виженера"""
        shifr = key * ((len(_str) // 2) + 1)
        listik = list(zip(_str, shifr))
        i = 0
        for symbol in _str:
            if not self.isalpha(symbol) is None:
                symbol = self.codding(symbol, self.symb_code(listik[i][0]) - self.symb_code(listik[i][1]))
                self.decode_str += symbol
            else:
                self.decode_str += symbol
            i += 1
        return self.decode_str