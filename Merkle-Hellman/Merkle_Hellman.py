import random
import math

# расширенный Алгоритм Евклида
def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x

# преобразовние сообщения в битовую форму
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# преобразовние из битовой формы в кодировку utf
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def find_sum(elem, ls):
    ls.sort(reverse=True)
    s = elem
    sum = list()
    while s != 0:
        for i in ls:
            if i <= s:
                s -= i
                sum.append(i)
    sum.sort()
    return sum

# шифрование
def encryption(bin_mes, res):
    size = len(res)
    chunks = []
    # разбиение на блоки по размерам равыне числу элементов последовательности
    i = 0
    while i < len(bin_mes):
        if i + size < len(bin_mes):
            chunks.append(bin_mes[i:i + size])
        else:
            chunks.append(bin_mes[i:len(bin_mes)])
        i += size
    s = []  # шифр текст
    # 1 - присутствие элементов в последовательности
    # 0 - его отсутствие
    # нахождение полных весов рюкзаков по одному рюкзаку для каждого блока сообщения
    for i in chunks:
        sum = 0
        for j, k in enumerate(i):
            if k == '1':
                sum += res[j]
        s.append(sum)
    return s

# расшифровка
def decryption(n, m, s, ls):
    # n -1
    n_1 = gcd_extended(n, m)[1]
    # каждое значение шифртекста умножается на n -1 mod m
    new_arr = [find_sum(i, ls) for i in [(i * n_1 % m) for i in s]]
    ls.reverse()
    bin_mes = ""
    # разбивка на биты с помощью закрытого ключа
    for i in new_arr:
        for j in ls:
            if j in i:
                bin_mes += "1"
            else:
                bin_mes += "0"
    return bin_mes

def m_generate(in_lst):
    return sum(in_lst) + random.randint(2, 100)


def n_generate(m):
    for i in list(range(m // 2, m)):
        if math.gcd(m, i) == 1:
            return i
    return -1
