import base64


class RS4:
    """класс алгоритма RS4"""

    def __init__(self, msg, key):
        """
        :param msg: ссобщение
        :param key: ключ
        """
        self.msg = msg
        self.key = key

    @staticmethod
    def ksa(key):
        """
        Генерация S-блока на основе секретного ключа
        :param key: ключ
        :return: блок (в данном случае список) длиной 256
        """
        S = list(range(256))
        j = 0
        """
        Инициализация начинается с заполнения массива S, далее этот массив перемешивается путём перестановок, 
        определяемых ключом. Так как только одно действие выполняется над S, то должно выполняться утверждение, 
        что S всегда содержит один набор значений, который был дан при первоначальной инициализации (S[i] := i). 
        """
        for i in range(256):
            j = (j + S[i] + ord(key[i % len(key)])) % 256  # генерируем псевдослучайно индексы
            S[i], S[j] = S[j], S[i]  # перестановка
        return S

    @staticmethod
    def prga(msg, s):
        """
        генератор псевдослучайной последовательности (англ. pseudo-random generation algorithm, PRGA)
        :param msg: сообщение
        :param s: блок s размером в 256 байт
        :return: n-битное слово K из ключевого потока
        """
        K = []
        i, j = 0, 0
        for x in msg:
            """
            Генератор ключевого потока RC4 переставляет значения, хранящиеся в S
            """
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            """
            В одном цикле RC4 определяется одно n-битное слово K из ключевого потока. В дальнейшем ключевое слово 
            будет сложено по модулю два с исходным текстом, которое пользователь хочет зашифровать, 
            и получен зашифрованный текст. 
            """
            K.append(chr(ord(x) ^ s[(s[i] + s[j]) % 256]))
        return "".join(K)

    def crypt(self):
        """
        :return: зашифрованное слово и расшифрованное
        в обоих случаях используем prga в первом для шифрования, во втором для расшифровки
        """
        encrpt = str(base64.b64encode(self.prga(self.msg, self.ksa(self.key)).encode('utf-8')), 'utf-8')
        decrpt = self.prga(bytes.decode(base64.b64decode(encrpt)), self.ksa(self.key))
        return encrpt, decrpt


if __name__ == '__main__':
    msg = input("\033[34m1. Введите сообщение:      ")
    key = input("2. Введите ключ:           ")
    rc4 = RS4(msg, key)
    encrpt, decrpt = rc4.crypt()
    print("\033[31m3. Зашифрованный текст:   ", encrpt)
    print("4. Расшифрованный текст:  ", decrpt)
