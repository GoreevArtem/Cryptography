Основы криптографических методов 

##  1. Потоковые шифры [^1]
Реализация потокового кода шифрования __RC4__ [^2]
#### Тестовый пример
Ключ (ASCII) | Открытый текст |Шифртекст 
:-----|:------|:----
hello   | world     | x>═Ц╧
nngy | russia   | ∙+У+
---
[^1]: [потоковые шифры](https://ru.wikipedia.org/wiki/Потоковый_шифр)
[^2]: [RC4](https://en.wikipedia.org/wiki/RC4)


## 2. Задача о рюкзаке Merkle-Hellman
Задача о рюкзаке (или Задача о ранце) в криптографии (англ. Knapsack problem) — это задача,
на основе которой американские криптографы Ральф Меркл и Мартин Хеллман разработали первый
алгоритм шифрования с открытым ключом. Он носит название криптосистема Меркла-Хеллмана.
Для шифрования сообщений использовалось решение задачи о рюкзаке, как известно, являющейся
NP-сложной. Потому, как считалось, она могла обеспечивать криптостойкость системы.
На данный момент создано множество рюкзачных криптосистем. Однако практически все существующие
на сегодняшний день взломаны или признаны потенциально небезопасными.


## 3. SHA
Secure Hash Algorithm 1 — алгоритм криптографического хеширования. Описан в RFC 3174.
Для входного сообщения произвольной длины примерно 2 эксабайта. Алгоритм генерирует 160-битное
(20 байт) хеш-значение, называемое также дайджестом сообщения, которое обычно отображается как
шестнадцатеричное число длиной в 40 цифр. Используется во многих криптографических приложениях
и протоколах. Также рекомендован в качестве основного для государственных учреждений в США.
Принципы, положенные в основу SHA-1, аналогичны тем, которые использовались Рональдом Ривестом
при проектировании MD4.


## 4. Эцп Эль-Гамаля
Схема Эль-Гамаля — криптосистема с открытым ключом, основанная на трудности вычисления дискретных
логарифмов в конечном поле. Криптосистема включает в себя алгоритм шифрования и алгоритм цифровой
подписи. Схема Эль-Гамаля лежит в основе бывших стандартов электронной цифровой подписи в США (DSA)
и России (ГОСТ Р 34.10-94).


## 5. Стеганография в цифровых изображениях
Стеганография в цифровых изображениях — раздел стеганографии, изучающий проблему сокрытия данных
в цифровых изображениях. В отличие от криптографии, задача стеганографии — скрыть сам факт наличия
скрытого сообщения. Основные методы сокрытия информации в цифровых изображениях можно разделить на
пространственные и частотные.

Задача стеганографии в изображениях — встроить информацию в цифровое изображение так, чтобы
и сообщение, и сам факт его наличия были скрыты. Полученное изображение с дополнительной скрытой
информацией не должно выглядеть аномальным. Это достигается путём внесения изменений, незаметных
для человеческого зрения. Многие методы стеганографии
используют методики, схожие с методами сжатия изображений.
