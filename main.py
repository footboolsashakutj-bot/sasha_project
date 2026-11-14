from dice_stats import *
n = int(input("Enter the number of rolls: "))
element = [0] * 7
result = simulate_rolls(n)
for i in result:
    element[i] += 1
for i in range(1,7):
    print(f"{i}: выпал {element[i]} раз")











