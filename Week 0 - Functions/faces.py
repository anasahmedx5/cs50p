def main():
    user_inp = input()
    user_inp = convert(user_inp)
    print(user_inp)


def convert(user_inp):
    user_inp = user_inp.replace(":)","🙂")
    user_inp = user_inp.replace(":(","🙁")
    return user_inp

main()
