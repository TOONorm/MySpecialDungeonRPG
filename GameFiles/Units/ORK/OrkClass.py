import sys
sys.path.append('../../../GameFiles')

from random import randint
from GameFiles import *


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
            'WEAPON': None,
            'ITEMS': []
        }

if __name__ == '__main__':
    ork = OrcOrk()
    ork.statistics()
    ork.get_inventory()


