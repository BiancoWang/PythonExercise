# coding=utf-8
favorite_languages = {
    'jen':'python',
    'sarch':'c',
    'edward':'ruby',
    'phil':'php',
}
print("Sarch's favorite lnguage is " +
    favorite_languages['sarch'].title() +
    '.')
#函数items()遍历键-值
for name, language in favorite_languages.items():
    print(name.title() + ' is favorite language is ' +
    language.title())
print('\n')
#函数keys() 遍历键,再用sorted（）临时排序
for key in sorted(favorite_languages.keys()):
    print(key.title() + ' hei hei')
print('\n')
#函数keys()也可省略
for key in favorite_languages:
    print(key.title() + ' hei hei')
print('\n')
#可以用键显示对应的值
friends = ['jen', 'phil']
for name in favorite_languages.keys():
#    print(name.title())
    if name in friends:
        print(name.title() + ' is favorite language is ' +
        favorite_languages[name].title())
#values()遍历其中的值
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

#集合set()；set（）中的值都是独一无二的，可用来避免重复
for language in set(favorite_languages.values()):
    print(language.title())