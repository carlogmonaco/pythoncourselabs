
'''
Copyright 2021-2022 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

x = int(input("Inserire un intero per verificare la sua relazione con 0\nx = ")) #input è una funzione di input con il tipo di dato

# print(x > 0)
# print(x < 0)
# print(x == 0)
# print(x != 0)
# print(x >= 0)
# print(x <= 0)

# ToDo: Use if statements to make more detailed prints.
if x > 0:
    print(f"{x} > 0 : {x>0}")
if x < 0:
    print(f"{x} < 0 : {x < 0}")
if x == 0:
    print(f"{x} == 0 : {x == 0}")
if x != 0:
    print(f"{x} != 0 : {x != 0}")
if x >= 0:
    print(f"{x} >= 0 : {x >= 0}")



# ToDo: Check if x in in one of the following intervals: [-2, 5], (10, 100], (200, 300)

I1 = (-2 <= x <= 5)
I2 = (10 < x <= 100)
I3 = (200 < x < 300)

if I1 or I2 or I3:
    print(f"{x} è in uno dei tre intervalli")
    if I1:
        print(f"{x} è nell'intervallo [-2,5]: {I1}")
    if I2:
        print(f"{x} è nell'intervallo (-10,100]: {I2}")
    if I3:
        print(f"{x} è nell'intervallo (-200,300): {I3}")
else:
    print(f"{x} non rientra negli intervalli specificati")

s = 'sciao sciao'
print(s.title())