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
    user_search = input('Введите фамилию: ')
    try:
        if user_search =='' or user_search.isdigit():
            print('Ошибка ввода')
            return data_search()
        else:
            return user_search    
    except ValueError:
        print('Ошибка ввода')
        error_enter()
        return data_search()

def key_choice():
    my_choice = input()
    try:
        my_choice = int(my_choice)
        return my_choice
    except ValueError:
        print('Ошибка ввода')
        error_enter()
        return  key_choice()
