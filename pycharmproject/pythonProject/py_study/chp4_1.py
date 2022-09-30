import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

name = 'Zophie'
print(name[0])
print('Zo' in name)
print('z' in name)

for i in name:
    print('* * * ' + i + ' * * *')

# 字符串不可变
name = 'Zophie a cat'
try:
    name[7] = 't'
except TypeError:
    print('You can not change a string')

newName = name[0:7] + 'the' + name[8:12]
print(newName)

# del 和 append 真正修改列表
# 其他只是给列表名赋值新的列表
# 类似指针指向新数组

print(tuple['cat', 'dog', 5])
print(list(('cat', 'dog', 5)))
print(list('hello'))

# 列表赋值传递的是引用，而非值
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)


def eggs(some_parmeter):
    some_parmeter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)
