import sys
sys.path.append('../../../GameFiles')

from random import randint
from GameFiles import *
from GameFiles.Items.OW_GoldenAxe import Golden_Axe

class OrcOrk(Unit):
    def __init__(self):
        self.name = 'OrcOrk'
        self.hp = randint(100, 166)
        self.damage = randint(15,35)
        self.defence = 13
        self.status = 'LIFE'
        self.inventory = {
            'HEAD': None,
            'BODY': None,
            'BOOTS': None,
            'WEAPON': Golden_Axe,
            'ITEMS': []
        }

if __name__ == '__main__':
    ork = OrcOrk()
    ork.statistics()
    ork.get_inventory()


