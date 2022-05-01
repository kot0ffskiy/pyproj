import src.globals
import string
from collections import Counter

class Caesar(src.globals.Defines):
    # Usable field

    usable_dict = 4
    code = ''
    dec_str = ''

    # Codding functions

    def find_dict(self, s):
        """Функция, которая находит словарь, в котором содержится подающийся на вход символ"""
        for letter in s:
            if self.isalpha(letter):
                for i in range(0, len(self.dictionary)):
                    if letter in self.dictionary[i]:
                        self.usable_dict = i
                        return

    def codding(self, s, k2) -> str:
        """Кодировка символа по переданному ключу"""
        for i in range(0, len(self.dictionary)):
            if s in self.dictionary[i]:
                ind = self.dictionary[i].index(s)
                s = self.dictionary[i][(ind + k2) % src.globals.length(self.dictionary[i])]
                break
        return s

    def code_this(self, dec_str, k_1):
        """Кодировка введённой строки"""
        code = ''
        for symbol in dec_str:
            symbol = self.codding(symbol, k_1)
            code += symbol
        self.code = code
        return code

    # Decoding

    def decode(self, code, keyword) -> str:
        """Функция декодировки строки"""
        self.dec_str = ''
        for symbol in code:
            symbol = self.codding(symbol, (-1) * keyword)
            self.dec_str += symbol
        return self.dec_str

    # Intellect decode

    def metrika(self, _dict, len_words) -> list:
        """Внутрення функция класса. Считает частоту появления символа в строке и суммирует отклонение от табличных данных. 
           Чем меньше значение, тем ближе к истине"""
        if self.dictionary[self.usable_dict] == self.abc_rus:  # Если русское слово
            return sum([abs((_dict[i] * 100 / len_words - self.rus_freq[i]) for i in self.rus_freq.keys())])
        else:
            return sum([abs((_dict[i] * 100) / len_words - self.eng_freq[i]) for i in self.eng_freq.keys()])

    def int_dec(self, _str):
        """Функция декодировки шифра Цезаря методом частотного анализа"""
        self.find_dict(_str.lower())
        lis = []
        for i in range(0, len(self.dictionary[self.usable_dict])):
            words = self.decode(_str, i)
            words_len = len(words)
            words = src.globals.remove_chars_from_text(words, string.punctuation + ' ')
            counter = Counter(words.lower())
            lis.append(self.metrika(counter, words_len))
        keyword = lis.index(min(lis))
        return self.decode(_str, keyword)
