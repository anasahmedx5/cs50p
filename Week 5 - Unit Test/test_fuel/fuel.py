def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction):
        x, z = fraction.split("/")
        if int(z) == 0:
            raise ZeroDivisionError
        if int(x) > int(z):
            raise ValueError

        return round((int(x)/int(z))*100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
