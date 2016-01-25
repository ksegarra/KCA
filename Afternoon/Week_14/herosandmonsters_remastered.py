from random import randrange


# Heroes and Monsters: Remastered

class Hero:

    def __init__(self, h_name: str):

        self.name = h_name
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.atk_max = 5
        self.atk_min = 0
        self.mana = 0
        self.mana_cap = 100

    def attack(self):
        return randrange(self.atk_min, self.atk_max)

    def decrease_hp(self, d_hp: int):
        self.hp = self.hp - d_hp

    def increase_hp(self, d_hp: int):
        self.hp = self.hp + d_hp

    def level_up(self, max_lvlup: int, min_lvlup: int):
        assert max_lvlup + min_lvlup  <= 10
        
        self.atk_max = self.atk_max + max_lvlup
        self.atk_min = self.atk_min + min_lvlup

    def is_alive(self,):
        return self.hp > 0

class Monster:
    
    def __init__(self, m_name: str, lvl: int):

        self.name = m_name
        self.level = lvl
        self.hp = 10*lvl
        self.atk_max = lvl*2
        self.atk_min = 0
        self.exp_given = lvl/5

    def attack(self):
        return randrange(self.atk_min, self.atk_max)

    def decrease_hp(self, d_hp: int):
        self.hp = self.hp - d_hp

    def increase_hp(self, d_hp: int):
        self.hp = self.hp + d_hp

    def is_alive(self):
        return self.hp > 0

def print_hp(character):
    print('{} has {} hp left'.format(character.name, max(character.hp,0)))

def attack(attacker, attackee):
    strength = attacker.attack()
    attackee.decrease_hp(strength)
    attacker.mana += 5 # attacker.mana = attacker.mana + 5
    
    print('{} hits {} for {} damage'.format(attacker.name,
                                            attackee.name, strength))
    
    #print('{} has {} hp left'.format(attackee.name, max(attackee.hp,0))) # turn the
    print_hp(attackee)

        
def down_beast_mode(attacker, target):
    strength = attacker.attack() + int(.2(100-attacker.hp))
    attacker.mana -= 20
    target.decrease_hp(strength)

    print('{} has unleashed his/her inner beast.\
        It hits {} for {} damage'.format(
        attacker.name, target.name, strength))
    
    print_hp(target)    

def demacian_justice(attacker, target):
    strength = 3*attacker.atk_max
    outcome = randrange(4)
    
    if outcome <= 1:
        target.decrease_hp(strength)
        print('{} unleashes a different animal but the same beast upon\
        {} dealing {} damage'.format(attacker.name, target.name, strength))
        print_hp(target)
    elif outcome == 3:
        print('{} unleashes Demacian Justice, but nothing happened'.format(
            attacker.name))
    else:
        attacker.decrease_hp(attacker.hp//4)
        print('{} hits himself/herself with his/her sword for 1/4 his/her\
        health'.format(attacker.name))
        print_hp(attacker)
        
    attacker.mana -= 40

def heal(healer):
    pass

def hero_action(hero):
    '''Prints out menu for your hero to do something in a fight, 'h' for heal,
    'a' attack'''
    pass

def fight_turn(hero: Hero, monster: Monster):
    print('{} vs {}'.format(hero.name, monster.name))

    attack(monster, hero)
    if not hero.is_alive():
        print('you died')
    else:
        attack(hero, monster)

def main():
    h = Hero('Garen')
    m = Monster('goblin', 10)

    while (h.is_alive() and m.is_alive()):
        fight_turn(h, m)

main()
    


        
