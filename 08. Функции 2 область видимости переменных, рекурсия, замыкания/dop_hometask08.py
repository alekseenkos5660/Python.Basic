import random
# Напишите рекурсивную функцию, которая принимает одномерный массив из 100 целых чисел заполненных случайным образом 
#и находит позицию, с которой начинается последовательность из 10 чисел, сумма которых минимальна.

num = 100
list = []
for i in range(num):
  list.append(random.randint(1, 99))
print(list)

new_list = [] # новый список, который будет наполняться элементами через срабатывание рекурсивной функции, не придумал как 
#поместить его внутрь функции, еще подумаю над этим.


def min_sum_num(list, i=0, j=10):
  if list[i:j] == list[90::]: # условие окончания рекурсивной функции
    return new_list.append(sum(list[i:j])), print("Index:", new_list.index(min(new_list))) # после того как условие окончания рекурсии 
#будет выполнено, будет добавлен последний элемент списка и выведен на экран индекс минимального элемента списка new_list, 
#который соответствует индексу элемента списка list, с которого начинается последовательность из 10 чисел, сумма которых минимальна.
  new_list.append(sum(list[i:j])), min_sum_num(list, i+1, j+1) # запуск рекурсивной функции, ничего не возвращает, наполняет список.


min_sum_num(list)
