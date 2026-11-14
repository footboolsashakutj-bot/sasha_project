import random
posledovatelnost = []
count = 0
n = random.randint(1, 10)
for i in range(n):
    posledovatelnost.append(random.choice(['O', 'P']))
for g in posledovatelnost:
    if g == 'O':
        count += 1
print(posledovatelnost)
print(count)






