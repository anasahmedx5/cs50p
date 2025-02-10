def main():
    cokePrice = 50

    while cokePrice>0:
        while True:
            print(f"Amount Due: {cokePrice}")
            coin = int(input("Insert Coin: "))
            if coin == 5 or coin == 10 or coin == 25:
                break
        cokePrice = cokePrice-coin

    print(f"Change owed: {-cokePrice}")


main()
