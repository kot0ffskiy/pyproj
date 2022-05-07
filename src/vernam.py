import src.globals


class Vernam(src.globals.Defines):
    def code_this(self, stringa, key) -> str:
        """Функция кодировки строки шифром Вернама"""
        if key and key[0].isalpha():
            key = ' '.join(str(ord(l)) for l in key)
        ls = list(zip(stringa, key.split()))
        return ' '.join([str(ord(elem[0]) ^ int(elem[1])) for elem in ls])

    def decode(self, stringa, key) -> str:
        """Функция декодировки строки шифром Вернама"""
        if key and key[0].isalpha():
            key = ' '.join(str(ord(l)) for l in key)
        ls = list(zip(stringa.split(), key.split()))
        return ''.join([chr(int(elem[0]) ^ int(elem[1])) for elem in ls])
