spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-3])

print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

a = [1, 2, 3] + ['A', 'B', 'C']
b = ['x', 'y', 'z'] * 3
print(a)
print(b)
del spam[2]
print(spam)

if 0:
    catNames = []
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) +
              ' (or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name]
    print('The cat names are:')
    for name in catNames:
        print(' ' + name)

ans = 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
print(ans)

spam = ['hello', 'hi', 'howdy', 'heyas']
print('howdy' not in spam)

if 0:
    myPets = ['Zophie', 'Pooka', 'Fat-tail']
    print('Enter a pet name:')
    name = input()
    if name not in myPets:
        print('I do not have a pet named ' + name)
    else:
        print(name + ' is my pet.')

cat = ['fat', 'black', 'loud']

size = cat[0]
color = cat[1]
disposition = cat[2]
print(size + ' ' + color + ' ' + disposition)

# 变量数目和列表长度必须严格相等
size, color, disposition = cat
print(size + ' ' + color + ' ' + disposition)

bacon = ['Zophie']
bacon *= 3
print(bacon)

spam = ['hello', 'hi', 'howdy', 'heyas', 'hi']
print(spam.index('hi'))
spam.append('moose')
print(spam)
spam.insert(1, 'chicken')
print(spam)
spam.remove('hi')
print(spam)

spam = [2, 5, 3.14, 1, -7]
# 顺序排序
spam.sort()
print(spam)
# 逆序排序
spam.sort(reverse=True)
print(spam)

# 字符串 ASCII 字符顺序排序
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
