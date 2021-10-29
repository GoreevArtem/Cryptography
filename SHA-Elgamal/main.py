# main.py
import sys
from SHA256 import *
from Elgamal import *


def main():
    msg = input("Введите сообщение\n")
    msg = SHA256(msg)
    print("Хэш сообщения :\n", msg)
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
    # Закрытый ключ для получателя
    key = gen_key(q)
    h = power(g, key, q)
    print("g == ", g)
    print("g^a == ", h)
    en_msg, p = encrypt(msg, q, h, g)
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    print("Расшифрованный хэш :\n", dmsg)


if __name__ == '__main__':
    sys.exit(main() or 0)
