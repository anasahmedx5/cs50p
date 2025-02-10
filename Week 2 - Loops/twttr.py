def main():
    user_input = str(input("Input: "))
    user_output = ommitV(user_input)
    print(f"Output: {user_output}")


def ommitV(user_input):
    ommited = ""
    for char in user_input:
        if isVowel(char):
            ommited += ""
        else:
            ommited += char
    return ommited

def isVowel(char):
    return char.lower() in "aeiou"

main()
