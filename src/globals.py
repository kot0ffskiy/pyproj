def length(dic) -> int:
    """Фуункция, возвращающая размер входного словаря"""
    return len(dic)


def remove_chars_from_text(text, chars):
    """Функция, удаляющая символы, находящиеся в chars, из входной строки"""
    return ''.join([ch for ch in text if ch not in chars])


class Defines:
    ABC_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    nums = '1234567890'
    abc_rus = ABC_rus.lower()
    ABC_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
        """Функция, проверяющая, является ли символ буквой"""
        for i in range(0, len(self.dictionary)):
            if s in self.dictionary[i]:
                return s
        return None