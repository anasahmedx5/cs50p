def main():
    user_inp = input("File name: ").strip().lower()
    file(user_inp)


def file(user_inp):
    if user_inp.endswith(".gif"):
        print("image/gif")
    elif user_inp.endswith(".jpg") or user_inp.endswith(".jpeg"):
        print("image/jpeg")
    elif user_inp.endswith(".png"):
        print("image/png")
    elif user_inp.endswith(".pdf"):
        print("application/pdf")
    elif user_inp.endswith(".txt"):
        print("text/plain")
    elif user_inp.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
