# modify multiplication program with lists, for loops, and zip function


list_values1 = [1,14,15,11,18,2,4,5,1024,3]
#list_values2 = [14,14,197,114,141114,5115,1515,1048,14,11]



def main():
    score = 0
    for v in list_values1:
        
        print(v, "*", 11)
        i = int(input())
        
        if i == v*11:
            print("We both have enough money to buy a brain")
            score = score + 1

        elif i > v*11:
            print("Too big, buddy")
            score = score - 1
        
        else:
            print("Go to school!!!!, its to small")
            score = score - 1
            
    print("Your score is", score)

main()
