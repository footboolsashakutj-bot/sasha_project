
import artith_tasks
g, otvet = artith_tasks.generate_task()
g0 = g[0]
g1 = g[1]
g2 = g[2]
print(g0, g1, g2)
x = int(input("Enter a number: "))
if x == otvet:
    print('Правильно')
else:
    print(f'Неправильно, правильный ответ: {otvet}')











