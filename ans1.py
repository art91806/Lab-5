import re

with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b(?=\.)', text)

num = re.findall(r'\b\d+\,\d+\b', text)

print("Слова перед точкой:")
print(words)

print("Числа:")
print(num)