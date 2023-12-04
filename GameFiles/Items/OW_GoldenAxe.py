from .ItemClass import Weapon
from GameFiles.Spells.SpellClass import Spell

def give_golden_axe(holder=None) -> None:    # holder:Unit
    golden_axe = Weapon(spell=Spell('Axe attack', 0, 3, 1), weapon_name='Golden Axe',
                        description='Very expencive, but gaudy', size=2, holder=holder)
    holder.inventory['ITEMS'].append(golden_axe)
    golden_axe.take_on()