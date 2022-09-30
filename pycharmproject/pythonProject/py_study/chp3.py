# 关键字参数

# end
print('Hello')
print('World')

print('Hello', end='')
print('World')

# sep
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')


def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
print(eggs)
spam()
print(eggs)


def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
