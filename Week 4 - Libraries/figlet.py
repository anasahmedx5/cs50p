import sys
import random
from pyfiglet import Figlet

fonts = Figlet().getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print("Output: ")
print(Figlet(font=font).renderText(user_input))
