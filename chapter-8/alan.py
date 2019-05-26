alan = {
    'age': 18,
    'sex': 'male'
}

ben = {
    'age': 18,
    'sex': 'male'
}

zhuang = alan

print(id(zhuang) == id(alan))

print(id(alan) != id(ben))

print(alan == ben)

zhuang['money'] = 0

print(alan) # {'age': 18, 'sex': 'male', 'money': 0}

