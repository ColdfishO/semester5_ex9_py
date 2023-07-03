# 1
import random
fo = open('liczby.txt', 'w')
for i in range(0, 20):
    liczba = str(random.randrange(1, 100))
    fo.write(liczba)
    fo.write(' ')
fo.close()

print('\n')
# 2
l = []
fo = open('liczby.txt', 'r')
char = ' '
s = ''
while char != '':
    char = fo.read(1)
    if char != ' ':
        s += char
    else:
        l.append(int(s))
        s = ''

fo.close()
print(l)

print('\n')
# 3
fo = open('plik.txt', 'w')
for i in range(0, 50):
    for j in range(0, 50):
        fo.write('*')
    fo.write('\n')
fo.close()
import random
fo = open('plik.txt', 'w')
for i in range(0, 50):
    for j in range(0, 50):
        if random.randrange(1, 5) == 1:
            fo.write('*')
        else:
            fo.write(' ')
    fo.write('\n')
fo.close()

print('\n')
# 4
fo = open('pierwsze.txt', 'w')
for i in range(2, 101):
    if i % 2 != 0 or i == 2:
        if i % 3 != 0 or i == 3:
            if i % 5 != 0 or i == 5:
                if i % 7 != 0 or i == 7:
                    fo.write(str(i))
                    fo.write(' ')
fo.close()

print('\n')
# 5
fo = open('pierwsze.txt', 'r')
s = fo.read()
s = s.split(' ')
print(s[-2])
fo.close()
fo = open('pierwsze.txt', 'a')
hund = 101
while hund <= int(s[-2]):
    hund += 100
for i in range(hund, hund+100):
    if i % 2 != 0 or i == 2:
        if i % 3 != 0 or i == 3:
            if i % 5 != 0 or i == 5:
                if i % 7 != 0 or i == 7:
                    fo.write(str(i))
                    fo.write(' ')
fo.close()

print('\n')
