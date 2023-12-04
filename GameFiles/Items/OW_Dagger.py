from .ItemClass import Weapon
from GameFiles.Spells.SpellClass import Spell


def give_dagger(holder=None) -> None:    # holder:Unit
    dagger = Weapon(spell=Spell('Dagger attack', 0, 3, 0), weapon_name='Dagger',
                        description='Casual dagger with curved blade', size=1, holder=holder)
    holder.inventory['ITEMS'].append(dagger)
    dagger.take_on()