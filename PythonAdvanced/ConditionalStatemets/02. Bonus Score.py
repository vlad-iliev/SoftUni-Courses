number = int(input())
bonus = 0
if number <= 100:
    bonus = bonus + 5
elif 100 < number < 1000:
    bonus = bonus + (number * 0.20)
elif number > 1000:
    bonus = bonus + (number * 0.10)

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + number)
