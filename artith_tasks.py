import random
def generate_task():
    g = ( random.randint(1, 9), random.choice(['+','-','*','/']) ,random.randint(1, 9))
    if g[1] == '+':
        otvet = g[0] + g[2]
    elif g[1] == '-':
        otvet = g[0] - g[2]
    elif g[1] == '*':
        otvet = g[0] * g[2]
    elif g[1] == '/':
        otvet = g[0] / g[2]

    return g, otvet