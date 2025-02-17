import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        if not (sys.argv[1].endswith(".py")):
            sys.exit("Not a Python file")

        lines = 0
        with open(sys.argv[1], "r") as file:
                for line in file:
                     strippedLine = line.strip()
                     if strippedLine.startswith("#") or strippedLine == "":
                        continue
                     lines += 1
        print(lines)

    except FileNotFoundError:
        sys.exit("File does not exist")


