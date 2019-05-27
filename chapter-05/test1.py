def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


map_1 = list(map(fact, range(5)))
print(map_1)
map_2 = [fact(n) for n in range(5)]
print(map_2)

filter_1 = list(map(fact, filter(lambda x: x % 2, range(6))))
print(filter_1)
filter_2 = [fact(n) for n in range(6) if n % 2]
print(filter_2)
