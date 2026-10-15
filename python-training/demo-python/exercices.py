a = 5
b = 7

tmp = a
a = b
b = tmp

print('a = ', a)
print('b = ', b)

# OU

a = a + b # 13
b = a - b # 5
a = a - b # 8

# OU, asctuce Python
c = 8
d = 12
x, y, z = 10, 12, 15

c,d = d,c
print('c = ',c)
print('d = ',d)



# Afficher une information
print("Entrez vos informations")
nom = input('Entrez votre nom : ')
prenom = input('Entrez votre prénom : ')
age = input('Entrez votre age : ')

print(f"Bonjour vous êtes {nom} - {prenom}, vous avez {age} ans")
print(type(age))

# Conversion de valeurs
age_int = int(age)
print(type(age_int))
print(age_int + 1)

# Converstion de valeurs
value : str = "152.54"

#int()
value_int = int(value)

# float
value_float = float(value)

# bool
bool()
value_bool = bool(value)