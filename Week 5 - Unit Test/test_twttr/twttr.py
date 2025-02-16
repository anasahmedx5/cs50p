def main():
    user_input = input("Input: ")
    user_output = shorten(user_input)
    print(f"Output: {user_output}")


def shorten(user_input):
    ommited = ""
    for char in user_input:
        if char.lower() in "aeiou":
            continue
        ommited += char
    return ommited


if __name__ == "__main__":
    main()
