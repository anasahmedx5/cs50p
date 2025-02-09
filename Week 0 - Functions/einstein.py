def main():
    mass = int(input("M: "))
    energy = calculate(mass)
    print(energy)

def calculate(mass):
    energy = mass * 300000000**2
    return energy

main()
