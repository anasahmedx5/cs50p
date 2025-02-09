def main():
    user_input = input("What time is it? ")
    time = convert(user_input)

    if 7<= time <= 8:
        print("breakfast time")
    elif 12<= time <=13:
        print("lunch time")
    elif 18<= time <=19:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")

    hour = float(hour)
    minutes = float(minutes)

    time = hour + (minutes/60)

    return time

if __name__ == "__main__":
    main()
