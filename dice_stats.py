import random
def simulate_rolls(n):
    result = []
    for i in range(n):
        roll = random.randint(1, 6)
        result.append(roll)
    return result



