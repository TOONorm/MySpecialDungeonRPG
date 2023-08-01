from random import randint
from Spells.SpellClass import Spell
from Items.ItemClass import Armor, Weapon, Item


class Unit:
    def __init__(self, NAME:str ,HP:int, DM:int, DEFENCE:int, STATUS:str='LIFE'):
        self.inventory = {
            'HEAD': None,
            'BODY':None,
            'BOOTS':None,
            'WEAPON': {
                'FIRST HAND': None,
                'SECOND HAND': None,
            },
            'ITEMS':[]
        }
        self.name = NAME
        self.hp = HP
        self.damage = DM
        self.defence = DEFENCE
        self.status = STATUS.upper()

    def attacking(self, victim):
        if self.status != "LIFE":
            print(f'{self.name} can`t attacking, because {self.name} is {self.status}\n')
        else:
            if randint(0, 20) >= victim.defence:
                victim.hp -= self.damage
                if victim.hp <= 0:
                    victim.status = 'DEAD'
                print(f'{self.name} damaging opponent\n')
            else:
                print(f'{self.name} missed\n')
    def get_inventory(self):
        print(f'{"ARMOR":-^20}')
        for i in ['HEAD',"BODY","BOOTS",]:
            if self.inventory[i] != None:
                print(f'{i}: {self.inventory[i].armor_name}')
            else:
                print(f'{i}: {self.inventory[i]}')
        print(f'{"ITEMS":-^20}')
        for i in range(len(self.inventory["ITEMS"])):
            print(f'{i+1}. {self.inventory["ITEMS"][i].item_name}')

    def statistics(self):
        name = self.name
        hp = self.hp
        damage = self.damage
        status = self.status
        defence = self.defence

        if status == 'LIFE':
            char = '_'; vol = 10
        elif status == 'SHOCKED':
            char = '*'; vol = 13
        elif status == "DEAD":
            char = '#'; vol = 10
        else:
            char = ''; vol = 0
        print(f'\nNAME: {name}\n'
               f'HP: {hp}\n' 
               f'DM: {damage}\n' 
               f'DF: {defence}\n' 
               f'STATUS: {status:{char}^{vol}}\n')

def main_test_1():
    opp = Unit('OrcBolk', 30, 10, 8, 'life')
    unit = Unit('Bob', 30, 10, 8, 'life')
    while opp.hp > -10 and unit.hp > -10:
        unit.statistics()
        opp.statistics()
        unit.attacking(opp)
        opp.attacking(unit)
    unit.statistics()
    opp.statistics()


if __name__ == '__main__':
    bob = Unit('Bob', 10, 1, 10)
    bob.statistics(); bob.get_inventory()
    item = Item(item_name='Beach',
                description='just the item')
    item.pick_up(bob)
    armor = Armor(Spell('ARMOR', '', 0, 0, 4), 'MEGAturboSUPERhead','boots')
    armor.pick_up(bob)
    bob.statistics(); bob.get_inventory()
