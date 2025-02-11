basket = {}

while True:

    try:
        item = input("").upper()
    except EOFError:
        break

    if item in basket:
        basket[item] += 1
    else:
        basket[item] = 1

for item, i in sorted(basket.items()):
    print(f"{i} {item}")

