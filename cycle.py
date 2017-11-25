""" task 4 """
#!coding: utf-8

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

while names:
    if names.pop() == 'Валера':
        print('Валера нашелся!')
    else:
        continue


def find_person(name):
    """ Find person """
    names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    while names:
        if names.pop() == name:
            return '{} найден(а)'.format(name)
    return 'Не нашлось человека с таким именем в списке.'

print(find_person('Маша'))


def get_anwser():
    """ Get answer """
    while True:
        user_input = input('Введите вопрос:').capitalize()
        if user_input == 'Как погода?':
            print('Холодно')
        elif user_input == 'Как настроение?':
            print('Хорошее')
        elif user_input == 'Пока':
            print('Пока!')
            break

def ask_user():
    """ Ask user """
    while True:
        user_input = input('Как дела? : ').capitalize()
        if user_input == 'Хорошо':
            break
        continue
    try:
        get_anwser()
    except KeyboardInterrupt:
        print('\nПока!')

try:
    ask_user()
except KeyboardInterrupt:
    print('\nПока!')
