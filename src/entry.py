import argparse
import src.caesar
import src.vernam
import src.vigener


class Entry:
    
    def __init__(self):
        """Функция-конструктор класса"""
        args = self.parse_inp()
        shifr_dict = {'c': src.caesar.Caesar, 'vig': src.vigener.Vigener,'ver': src.vernam.Vernam }
        with open(args.path, 'r') as f_read:
            if args.intel:
                self.intel(args, f_read)
            elif args.dec_or_cod:  # Шифровка
                self.shifr(args, shifr_dict, f_read)
            else:
                self.deshifr(args, shifr_dict, f_read)

    def parse_inp(self):
        """Парсер входных параметров"""
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
        return args

    def intel(self, args, f_read):
        """Функция, запускающая дешифровку методом частотного анализа"""
        stringa = f_read.read()
        f_write = open(args.output, 'w')
        obj = src.caesar.Caesar()
        f_write.write(obj.int_dec(stringa))
        f_write.close()

    def shifr(self, args, shifr_dict, f_read):
        """Функция, применяющая конкретный метод шифрования входной строки"""
        stringa = f_read.read()
        f_write = open(args.output, 'w')
        obj = shifr_dict[args.type]()
        with open(args.key, 'r') as file_key:
            key = file_key.read()
            f_write.write(obj.code_this(stringa, key))
        f_write.close()

    def deshifr(self, args, shifr_dict, f_read):
        """Функция дешифрования закодированной строки"""
        stringa = f_read.read()
        f_write = open(args.output, 'w')
        obj = shifr_dict[args.type]()
        file_key = open(args.key, 'r')
        key = file_key.read()
        file_key.close()
        f_write.write(obj.decode(stringa, key))
        f_write.close()