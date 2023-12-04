from GameFiles import *


class OrcOrk(Unit):
    def __init__(self):
        self.name = 'Orc-Ork'
        self.lvl = 1
        self.hp = 55
        self.damage = 5
        self.defence = 2
        self.status = 'LIFE'
        self.inventory = {
            'HEAD': None,
            'BODY': None,
            'BOOTS': None,
            'FIRST HAND': None,
            'SECOND HAND': None,
            'ITEMS': []
        }


if __name__ == '__main__':
    ork = OrcOrk()
    ork.statistics()
    ork.get_inventory()


