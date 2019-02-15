diccionario = {1: 'hola',
                2: "mundo",
                3: "desde",
                "cuatro": "diccionario"}

print(type(diccionario))

print(diccionario)

for keys, value in diccionario.items():
    print(f"""llave{keys}:valor-{value}""")

persona = {}

persona["Nombre"] = "Ramón"
persona["Apellido"] = "Agramón"
persona["Edad"] = "22"

for datos, value in persona.items():
    print(f"""{datos} - {value}""")


persona["Correo"] = "ramonagramon2@gmail.com"

if "Correo" in persona:
    print(f"El correo es {persona['Correo']}")
else:
    print("no tiene correo")

if persona.get("altura") == None:
    persona["altura"] = "1.74mts"
    
print(persona.get("altura"))