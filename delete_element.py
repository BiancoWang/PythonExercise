#-*-coding:utf-8-*-
#从列表中删除元素
motorcycles = ['BMW', 'Ducuti', 'Honda', 'Benali', "KTM"]
first = motorcycles[0]
#del删除需要知道元素位置
del motorcycles[0]
print(motorcycles)
print(first)
#将删除的元素重新添加
motorcycles.insert(0, first)
print(motorcycles)
len(motorcycles)

#pop()删除末尾元素(没有下标时)
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
motorcycles.insert(-1, poped_motorcycle)
print(motorcycles)
len(motorcycles)

#带下标的pop()
first_owned = motorcycles.pop(1)
print(motorcycles)
print('The first motorcycles I owned was a ' + first_owned + '.')
len(motorcycles)

#根据值删除元素remove()
motorcycles.remove('Ducuti')
print(motorcycles)
len(motorcycles)