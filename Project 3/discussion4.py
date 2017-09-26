"I'm in the club when they play the competition if they play the competition then I see the response they get"
from functools import reduce
import math


adders = []
for n in range(5):
    adders.append(lambda m: m+n)

print(adders)
x = [adder(10) for adder in adders]
print(x)
print(n)
n = 50
y = [adder(10) for adder in adders]
print(y)



#List of ints
#
#list_of_ints ::= empty_list
#list_of_ints ::= int + list_of_ints

def empty_list_of_ints():
    return []

def list_of_ints(n, lst_of_ints):
    return [n] + lst_of_ints

def remove(n, lst_ints):
    if(len(lst_ints) == 0):
        return []
    f = lst_ints[0]
    if(f != n):
        list_of_ints(f, remove(n, lst_ints[1:]))
    else:
        return lst_ints[1:]
