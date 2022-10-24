from log import error_enter
from file_writing import last_key


def user_choice():
   choice1 = input('Выберите пункт меню: ')
    try:
        choice1  = int(choice1)
        return choice1 
    except ValueError:
        print('Ошибка ввода')
        error_enter()
        return user_choice()

def data_search():
    try:
        search = input('Введите данные для поиска контакта: ')
    except ValueError:
        print('Ошибка ввода')
        error_enter()
    return search

def key_choice():
    try:
        my_choice = int(input())
    except ValueError:
        print('Ошибка ввода')
        error_enter()
    return my_choice
