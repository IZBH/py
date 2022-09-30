if 0:
    my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
    print(my_cat['size'])

    # 字典无序
    spam = ['cats', 'dogs', 'moose']
    bacon = ['dogs', 'moose', 'cats']
    print(spam == bacon)

    eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
    ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
    print(eggs == ham)

    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Caro1': 'Mar 4'}

if 0:
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

if 0:
    spam = {'color': 'red', 'age': 42}
    for v in spam.values():
        print(v)

    for k in spam.keys():
        print(k)

    for i in spam.items():
        print(i)

    spam = {'color': 'red', 'age': 42}
    print(spam.keys())
    print(list(spam.keys()))

    for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))

    spam = {'name': 'Zophie', 'age': 7}
    print('name' in spam.keys())

    print('Zophie' in spam.values())

    print('color' in spam.keys())

    print('color' not in spam.keys())

    print('color' in spam)

# 设置默认值
spam = {'name': 'Pooka', 'age': 5}
print(spam)
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

spam = {'name': 'Pooka', 'age': 5}
print(spam)
print(spam.setdefault('color', 'black'))
print(spam)
# spam字典包含'color'键
print(spam.setdefault('color', 'white'))
print(spam)



























