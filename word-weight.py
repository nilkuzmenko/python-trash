#Вес слов. Тяжесть буквы растет с приближением к концу алфавита.

ext = input("Введите свой русский текст: ").lower()

abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
word = []
for i in text:
    if i not in """ '"[]\;.,!@#:$%^&*()_+-=1234567890""":
        word.append(abc.index(i) + 1)
    else:
        if word != []:
            print(sum(word), end=' ')
        word = []

print(sum(word), end=' ')
