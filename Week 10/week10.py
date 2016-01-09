from collections import namedtuple

fraction = namedtuple("fraction", "num denom")

def print_fraction(frac):
    print(frac.num, "/", frac.denom)
    
f = fraction(1, 2)
f1 = fraction(3, 4)
##print_fraction(f)
##print_fraction(f1)

def add_fracs(frac1, frac2):
    new_num = frac1.num + frac2.num
    return fraction(new_num, frac1.denom)

def main():
    while True:
        frac_1 = fraction(8,19)
        frac_2 = fraction(5,19)
        print_fraction(frac_1)
        print('+', end = '')
        print_fraction(frac_2)

        ans = add_fracs(frac_1, frac_2)
        num = input("what is the numerator")
        denom = input("what is the denomator")
        input_answer = fraction(num, denom)

        if input_answer.num == ans.num:
            print("correct")
            break
        else:
            print("bad")
        
        
        
main()
        
    
##r1 = add_fracs(f, f)
##r2 = add_fracs(f1, f1)
##
##print_fraction(r1)
##print_fraction(r2)

r3 = add_fracs(f, f1)
print_fraction(r3)


