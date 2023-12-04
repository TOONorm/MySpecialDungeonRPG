from .UnitClass import Unit
from .Items.ItemClass import Armor, Weapon, Item
from .Items.OW_GoldenAxe import give_golden_axe
from .Items.OW_Dagger import give_dagger
from .Spells.SpellClass import Spell
from .Units.ORK.OrkClass import OrcOrk
from .Units.GUBLIN.GublinClass import Gublin
from .BiomClass import BiomClass

def lst_un() -> list:
    list_of_units = [OrcOrk(), Gublin()]
    return list_of_units
def lst_it() -> list:
    list_of_items = [give_golden_axe, give_dagger]
    return list_of_items