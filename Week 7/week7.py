# namedtuple

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'hair_color', 'height', 'weight'])

my_class = [Person('Klint Segarra', 19, 'black', 70, 160),
            Person('Daniel Lo', 9, 'black', 56, 60),
            Person('Isaiah Renauld', 10, 'black', 58, 65),
            Person('Faris Hanna', 9, 'brown', 59, 60),
            Person('Jacob Kopp', 9, 'blonde', 58, 65)]

def main():
    people_with_blackhair = []
    for person in my_class:
        if person.hair_color == 'black':
            people_with_blackhair.append(person)

    for person in people_with_blackhair:
        print(person.name)

main()
    
