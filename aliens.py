# coding=utf-8

#创建三个外星人
alien_0 = {'color':'green', 'point':5}
alien_1 = {'color':'yellow', 'point':10}
alien_2 = {'color':'red', 'point':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#创建一个空列表
aliens = []
#创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color':'green', 'point':5, 'speed':'slow'}
    aliens.append(new_alien)
#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')

#显示创建了多少个外星人
print('Total number of aliens: ' + str(len(aliens)))
#修改前3个外星人
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = '10'

#再次显示前5个外星人
for alien in aliens[0:5]:
    print(alien)