myList = [n for n in range(0, 100) if n % 2 == 0]

print(f"myList: {myList}")

myDict = {'nome': 'Carlo', 'cognome': 'Monaco'}
for x in myDict:
    print(f"Chiave {x}")

for x in myDict.values():
    print(f"Valore {x}")

for x in myDict.items():
    print(f"{x} {type(x)}")

r = {}
for k, v in myDict.items():
    print(f"{k} : {v}")
    r[f"myApp_{k}"] = v.upper()

print(f"r = {r}")


#forma breve
l = [x for x in range(2, 10)]
print(l)

#forma verbosa
l=[]
for x in range(2,10):
    l.append(x)
print(l)


#forma breve
l = [x for x in range(2, 10) if x % 2 == 0]
print(l)

#forma semiverbosa
l=[]
for x in range(2, 10, 2):
    l.append(x)
print(l)

#forma verbosa
l=[]
for x in range(2, 10):
    if x % 2 == 0:
        l.append(x)
print(l)

l = range(1, 10)
l2 = [x*2 if x % 2 == 0 else 'dispari' for x in l]
print(l2)


s = 'ciao ragazzi belli!'
d = {k: ord(k) for k in s}
print(d)

d = {k: k.upper() for k in s}
print(d)

d = {k.upper() for k in s if k != ' '}
print(d)


arr = ['ciao', 'mondo', 'meraviglioso']

for elem in arr:
    print(f"{elem} {type(elem)}")


for x in enumerate(arr):
    print(f"{x} {type(x)}")


for idx, val in enumerate(arr):
    print(f"{val} in indice {idx}")