#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def counting_words(text):
    return len(text.split())
text = "Python прекрасен!"
print(f"В '{text}' {counting_words(text)} слов")
