import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command_line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command_line arguments")
    else:
        try:
            if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
                sys.exit("Not a CSV file")

            with open(sys.argv[1], "r") as before:
                reader = csv.DictReader(before)
                with open(sys.argv[2], "w") as after:
                    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for _ in reader:
                        last, first = _["name"].split(", ")
                        house = _["house"]
                        writer.writerow({"first": first, "last": last, "house": house})

        except FileNotFoundError:
            sys.exit("Could not read invalid_file.csv")


if __name__ == "__main__":
    main()
