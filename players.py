# -*-coding = utf-8-*-
#!python切片
players = ['shuting', 'chunxiang', 'zhaoxia', 'wangmiao', 'furong']

#从下标为0的元素开始3-0=3位
print(players[0:3])
#从下标1开始的4-1=3位
print(players[1:4])
#没有起始索引时，自动从0开始
print(players[:3])
#没有结束索引，自动到结尾
print(players[2:])
#输出列表最后三位
print(players[-3:])

#循环输出
for player in players[-3:]:
    print(player.title())

#复制列表
my_wifes = players[:]
print('My players are:')
print(players)
print('\nMy wifes are:')
print(my_wifes)
#两个列表增加一个不同的元素
my_wifes.append('xiaofeng')
players.append('zhangjuan')

print(my_wifes)
print(players)

#不使用切片,相当于将两个列表关联，更改一个另一个生效
my_wifes = players
print(my_wifes)
print(players)

my_wifes.append('yamei')
players.append('yali')

print(my_wifes)
print(players)
