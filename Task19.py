# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

print()
import itertools
def compress(text):
    for char, same in itertools.groupby(text):
        count = sum(1 for _ in same)
        yield str(count)+char

def unCompress(rle):
    decode = ''
    count = ''
    for i in rle:
        if i.isdigit():
            count += i
        else:
            decode += i * int(count)
            count = ''
    return decode

s = input('Enter: ')
s1 = ''.join(compress(s))
print(s1)
s2 = unCompress(s1)
print(s2)