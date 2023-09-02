# from GameFiles import Spell

class Item:
    def __init__(self,item_name:str, description:str='',):
        self.item_name = item_name
        self.description = description
    def pick_up(self,holder):
        self.holder = holder
        holder.inventory['ITEMS'].append(self)
    def drop(self, holder):
        holder.inventory['ITEMS'].remove(self)
        del self
    def info(self):
        print(f'{self.item_name:-^20}\n'
              f'DISCRIPTION: {self.description}\n'
              f'HOLDER: {self.holder.name}\n')


class Weapon(Item):
    def __init__(self,spell:object, weapon_name:str, description:str, size:int, holder=None): #size = 1 or 2
        self.spell = spell
        self.item_name = weapon_name
        self.size = size
        self.item_name = weapon_name
        self.holder = holder
        self.description = description
    def pick_up_weapon(self,):
        self.holder.inventory['ITEMS'].append(self)
        self.spell(self.holder)

class Armor(Item):
    def __init__(self, spell:object, armor_name:str, description:str, piece_of_armor:str, holder=None): #piece_of_armor='HEAD' or 'BODY' or "BOOTS"
        self.spell = spell
        self.item_name = armor_name
        self.piece_of_armor = piece_of_armor.upper()
        self.holder = holder
        self.description = description
    def take_on(self):
        if self not in self.holder.inventory['ITEMS']:
            print(f'You can`t wear {self.item_name}, because {self.item_name} not in your inventory')
        else:
            if self.holder.inventory[self.piece_of_armor] != None:
                self.holder.inventory['ITEMS'].append(self.holder.inventory[self.piece_of_armor])
                self.holder.inventory[self.piece_of_armor] = None
            self.holder.inventory[self.piece_of_armor] = self
            self.holder.inventory['ITEMS'].remove(self)
            self.spell(self.holder)
    def take_off(self,):
        if self in self.holder.inventory['ITEMS']:
            print('You can`t take off without wearing it')
        else:
            self.holder.inventory['ITEMS'].append(self.holder.inventory[self.piece_of_armor])
            self.holder.inventory[self.piece_of_armor] = None
    def info(self):
        print(f'{self.item_name:-^20}\n'
            f'{self.description}\n'
            f'{self.holder}'
            f'{self.spell.get_info()}')



if __name__ == '__main__':
    # item = Item(holder=Unit('Bob', 10, 1, 10),
    #             item_name='Beach',
    #             description='just the item')
    # print(item)
    # armor = Armor(Spell('LoL',Item.holder))
    pass