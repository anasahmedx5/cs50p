def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate)<2 or len(plate)>6:
        return False

    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    for char in plate:
        if char == " " or char == ".":
            return False

    for i in range(len(plate)):
        if plate[i].isdigit():
            for j in range(i,len(plate)):
                if plate[j].isalpha() or plate[i] == "0":
                    return False
            break

    return True

if __name__ == "__main__":
    main()
