from Merkle_Hellman import *


# Сверхвозрастающая последовательность
# закрытый ключ
ls = [2,3,6,13,27,52]
print(ls)

m = m_generate(ls)  # больше суммы чисел всей последовательности
n = n_generate(m)  # взаимно простое число с m

print("m = ",m ,"\nn = ", n)

res = []  # нормальная последовательность
# открытый ключ
for i in ls:
    res.append(i * n % m)
print("Нормальная последовательность ", res)

bin_mes = text_to_bits(input('Введите текст сообщения '))
print("Бинарный вид сообщения\n", bin_mes)

s = encryption(bin_mes, res)
print("Шифртекстом будет последовательность\n", s)

bin_mes = decryption(n, m, s, ls)
print("Бинарный вид сообщения\n", bin_mes)

mes = text_from_bits(bin_mes[:(len(bin_mes) // 8) * 8])
print(mes)