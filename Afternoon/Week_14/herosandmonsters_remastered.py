from random import randrange

# Heros and Monsters: Remastered

class Hero:

    def __init__(h_name: str):

        self.name = h_name
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.atk_max = 5
        self.atk_min = 0

    def attack():
        return randrange(self.atk_min, self.atk_max)

    def decrease_hp(d_hp: int):
        self.hp = self.hp - d_hp

    def increase_hp(d_hp: int):
        self.hp = self.hp + d_hp

    def level_up(max_lvlup: int, min_lvlup: int):
        assert max_lvlup + min_lvlup  <= 10
        
        self.atk_max = self.atk_max + max_lvlup
        self.atk_min = self.atk_min + min_lvlup

    def is_alive():
        return self.hp > 0

class Monster:
    
    def __init__(m_name: str, lvl: int):

        self.name = m_name
        self.level = lvl
        self.hp = 10*lvl
        self.atk_max = lvl*2
        self.atk_min = 0
        self.exp_given = lvl/5

    def attack():
        return randrange(self.atk_min, self.atk_max)

    def decrease_hp(d_hp: int):
        self.hp = self.hp - d_hp

    def increase_hp(d_hp: int):
        self.hp = self.hp + d_hp

    def is_alive():
        return self.hp > 0

def fight(hero: Hero, monster: Monster):
    print('{} vs {}'.format(hero.name, monster.name))




        
