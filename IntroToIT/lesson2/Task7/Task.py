#INTRO TO IT 2nd COURSE
# Задача 7: Факториал на месте!
# Рассчитай факториал введенного числа.
def factorial(integer_t):
    return 1 if integer_t == 0 else integer_t * factorial(integer_t-1)
count = 5
print(f"Факториал {count} равен {factorial(count)}")
