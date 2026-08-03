L1=[1,2,3]
L2=['first','second','third']

print(zip(L1,L2))
print(list(zip(L1,L2)))

days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
weathers = 'rainy rainy sunny cloudy rainy sunny sunny'.split()
temperatures = [10,12,12,9,9,11,11]

for day, weather, temperature in zip(days, weathers, temperatures):
    print(f"On {day} it was {weather} and the temperature was temperature was {temperature} degree celsius.")
