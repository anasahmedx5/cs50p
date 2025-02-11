def main():
    percentage = getFraction("Fraction: ")
    printPercentage(percentage)


def getFraction(prompt):
    while True:
        try:
            fraction = str(input(prompt))

            x, z = fraction.split("/")
            x = int(x)
            z = int(z)

            if z == 0 or z<x:
                raise ZeroDivisionError

            total = round((x/z)*100)
            return total

        except (ValueError, ZeroDivisionError):
            pass


def printPercentage(percentage):
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


main()
