import inflect

names = []

p = inflect.engine()

while True:
    try:
        name = input("Name: ").strip()
        if name:
            names.append(name)
    except EOFError:
        break

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")

else:
    print(f"Adieu, adieu, to {p.join(names)}")
