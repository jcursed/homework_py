from functools import reduce

arr = input()
l = list(map(int, arr.split(' ')))

# Возведение в степень
def pow3(num):
    return num ** 3

nums = list(map(pow3, l))
print(nums)

#Фильтрация и сложение
nums = list(filter(lambda x: x != 0, l))
print(f'Сумма: {reduce(lambda x, y: x + y, nums)}')
