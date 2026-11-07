import random
a = ''
x = int(input('Enter a number: '))
for i in range(x):
    a += str(random.randint(0,9))
print(a)



