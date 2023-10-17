#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def it_palindrome(text):
    return text == text[::-1]
text = "радар"
print(f"Является ли '{text}' палиндромом? {it_palindrome(text)}")
