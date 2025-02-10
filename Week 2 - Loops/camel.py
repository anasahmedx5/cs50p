def main():
    user_input = input("camelCase: ")
    snake = snakeCase(user_input)
    print(f"snake_case: {snake}")

def snakeCase(user_inp):
    snake = ""
    for char in user_inp:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake


main()
