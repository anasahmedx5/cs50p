import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command_line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command_line arguments")
    else:
        try:
            if not (sys.argv[1].endswith(".csv")):
                sys.exit("Not a CSV file")

            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
