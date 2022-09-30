import copy

# 值传递
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)
# 列表中包含列表时使用 deepcopy,同时拷贝列表
