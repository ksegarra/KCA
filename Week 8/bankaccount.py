from random import randrange
from collections import defaultdict
from collections import namedtuple

bankaccount = namedtuple("bankaccount", ["owner_name", "branch", "bank_name", "balance"])


banks = ['Bank of America', 'US Bank', 'Chase', 'Wells Fargo']
cities = ['Irvine', 'Los Angeles', 'Aliso Viejo', 'Anaheim', 'Orange', 'Newport Beach']

def generate_bank_accounts(names_file: str) -> [bankaccount]:
    ba_list = []
    with open(names_file, 'r') as buf:
        for line in buf:
            name = line.rstrip()
            ba_list.append(bankaccount(name, random_index(cities), random_index(banks), generate_acct_bal()))
    return ba_list


def random_index(indexable):
    return indexable[randrange(0, len(indexable))]
        

def generate_acct_bal()->int:
    balance = 0
    for i in range(9):
        balance += randrange(0, 600)
    return balance

def histogram(l_data: [(str, int)]):
    for s,d in l_data:
        print('{}: {}'.format(s, ((d//100)*'*'if d > 100 else '*')))

def make_bal_dict()->dict:
    d = defaultdict(int)
    for i in range(10000):
        bal = generate_acct_bal()
        if bal <= 500:
            d['500'] += 1
        elif 1000 >= bal < 500:
            d['1000'] += 1
        elif 1500 >= bal < 1000:
            d['1500'] += 1
        elif 2000 >= bal < 1500:
            d['2000'] += 1
        elif 2500 >= bal < 2000:
            d['2500'] += 1
        elif 3000 >= bal < 2500:
            d['3000'] += 1
        elif 3500 >= bal < 3000:
            d['3500'] += 1
        elif 4000 >= bal < 3500:
            d['4000'] += 1
        elif 4500 >= bal < 4000:
            d['4500'] += 1
        else:
            d['5000'] += 1
    return d

def main():
    #histogram(sorted(make_bal_dict().items(), key = lambda d:int(d[0])))
    l = generate_bank_accounts("names.txt")
    print(l)

main()
