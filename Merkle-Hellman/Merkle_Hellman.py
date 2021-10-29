# расширеннЫй Алгоритм Евклида

def euclid_algorithm(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        # q является частным
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def find_sum(elem, list):
    list.sort(reverse=True)
    s = elem
    g = []
    while s != 0:
        for i in list:
            if i <= s:
                s -= i
                g.append(i)
    g.sort()
    return g


def encryption(bin_mes, res):
    size = len(res)
    chunks = []
    # разбиение на блоки
    i = 0
    while i < len(bin_mes):
        if i + size < len(bin_mes):
            chunks.append(bin_mes[i:i + size])
        else:
            chunks.append(bin_mes[i:len(bin_mes)])
        i += size
    s = []  # шифр текст
    for i in chunks:
        sum = 0
        for j, k in enumerate(i):
            if k == '1':
                sum += res[j]
        s.append(sum)
    return s


def decryption(n, m, s, ls):
    n_1 = euclid_algorithm(n, m)
    rr = []
    for i in s:
        rr.append(i * n_1 % m)
    new_arr = []
    for i in rr:
        new_arr.append(find_sum(i, ls))
    ls.reverse()
    bin_mes = ""
    for i in new_arr:
        for j in ls:
            if j in i:
                bin_mes += "1"

            if j not in i:
                bin_mes += "0"
    return bin_mes


from random import *


def knapsack_generate():
    lst = [1]
    sum = 1
    random_int = randint(1, 10)
    sum += random_int
    lst.append(1 + random_int)
    for i in range(4):
        random_int = randint(1, 10)
        next_int = sum + random_int
        sum += next_int
        lst.append(next_int)
    return lst


def m_generate(in_lst):
    sum = 0
    for i in in_lst:
        sum += i
    return sum + randint(2, 100)


def n_generate(m):
    for i in list(range(m // 2, m)):
        from math import gcd
        if gcd(m, i) == 1:
            return i
    return -1
