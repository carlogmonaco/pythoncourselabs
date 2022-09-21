
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

x = 1
y = 2
z = 3

x = int(input("inserire un intero per verificare se sia pari a 0\n x = "))
if x != 0:
    print(f"x = {x} is not 0")
y = int(input("inserire un intero per ferificare se sia o non sia 0\n y = "))
if y == 0:
    print(f"y = {y} is 0")
else:
    print(f"y = {y} is not 0")
z = int(input("inserire un intero per verificarlo rispetto a 0\n z = "))
if z == 0:
    print(f"z={z} is 0")
elif z > 0:
    print(f"z={z} is greater then 0")
else:
    print(f"z={z} is smaller then 100")
print("fine!")