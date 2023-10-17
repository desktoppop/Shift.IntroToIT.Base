#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def counting_vowels(string_0):
    return sum(1 for symbol_t in string_0 if symbol_t.lower() in "аеёиоуыэюя")
string_hi = "Привет, мир!"
print(f"В '{string_hi}' {counting_vowels(string_hi)} гласных")
