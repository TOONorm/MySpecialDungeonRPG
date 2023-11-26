from random import randint
#from GameFiles import Unit


class Spell:
    def __init__(self, spl_name:str,hp=0, damage=0, defence=0,):
        self.spl_name = spl_name
        self.options = {
            'HP':hp, 'DAMAGE':damage, 'DEFENCE':defence,
        }
    def get_info(self):
        print(f'{self.spl_name:-^20}\n'
              f'HP BOOST: {self.options["HP"]}\n'
              f'DM BOOST: { self.options["DAMAGE"]}\n'
              f'DF BOOST: {self.options["DEFENCE"]}\n'
              )
    def __call__(self,victim:object):
        if self.spl_name == 'ARMOR' or self.spl_name == 'WEAPON':
            victim.hp += self.options['HP']
            victim.damage += self.options['DAMAGE']
            victim.defence += self.options['DEFENCE']
        else:
            if randint(0, 20) >= victim.defence:
                victim.hp += self.options['HP']
                victim.damage += self.options['DAMAGE']
                victim.defence += self.options['DEFENCE']

if __name__ == '__main__':
    spell = Spell('Fireball!', "Classic fireball", hp=10,defence=-3)
    spell.get_info()
    unit = Unit('Bob', 15, 6, 20)
    unit.statistics()
    spell(unit)
    unit.statistics()
