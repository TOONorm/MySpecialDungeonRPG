import random
from random import randint, choice
from .Spells.SpellClass import Spell
from .Items.ItemClass import Armor, Weapon, Item


class Unit:
    def __init__(self, NAME:str='Bob' ,HP:int=100, DM:int=4, DEFENCE:int=7, LEVEL:int = 1, STATUS:str='LIFE'):
        self.inventory = {
            'HEAD': None,
            'BODY':None,
            'BOOTS':None,
            'FIRST HAND': None,
            'SECOND HAND': None,
            'ITEMS':[]
        }
        self.spell_book = []
        self.name = NAME
        self.hp = HP
        self.damage = DM
        self.defence = DEFENCE
        self.status = STATUS.upper()
        self.lvl = LEVEL

    def attacking(self, victim):
        if self.status != "LIFE":
            print(f'\n{self.name} can`t attacking, because {self.name} is {self.status}\n')
            del self
            return 'DEAD'
        elif victim.status != 'LIFE':
            print(f'{self.name} can`t attacking, because {victim.name} is {victim.status}\n')
            del victim
        else:
            if randint(0, 20) >= victim.defence:
                victim.hp -= self.damage
                if victim.hp <= 0:
                    victim.status = 'DEAD'
                print(f'\n{self.name} damaging opponent')
            else:
                print(f'{self.name} missed\n')
    def looting(self, victim):
        if victim.status == 'DEAD':
            item = random.choice(list(victim.inventory.keys()))
            try_taked_item = victim.inventory[item]
            if try_taked_item != None:
                if isinstance(try_taked_item, Weapon) or isinstance(try_taked_item, Armor):
                    try_taked_item.holder = self
                    if try_taked_item is isinstance(list, object):
                        try_taked_item[randint(0, len(try_taked_item))].pick_up(self)
                        try_taked_item[randint(0, len(try_taked_item))].drop(victim)
                    else:
                        try_taked_item.pick_up(self)
                        try_taked_item.drop(victim)
                print(f'You just take new item from {item}, check your inventory\n')
            else:
                print('\nYou are unfind nothin\n')
        else:
            print('Enemy is not dead\n')
    def get_inventory(self):
        self.get_armor()
        self.get_weapon()
        self.get_items()
    def get_armor(self):
        print(f'{"ARMOR":-^20}')
        for i in ['HEAD',"BODY","BOOTS",]:
            if self.inventory[i] != None:
                print(f'{i}: {self.inventory[i].item_name}')
            else:
                print(f'{i}: {self.inventory[i]}')
    def get_weapon(self):
        print(f'{"WEAPON":-^20}')
        for i in ['FIRST HAND', 'SECOND HAND']:
            if self.inventory[i] != None:
                print(f'{i}: {self.inventory[i].item_name}')
            else:
                  print(f'{i}: None')
    def get_items(self):
        print(f'{"ITEMS":-^20}')
        for i in range(len(self.inventory["ITEMS"])):
            print(f'{i+1}. {self.inventory["ITEMS"][i].item_name}')

    def statistics(self):
        name = self.name
        hp = self.hp
        damage = self.damage
        status = self.status
        defence = self.defence
        lvl = self.lvl

        if status == 'LIFE':
            char = '_'; vol = 10
        elif status == 'SHOCKED':
            char = '*'; vol = 13
        elif status == "DEAD":
            char = '#'; vol = 10
        else:
            char = ''; vol = 0
        print(f'\nNAME: {name}\n'
              f'LVL: {lvl}\n'
               f'HP: {hp}\n' 
               f'DM: {damage}\n' 
               f'DF: {defence}\n' 
               f'STATUS: {status:{char}^{vol}}\n')

def main_test_1():
    opp = Unit('OrcBolk', 30, 10, 8,)
    player = Unit('Bob', 30, 10, 8,)
    while opp.hp > -10 and player.hp > -10:
        player.statistics()
        opp.statistics()
        player.attacking(opp)
        opp.attacking(player)
    player.statistics()
    opp.statistics()

def main_test_2():
    bob = Unit('Bob', 10, 1, 10)
    bob.statistics()
    bob.get_inventory()
    item = Item(item_name='Beach',
                description='just the item')
    item.pick_up(bob)
    armor = Armor(Spell('ARMOR', '', 0, 0, 4), 'MEGAturboSUPERhead', 'boots')
    armor.pick_up(bob)
    bob.statistics()
    bob.get_inventory()

if __name__ == '__main__':
    main_test_2()
