from functools import reduce

x = [
    {
        'a': 3,
        'b': 'ciao'
    },
    {
        'a': 2,
        'b': 'bye'
    }
]


def get_key_a(x):
    return x['a']



x.sort(key=get_key_a)
print(x)

# def get_key_b(x):
#     return ord(x['b'])
# x.sort(key=get_key_b)
# print(x)

x.sort(key=lambda x:x['a'], reverse=True)
print(x)

def increment(elem):
    return elem+1

print(type(increment)) #class function



l = [1,2,3,4]
for i in l:
    print(i)

mapped = list(map(increment, l))
print(f"{mapped} {type(mapped)}")

print([item for item in mapped])
print([item for item in map(increment, l)])


def dispari(x):
    return x % 2 != 0

print([i for i in filter(dispari,l)])

# sezione reduce
print(f"stampa inline di reduce: {reduce(lambda x, y: x * y, l)}")


def prodotto(x, y):
    return x*y

print(f"stampa con function di reduce: {reduce(prodotto, l)}")

''' 
esercizio 
massimo e minimo 
1- con ciclo
2 con reduce

'''

# massimo e minimo con cicli

def massimo(list):
    if list:
        maxValue = list[0]
        for i in list:
            if i > maxValue:
                maxValue = i
    else:
        maxValue = None
    return maxValue


def minimo(list):
    if list:
        minValue = list[0]
        for i in list:
            if i < minValue:
                minValue = i
    else:
        minValue = None
    return minValue

print(f"Determinazione di massimo e minimo con funzioni:\nil minimo di {l} è {minimo(l)}\nil massimo di {l} è {massimo(l)}")


# massimo e minimo con reduce



print(f"Determinazione di massimo e minimo con reduce:\n"
      f"il minimo di {l} è {reduce(lambda x,y: x if x < y else y,l)}\n"
      f"il massimo di {l} è {reduce(lambda x,y: x if x > y else y,l)}")


increment = 'fine'
print(f"{increment} {type(increment)}")
