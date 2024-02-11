# Задача №55 Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# План
# 1. Создание файла:
#     - открываем файл на дозапись # a

# 2. Добавление контакта:
#     - запросить у пользователя новый контакт
#     - открыть файл на дозапись # a
#     - добавить новый контакт 

# 3. Вывод данных на экран:
#     - открыть файл на чтение # r
#     - считать файл
#     - вывести на экран

# 4. Поиск контакта:
#     - выбор варианта поиска
#     - запросить данные для поиска
#     - открыть файл на чтение
#     - считываем данные файла, сохранить их в переменную
#     - осуществляем поиск контакта
#     - выводим на экран найденный контакта

# 5. Копирование контакта:
#     - открыть файл на чтение # r
#     - считать файл
#     - вывести на экран список контактов
#     - запросить у пользователя номер контакта для копирования
#     - создать и открыть новый файл (copy_phonebook) для сохранения копии контакта 
#     - скопировать указанный контакт

# 6. Создание UI:
#     - вывести меню на экран 
#     - запросить у пользавателя вариант действия
#     - запустить соответствующую функцию
#     - осуществить возможность выхода из программы

def create_contact():
    surname = input('Введите фамилию контакта: ').title()
    name = input('Введите имя контакта: ').title()
    patronymic = input('Введите отчество контакта: ').title()
    phone = input('Введите телефон контакта: ')
    address = input('Введите адрес(город) контакта: ').title()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'

def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='utf-8') as file: # открываем файл на дозапись - а, обращаемся к файловому дискриптору
        file.write(contact_str)
    
def print_contacts():
    with open("phonebook.txt", 'r', encoding='utf-8') as file: # открываем файл на чтение - r
        contacts_str = file.read() # в переменную сохраняем все контакты в виде строки (многострочной)
    
    contacts_list = contacts_str.rstrip().split('\n\n') # создаем из строки список, элементы которого являются контактами (разделенные между собой: \n\n)
    for n, contact in enumerate(contacts_list, 1): # (enumerate номирует элементы contacts_list начиная с 1) 
        print(n, contact) # выводим на экран все контакты пронумерованные
    
def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. По фамилии\n'
            '2. По имени\n'
            '3. По отчество\n'
            '4. По телефону\n'
            '5. По адресу(город)'
            )
    var = input('выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('некорректный ввод!')
        var = input('выберите вариант поиска: ')
    i_var = int(var) - 1   # получаем индекс нужного элемента
    
    search = input('Введите данные для поиска: ').title()
    with open("phonebook.txt", 'r', encoding='utf-8') as file: 
        contacts_str = file.read() 
    contacts_list = contacts_str.rstrip().split('\n\n')
    for str_contact in contacts_list:  
        lst_contact = str_contact.replace(':', '').split() # преобразуем каждый контакт в список из ф, и, о, тел. и города (заменяя : на пробел) сплитуя по пробелам
        if search in lst_contact[i_var]: # проверяем совпадение с элементом (имеющим нужный индекс) в lst_contact
            print(str_contact)

def copy_contact(): 
    with open("phonebook.txt", 'r', encoding='utf-8') as file: 
        contacts_str = file.read() 
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):  
        print(n, contact)  
    print()
    number_copy_contact = int(input("введите номер контакта для копирования: "))
    print()
    with open("copy_phonebook", 'a', encoding='utf-8') as file:
        file.write(f'{contacts_list[number_copy_contact-1]}\n')
    return

def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'): 
        pass
    var = 0
    while var != '5':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Копирование контакта\n'
            '5. Выход'
            )
        print()
        var = input('выберите вариант действия: ')
        while var not in ('1', '2', '3', '4','5'):
            print('некорректный ввод!')
            var = input('выберите вариант действия: ')
        print()    

        match var: 
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3': 
                search_contact()
            case '4':
                copy_contact()
            case '5':
                print('До свидания') 
        print()        


if __name__ == '__main__':
    interface()