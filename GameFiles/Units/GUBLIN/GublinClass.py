from GameFiles import *

class Gublin(Unit):
    def __init__(self):
        self.name = 'Gublin-Bublin'
        self.lvl = 1
        self.hp = 40
        self.damage = 1
        self.defence = 5
        self.status = 'LIFE'
        self.inventory = {
            'HEAD': None,
            'BODY': None,
            'BOOTS': None,
            'FIRST HAND': None,
            'SECOND HAND': None,
            'ITEMS': []
        }