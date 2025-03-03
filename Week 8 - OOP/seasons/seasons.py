from datetime import date
import inflect
import sys


def getMin(birth, today):
    return (today - birth).days * 24 * 60


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: ").strip())
    except ValueError:
        sys.exit("Invalid date")

    mins = getMin(birth, date.today())

    p = inflect.engine()
    words = p.number_to_words(mins, andword="").capitalize()

    print(f"{words} {p.plural('minute', mins)}")


if __name__ == "__main__":
    main()
