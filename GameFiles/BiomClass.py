import random as rnd


class BiomClass:
    def __init__(self, lst_Units:list, lst_Items:list, player:object):
        self.units = lst_Units
        self.items = lst_Items
        self.player = player

    def summon_some_monsters(self):
        # summon random monster
        rnd_monster = rnd.choice(self.units)

        # buff monster
        rnd_monster.hp += self.player.lvl
        rnd_monster.defence += self.player.lvl
        rnd_monster.damage += self.player.lvl
        rnd_monster.lvl += self.player.lvl

        # give random weapon for monster
        rnd_weapon = rnd.choice(self.items)
        rnd_weapon(rnd_monster)

        return rnd_monster
