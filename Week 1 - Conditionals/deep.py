def main():
    user_inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    user_inp = str(user_inp)
    user_inp = user_inp.lower().strip()
    check(user_inp)


def check(user_inp):
    match user_inp:
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "forty two":
            print("Yes")
        case _:
            print("No")


main()
