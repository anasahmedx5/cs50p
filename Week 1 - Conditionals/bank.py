def main():
    greeting = input("Greeting: ").strip().lower()
    money(greeting)


def money(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")



main()
