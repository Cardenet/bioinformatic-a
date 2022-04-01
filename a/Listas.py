#Tutoeial 3.1.3 Listas
import pprint 
import random
import copy

l1: list = [] #Lista vacia

l2: list [str] = ["jonny" , "Maria", "Lucy"]

l2_len: int = len(l2)



print(l2 [0])
print(l2 [2])
print(l2 [2][0]) #"Lucy" [0] la L
#Sublistas
l3: list[str] = ["a", "b", "c", "d", "e", "f"]
print(l3[0:4]) #a b c d
print(l3[4:6]) #c,f
print(l3[4:])  # c, f mejor forma

#operaciones de listas
print(["jonny","Willyrex","Lolito"] + ["Peter", "Vegetta", "Osas"])
print([1, 2, 3] * 3)
l4: list[object] = print([1, "jonny", True, 0.9])
l5: list[list[int]] = [[1,2],[3,4]]
print(f"{l5[0]}\n{l5[1]}")
firts_row = l5[0]
second_row =l5[1]
print(f"{firts_row}\n{second_row}")

#Tutorial 5,1 "More en list"
#Pure fuction (libreta)vs Impures
#Example: Failure condition
#Pure
#1
a=1
def do_something_v1():
    print(a)
def do_something_v2():
    b= input()
    print (b)
#2
l6: list[int] = [1, 2, 3]
l6.append(4)
#3
def do_something_v3():
    return random.randint (1, 10)
do_something_v3()
#Search
l5: list[str] = ["a", "b", "c", "d"]
print(l5.index("c"))
#cOUNT
l5: list[str] = ["a", "b","b", "c","c","c", "d"]
print(l5.count("c"))
#Sorted esta en pasado pq la normal es impura (.sort)
l5: list[int] = [4,2,1,3]
l5_sorted: list[int] = sorted(l5)
print(l5_sorted)
l5_sorted: list[int] = sorted(l5, reverse=True)
print(l5_sorted)
#Reversed esta en pasado pq la normal es impura (.reverse)
l5: list[int]= [4,3,2,1]
l5_reversed:list [int] = list(reversed(l5))
print(l5_reversed)


#Impure
#Las listas son "mutables"
l3[0] = "z"
l3[0] = "a"
print(l3)
#Slice assigments
l3[3:] = [1,2,3] # d ,e , f ->1,2,3
l3[3:] = ["d"]
l3[3:] = []
l3[:]  = []
print(l3)
#Append 
l3: list[int] = [1,2,3,4,5]
l3_methods: list[str] =dir(l3)
pprint.pp(l3_methods)

l3.append(6)
print(l3)
result = l3.append(6)
print(result)
#Extend 
l6: list[int] = [1,2,3]
l7: list[int] = [4,5,6]
l8: list[int] = l6 + l7#Pure, no cambia ninguna de las 2
l6.extend(l7)# Impure, cambia l6
print(l6)
#Insert
l6.insert(0, 10)
l6.insert(len(l6), 10)
print(l6)
#Remove
l6: list[str] = ["a", "b", "c"]
l6.remove("b")
print(l6)
l6.pop(1)
print(l6)
#"del" Keyword, is not a fuction, after "del" there are no brackets
#"del" means delete, can delete anything
l6: list[str] = ["a", "b", "c","d"]
del l6[1] #Delete the whole list
print(l6)
del l6 # TAMBIEN SE PUEDE HACER ASI:
del l6[:]
print(l6)
#Clear
l6: list[str] = ["a", "b", "c","d"]
l6.clear()
#Copy
l6: list[int] = [1,2,3]
l7: list[int] = copy.copy(l6)
#---------------------------------------------------------------------------------------------------------

