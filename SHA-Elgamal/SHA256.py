# SHA256.pu
# константа для суммы по mod 2**32
VAL_MOD = 2 ** 32


# вставка нулей в конец битовой последовательности
def set_zero_in_end(bites, len_str):
    while len(bites) % len_str != 0:
        bites += '0'
    return bites


# вставка нулей в начало битовой последовательности
def set_zero_in_start(bites, len_str):
    while len(bites) % len_str != 0:
        bites = '0' + bites
    return bites


# ставки в конец битовой последовательности текста длины сообщения
def set_len_str_in_end(bits, bits_len, max_mod=1024):
    while (len(bits) + len(bits_len)) % max_mod != 0:
        bits += '0'
    bits += bits_len
    return bits


# перевод числа из 16-ричного представления в бинарное
def hex_to_bin(hex_num, len_bits=64):
    bits = bin(hex_num)[2:]
    # добавление в начало нули для получения нужной длины последовательности
    while len(bits) < len_bits:
        bits = '0' + bits
    return bits


# перевод строки в бинарное представление
def str_to_bin(text):
    binary = ''
    # приводим текст к виде списка байт
    byte_array = bytearray(text, "utf8")
    # каждый байт преобразуем в битовую строчку
    for byte in byte_array:
        binary_repr = bin(byte)[2:]
        while len(binary_repr) < 8:
            binary_repr = '0' + binary_repr
        binary += binary_repr
    return binary


# циклический сдвиг вправо бинарной последовательности
def rotate_right(list_bits, count):
    for _ in range(count):
        list_bits = list_bits[-1] + list_bits[:-1]
    return list_bits


# логический сдивг вправо бинарной последовательности
def shift_right(list_bits, count):
    for _ in range(count):
        list_bits = '0' + list_bits[:-1]
    return list_bits


# вычисление исключающего или
def xor(list_bits1, list_bits2):
    # дополняем последовательности до одинаковой длины
    max_len = max(len(list_bits1), len(list_bits2))
    list_bits1 = '0' * (max_len - len(list_bits1)) + list_bits1
    list_bits2 = '0' * (max_len - len(list_bits2)) + list_bits2
    rez_bits = []
    # xor: 1 если хотя бы один бит 1, но не оба вместе, иначе 0
    for i in range(max_len):
        new_bit = '1' if list_bits1[i] != list_bits2[i] else '0'
        rez_bits.append(new_bit)
    return ''.join(rez_bits)


# вычисление логического И
def log_and(bits1, bits2):
    max_len = max(len(bits1), len(bits2))
    bits1 = '0' * (max_len - len(bits1)) + bits1
    bits2 = '0' * (max_len - len(bits2)) + bits2
    rez_bits = []
    for i in range(max_len):
        new_bit = '1' if bits1[i] == bits2[i] == '1' else '0'
        rez_bits.append(new_bit)
    return ''.join(rez_bits)


# суммирование битовых последовательностей
def sum_bit_seq(*list_bits):
    summa = 0
    # для получения суммы всё переводится к обычным 10-чным числам
    for bit in list_bits:
        summa += int(bit, base=2)
    # в sha-256 сумма берется по mod 2**32
    summa = summa % VAL_MOD
    # приводим обратно к битовой последовательности
    binary = bin(summa)[2:]
    while len(binary) < 32:
        binary = '0' + binary
    return binary


# получение отрицания от битовой последовательности
def log_not(bits):
    binary = ''
    for bit in bits:
        binary += '1' if bit == '0' else '0'
    return binary


# заполняем список первоначальных значений хеш-функции
# первые 32 бита дробных частей квадратных корней первых восьми простых чисел
H0 = hex_to_bin(0x6A09E667)
H1 = hex_to_bin(0xBB67AE85)
H2 = hex_to_bin(0x3C6EF372)
H3 = hex_to_bin(0xA54FF53A)
H4 = hex_to_bin(0x510E527F)
H5 = hex_to_bin(0x9B05688C)
H6 = hex_to_bin(0x1F83D9AB)
H7 = hex_to_bin(0x5BE0CD19)

