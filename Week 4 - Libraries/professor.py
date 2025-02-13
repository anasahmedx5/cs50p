import random


def main():
    score = 0
    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += get_answer(x,y)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


def get_answer(x,y):
    count = 0
    while count < 3:
        try:
            count+=1
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return 1
            else:
                print("EEE")

        except ValueError:
            pass

    print(f"{x} + {y} = {x+y}")
    return 0


if __name__ == "__main__":
    main()
