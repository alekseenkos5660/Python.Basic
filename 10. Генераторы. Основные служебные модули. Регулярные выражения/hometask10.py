# import re
# # Написать валидации с помощью регулярных выражений:

# # - мобильный номер телефона (только цифры, возможное наличие плюса, длина номера)

# cell_list = ["0950000000", "1950000000", "80660000000", "380970000000", "+380930000000", "+480930000000"]

# # v1. Если номер состоит из 12 любых цифр и может быть записан с плюсом или без него

# for num in cell_list:
#     if re.match(r'^\+?\d{12}$', num):
#         print("valid")
#     else:
#         print("not valid")

# # v2. Если номер может быть записан в формате для звонка в Украину из-за рубежа (с +38) или
# # для звонка по Украине (без +38), а 0 — префикс выхода на линию другого оператора в пределах страны

# for num in cell_list:
#     if re.match(r'^(\+38)?0\d{9}$', num):
#         print("valid")
#     else:
#         print("not valid")

# # - домашний номер телефона (только цифры и длина номера)

# # представим что номер домашнего телефона состоит от 7 до 9 любых цифр в любой последовательности, тогда:

# home_list = ["1234567", "777 77 77", "123456789", "12345678", "1234567890"]

# for num in home_list:
#     if re.match(r'^\d{7,9}$', num):
#         print("valid")
#     else:
#         print("not valid")

# # - email (наличие @, домена: gmail.com например, минимальная длина и максимальная на ваш выбор)

# # Представим что имя пользователя может содержать:
# # буквы латинского алфавита (A-Za–z), цифры (0–9) точки (.), символ подчеркивания (_) и дефис (-)

# mail_list = [input("Enter your mail: ")]

# for mail in mail_list:
#     if re.match(r'^[-.\w]{5,20}@[a-z]{2,5}\.[a-z]{2,3}$', mail):
#         print("valid")
#     else:
#         print("not valid")

# # - ФИО клиента (3 слова, минимальная длина 2 символа, максимальная длина 20)

# # Представим что нам нужно записать имя клиента через пробел, при этом имя, фамилия и отчество должно обязательно
# # начинаться с большой буквы

# full_name = [input("Enter your Full Name: ")]

# for name in full_name:
#     if re.match(r'^[A_Z]{1}[a-z]{1,19}\s[A_Z]{1}[a-z]{1,19}\s[A_Z]{1}[a-z]{1,19}$', name):
#         print("valid")
#     else:
#         print("not valid")

# # дополнительно:

# # - Пароль (минимально: одна большая буква, одна маленькая буква, одна цифра, один символ,
# # длина пароля - от 8 до 16 символов)

# # Чтобы не перечислять все спецсимволы, представим что в пароле
# # могут быть только следующие спецсимволы: _.!#-

# # Для написания этой валидации нам нужно воспользоваться позиционной проверкой в регулярных выражениях. 
# # Она сопоставляет символы без указания конкретных совпадений. Вместо этого возвращается двоичный результат о наличии 
# # или отсутствии совпадения.
# # Воспользуемся позитивной опережающей проверкой, которая проводится с использованием в строке символов ?=

# password_list = [input("Enter password: ")]

# for password in password_list:
#   if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[_.!#-])[A-Za-z\d_.!#-]{8,16}$', password):
#     print("valid")
#   else:
#     print("not valid")