# таблица констант
# первые 32 бита дробных частей кубических корней первых 64 простых чисел
constants = [
    hex_to_bin(0x428A2F98), hex_to_bin(0x71374491), hex_to_bin(0xB5C0FBCF), hex_to_bin(0xE9B5DBA5),
    hex_to_bin(0x3956C25B), hex_to_bin(0x59F111F1), hex_to_bin(0x923F82A4), hex_to_bin(0xAB1C5ED5),
    hex_to_bin(0xD807AA98), hex_to_bin(0x12835B01), hex_to_bin(0x243185BE), hex_to_bin(0x550C7DC3),
    hex_to_bin(0x72BE5D74), hex_to_bin(0x80DEB1FE), hex_to_bin(0x9BDC06A7), hex_to_bin(0xC19BF174),
    hex_to_bin(0xE49B69C1), hex_to_bin(0xEFBE4786), hex_to_bin(0x0FC19DC6), hex_to_bin(0x240CA1CC),
    hex_to_bin(0x2DE92C6F), hex_to_bin(0x4A7484AA), hex_to_bin(0x5CB0A9DC), hex_to_bin(0x76F988DA),
    hex_to_bin(0x983E5152), hex_to_bin(0xA831C66D), hex_to_bin(0xB00327C8), hex_to_bin(0xBF597FC7),
    hex_to_bin(0xC6E00BF3), hex_to_bin(0xD5A79147), hex_to_bin(0x06CA6351), hex_to_bin(0x14292967),
    hex_to_bin(0x27B70A85), hex_to_bin(0x2E1B2138), hex_to_bin(0x4D2C6DFC), hex_to_bin(0x53380D13),
    hex_to_bin(0x650A7354), hex_to_bin(0x766A0ABB), hex_to_bin(0x81C2C92E), hex_to_bin(0x92722C85),
    hex_to_bin(0xA2BFE8A1), hex_to_bin(0xA81A664B), hex_to_bin(0xC24B8B70), hex_to_bin(0xC76C51A3),
    hex_to_bin(0xD192E819), hex_to_bin(0xD6990624), hex_to_bin(0xF40E3585), hex_to_bin(0x106AA070),
    hex_to_bin(0x19A4C116), hex_to_bin(0x1E376C08), hex_to_bin(0x2748774C), hex_to_bin(0x34B0BCB5),
    hex_to_bin(0x391C0CB3), hex_to_bin(0x4ED8AA4A), hex_to_bin(0x5B9CCA4F), hex_to_bin(0x682E6FF3),
    hex_to_bin(0x748F82EE), hex_to_bin(0x78A5636F), hex_to_bin(0x84C87814), hex_to_bin(0x8CC70208),
    hex_to_bin(0x90BEFFFA), hex_to_bin(0xA4506CEB), hex_to_bin(0xBEF9A3F7), hex_to_bin(0xC67178F2),
]


def SHA256(msg: str) -> str:
    # НАЧАЛО АЛГОРИТМА
    # сообщение для хеширования
    # переводим сообщение в битовую последовательность
    m = str_to_bin(msg)
    # добавляем в конец '1'
    m = m + "1"
    # добавляем в конец исходную длину сообщения в виде 64 битной последователньости
    bits_len = set_zero_in_start(bin(len(msg) * 8)[2:], 64)
    # добавляем в конец длину строки
    m = set_len_str_in_end(m, bits_len)

    for i in range(0, len(m), 512):
        part = m[i:i + 512]
        parts = []
        # разбиваем исходное сообщение на 16 блоков длиной 32 бита
        for j in range(0, 512, 32):
            parts.append(part[j:j + 32])

    for k in range(16, 64):
        rr1 = rotate_right(parts[k - 15], 7)
        rr2 = rotate_right(parts[k - 15], 18)
        sr = shift_right(parts[k - 15], 3)
        x1 = xor(rr1, rr2)
        s0 = xor(x1, sr)
        rr1 = rotate_right(parts[k - 2], 17)
        rr2 = rotate_right(parts[k - 2], 19)
        sh = shift_right(parts[k - 2], 10)
        x1 = xor(rr1, rr2)
        s1 = xor(x1, sh)
        new_part = sum_bit_seq(parts[k - 16], s0, parts[k - 7], s1)
        parts.append(new_part)

    # инициализируем дополнительные переменные
    a = H0
    b = H1
    c = H2
    d = H3
    e = H4
    f = H5
    g = H6
    h = H7

    # весь алгоритм хеширования выполняется 64 раза
    for k in range(64):
        rr1 = rotate_right(e, 6)
        rr2 = rotate_right(e, 11)
        rr3 = rotate_right(e, 25)
        x1 = xor(rr1, rr2)
        s1 = xor(x1, rr3)
        rr1 = log_and(e, f)
        rr3 = log_and(log_not(e), g)
        ch = xor(rr1, rr3)
        t1 = sum_bit_seq(h, s1, ch, constants[k], parts[k])
        rr1 = rotate_right(a, 2)
        rr2 = rotate_right(a, 13)
        rr3 = rotate_right(a, 22)
        x1 = xor(rr1, rr2)
        s0 = xor(x1, rr3)
        rr1 = log_and(a, b)
        rr2 = log_and(a, c)
        rr3 = log_and(b, c)
        x1 = xor(rr1, rr2)
        maj = xor(x1, rr3)
        t2 = sum_bit_seq(s0, maj)
        h = g
        g = f
        f = e
        e = sum_bit_seq(d, t1)
        d = c
        c = b
        b = a
        a = sum_bit_seq(t1, t2)

    # в конце необходимо изменить начальные переменные для хранения хеша
    h0 = sum_bit_seq(H0, a)
    h1 = sum_bit_seq(H1, b)
    h2 = sum_bit_seq(H2, c)
    h3 = sum_bit_seq(H3, d)
    h4 = sum_bit_seq(H4, e)
    h5 = sum_bit_seq(H5, f)
    h6 = sum_bit_seq(H6, g)
    h7 = sum_bit_seq(H7, h)

    # приводим вычисленные бинарные последовательности к 16-ым значениям
    sha256 = (hex(int(h0, base=2))[2:] +
              hex(int(h1, base=2))[2:] +
              hex(int(h2, base=2))[2:] +
              hex(int(h3, base=2))[2:] +
              hex(int(h4, base=2))[2:] +
              hex(int(h5, base=2))[2:] +
              hex(int(h6, base=2))[2:] +
              hex(int(h7, base=2))[2:])
    return sha256
