# elifs, arithmetic, comparison, casting


def main():
    while True:
        print(11, "*", 11)
        i = int(input())

        # CASE 1: answer is correct

        if i ==  11*11:
            print("We both have enough money to buy a brain")
            break

        # CASE 2: answer is too big

        elif i > 11*11:
            print("Too big, buddy")

        # CASE 3: answer is too small

    ##    elif i < 11*11:
    ##        print("Too small, buddy")

        else:
            print("Go to school!!!!, its to small")
    
main()
