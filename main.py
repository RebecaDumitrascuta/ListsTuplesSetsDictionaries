lista_cumparaturi = ["paine", "lapte", "unt", "legume", "fructe"]
print(lista_cumparaturi)
print(len(lista_cumparaturi))
print(lista_cumparaturi[-1])
print(lista_cumparaturi[0:2])
lista_cumparaturi.append("apa")
print(lista_cumparaturi)
lista_cumparaturi.insert(0, "cereale")
print(lista_cumparaturi)
lista_cumparaturi_noua = ["dulciuri", "suc"]
lista_cumparaturi.extend(lista_cumparaturi_noua)
print(lista_cumparaturi)
lista_cumparaturi.remove("dulciuri")
print(lista_cumparaturi)
lista_cumparaturi.reverse()
print(lista_cumparaturi)
lista_cumparaturi.sort()
print(lista_cumparaturi)
numbers = [1, 2, 3, 4, 5]
print(min(numbers))
print(max(numbers))
print(3 in lista_cumparaturi)
print(7 in lista_cumparaturi)
for x in enumerate(lista_cumparaturi):
    print(x)

# print(lista_cumparaturi)
print(lista_cumparaturi)

print(lista_cumparaturi[len(lista_cumparaturi) // 2])
print("-".join(lista_cumparaturi))
lista_cumparaturi_str = " - ".join(lista_cumparaturi)


tuplu=('apa', 'cereale', 'fructe', 'lapte', 'legume', 'paine', 'suc', 'unt')
print(tuplu)

setul_1= {"paine", "lapte", "unt", "legume", "fructe"}
print(setul_1)
setul_2= {"paine", "lapte", "unt", "legume","dulciuri", "suc"}
print(setul_2)

print(setul_1.intersection(setul_2))
print(setul_1.difference(setul_2))
print(setul_1.union(setul_2))

student = {"name": "Rebeca Groza", "age": 32, "courses": ["python", "linux"]}
print(student)
print(student.get("phone", "Not found"))
student["Phone"]= "0741567599"
print(student)
student.update({"name": "Rebeca Dumitrascuta", "age": 33})
print(student)
age = student.pop("age")
print(student)
print(age)
