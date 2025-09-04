name = input("Hola como te llamas?")

print(f"Hello world, {name}")

edad = input("Qué edad tienes?")

print(f"Tienes {edad}")
edadInt = int(edad)
if edadInt >= 18:
    print(f"Excelente {name} eres mayor de edad y estas creando tu primer programa en python")
else:
    print("Necesitas ser mayor de edad")