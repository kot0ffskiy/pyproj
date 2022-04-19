import argparse
from collections import Counter
import string


def length(dic) -> int:
    return len(dic)


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


class Defines:
    ABC_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    nums = '1234567890'
    abc_rus = ABC_rus.lower()
    ABC_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc_eng = ABC_eng.lower()
    dictionary = [ABC_rus, nums, abc_rus, ABC_eng, abc_eng]

    eng_freq = {
        'a': 8.17, 'b': 1.4, 'c': 2.78, 'd': 4.25, 'e': 12.7, 'f': 2.23, 'g': 2.02, 'h': 6.09,
        'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93,
        'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
        'y': 1.97, 'z': 0.07
    }

    rus_freq = {
        'о': 9.28, 'а': 8.66, 'е': 8.10, 'и': 7.45, 'н': 6.35, 'т': 6.30, 'р': 5.53, 'с': 5.45,
        'л': 4.32, 'в': 4.19, 'к': 3.47, 'п': 3.35, 'м': 3.29, 'у': 2.90, 'д': 2.56, 'я': 2.22,
        'ы': 2.11, 'ь': 1.90, 'з': 1.81, 'б': 1.51, 'г': 1.41, 'й': 1.31, 'ч': 1.27, 'ю': 1.03,
        'х': 0.92, 'ж': 0.78, 'ш': 0.77, 'ц': 0.52, 'щ': 0.49, 'ф': 0.40, 'э': 0.17, 'ъ': 0.04
    }

    def isalpha(self, s):
        for i in range(0, len(self.dictionary)):
            if s in self.dictionary[i]:
                return s
        return None


class Vernam(Defines):
    def code_this(self, stringa, key) -> str:
        if key and key[0].isalpha():
            key = ' '.join(str(ord(l)) for l in key)
        ls = list(zip(stringa, key.split()))
        return ' '.join([str(ord(elem[0]) ^ int(elem[1])) for elem in ls])

    def decode(self, stringa, key) -> str:
        if key and key[0].isalpha():
            key = ' '.join(str(ord(l)) for l in key)
        ls = list(zip(stringa.split(), key.split()))
        return ''.join([chr(int(elem[0]) ^ int(elem[1])) for elem in ls])


class Vigener(Defines):
    # Usable field

    code_str = ''
    decode_str = ''

    # Codding funcs

    def codding(self, s, key_):
        for i in range(0, len(self.dictionary)):
            if s in self.dictionary[i]:
                s = self.dictionary[i][key_ % length(self.dictionary[i])]
                return s
        return None

    def symb_code(self, symb) -> int:
        for i in range(0, len(self.dictionary)):
            if symb in self.dictionary[i]:
                gh = self.dictionary[i].index(symb)
                return gh

    def code_this(self, stringo, key) -> str:
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


class Caesar(Defines):
    # Usable field

    usable_dict = 4
    code = ''
    dec_str = ''

    # Codding functions

    def find_dict(self, s):
        for letter in s:
            if self.isalpha(letter):
                for i in range(0, len(self.dictionary)):
                    if letter in self.dictionary[i]:
                        self.usable_dict = i
                        return

    def codding(self, s, k2) -> str:
        for i in range(0, len(self.dictionary)):
            if s in self.dictionary[i]:
                ind = self.dictionary[i].index(s)
                s = self.dictionary[i][(ind + k2) % length(self.dictionary[i])]
                break
        return s

    def code_this(self, dec_str, k_1):
        code = ''
        for symbol in dec_str:
            symbol = self.codding(symbol, k_1)
            code += symbol
        self.code = code
        return code

    # Decoding

    def decode(self, code, keyword) -> str:
        self.dec_str = ''
        for symbol in code:
            symbol = self.codding(symbol, (-1) * keyword)
            self.dec_str += symbol
        return self.dec_str

    # Intellect decode

    def metrika(self, _dict, len_words) -> list:
        if self.dictionary[self.usable_dict] == self.abc_rus:  # Если русское слово
            return sum([abs((_dict[i] * 100) / len_words - self.rus_freq[i]) for i in self.rus_freq.keys()])
        else:
            return sum([abs((_dict[i] * 100) / len_words - self.eng_freq[i]) for i in self.eng_freq.keys()])

    def int_dec(self, _str):
        self.find_dict(_str.lower())
        lis = []
        for i in range(0, len(self.dictionary[self.usable_dict])):
            words = self.decode(_str, i)
            words_len = len(words)
            words = remove_chars_from_text(words, string.punctuation + ' ')
            counter = Counter(words.lower())
            lis.append(self.metrika(counter, words_len))
        keyword = lis.index(min(lis))
        return self.decode(_str, keyword)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt!it#")
    # parser.add_argument('-test', type=bool, dest='testing', help='Execute testing script: 1 or 0')
    parser.add_argument('-p', '--path', type=str, dest='path', required=True,
                        help='path to file')  # добавь тестовый запуск для случая когда путь не указан
    parser.add_argument('-o', '--output', type=str, dest='output', required=True, help='path to file with code.')
    parser.add_argument('-doc', '--decorcod', type=bool, required=True, dest='dec_or_cod',
                        help='type 1 if you want to encrypt or 0 - to decrypt')
    parser.add_argument('-i', '--intel', type=bool, required=False, dest='intel', help='intellect encryption research')
    parser.add_argument('-t', '--type', type=str, required=False, dest='type',
                        help='set "c" for Ceasar, "vig" for Vigener or "ver" for Vernam')
    parser.add_argument('-k', '--key', required=False, dest='key', help='destination of file with encryption key')

    args = parser.parse_args()
    shifr_dict = {
        'c': Caesar,
        'vig': Vigener,
        'ver': Vernam
    }
    with open(args.path, 'r') as f_read:
        if args.intel:
            stringa = f_read.read()
            f_write = open(args.output, 'w')
            obj = Caesar()
            f_write.write(obj.int_dec(stringa))
            f_write.close()
        elif args.dec_or_cod:  # Шифровка
            stringa = f_read.read()
            f_write = open(args.output, 'w')
            obj = shifr_dict[args.type]()
            with open(args.key, 'r') as file_key:
                key = file_key.read()
                f_write.write(obj.code_this(stringa, key))
            f_write.close()
        else:
            stringa = f_read.read()
            f_write = open(args.output, 'w')
            obj = shifr_dict[args.type]()
            with open(args.key, 'r') as file_key:
                key = file_key.read()
                f_write.write(obj.decode(stringa, key))
            f_write.close()
