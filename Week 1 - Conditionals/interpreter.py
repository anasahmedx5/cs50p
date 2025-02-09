def main():
    exp = input("Expression: ").strip()
    solve(exp)

def solve(exp):
    x, y, z = exp.split()
    x = float(x)
    z = float(z)

    match y:
        case "+":
            print(x+z)
        case "-":
            print(x-z)
        case "*":
            print(x*z)
        case "/":
            print(x/z)
        case _:
            print("Error")


main()
