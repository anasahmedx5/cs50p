import os
import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command_line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command_line arguments")
    else:
        try:
            extensions = ('.jpg', '.jpeg', '.png')

            input = sys.argv[1]
            output = sys.argv[2]

            if not input.lower().endswith(extensions) or not output.lower().endswith(extensions):
                sys.exit("Invalid input")

            if os.path.splitext(input)[1].lower() != os.path.splitext(output)[1].lower():
                sys.exit("Input and output have different extensions")

            shirt = Image.open("shirt.png")
            with Image.open(input) as input:
                shirtOn = ImageOps.fit(input, shirt.size)
                shirtOn.paste(shirt, mask=shirt)
                shirtOn.save(output)

        except FileNotFoundError:
            sys.exit("File not found")




if __name__ == "__main__":
    main()
