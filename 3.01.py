# Глобальная переменная для подсчета вызовов
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция string_info
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция is_contains
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим строку и все элементы списка к одному регистру (например, нижнему)
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# Пример выполнения программы
print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False
print(calls)  # 4
