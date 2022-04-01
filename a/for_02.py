
#-----------------------------------------------------------------------------------------
print("Escribe tu nombre")
a: list[str] = []

name1: str = input()
a.append(name1)
name2: str = input()
a.append(name2)
name3: str = input()
a.append(name3)
reverse_a: list[str] = list(reversed(a))
for name in reverse_a: 
    print(f"hello {name}")