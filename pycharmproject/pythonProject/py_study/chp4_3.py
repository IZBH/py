def list2str(para_list):
    str_list = ''
    for i in range(len(para_list)):
        if i < len(para_list) - 1:
            str_list += spam[i] + ', '
        else:
            str_list += 'and ' + spam[i]
    return str_list


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    str_spam = list2str(spam)
    print(str_spam)
