import time

import spoof_progress
from GameFiles import *
import cmd
import pickle
from spoof_progress import spoof

def main():
    global player, monster, player_name, select_save
    while True:
        try:
            # load save
            select_save = input(
                f'Select a save:\n1.{"ZeroSave":=^20}\n2.{"SecondSave":=^20}\n3.{"ThirdSave":=^20}\n>>> ')
            if select_save == '1':
                with open('./GameFiles/Saves/ZeroSave_player.pickle', "rb") as file:
                    player = pickle.load(file)
                with open('./GameFiles/Saves/ZeroSave_monster.pickle', "rb") as file:
                    monster = pickle.load(file)
                with open('./GameFiles/Saves/ZeroSave_player_name.txt', "r") as file:
                    player_name = file.read()
                    print(player_name)
            elif select_save == '2':
                with open('./GameFiles/Saves/SecondSave_player.pickle', "rb") as file:
                    player = pickle.load(file)
                with open('./GameFiles/Saves/SecondSave_monster.pickle', "rb") as file:
                    monster = pickle.load(file)
                with open('./GameFiles/Saves/SecondSave_player_name.txt', "r") as file:
                    player_name = file.read()
            elif select_save == '3':
                with open('./GameFiles/Saves/ThirdSave_player.pickle', "rb") as file:
                    player = pickle.load(file)
                with open('./GameFiles/Saves/ThirdSave_monster.pickle', "rb") as file:
                    monster = pickle.load(file)
                with open('./GameFiles/Saves/ThirdSave_player_name.txt', "r") as file:
                    player_name = file.read()
            # game
            Game().cmdloop()
        # except AttributeError:
        #     print('You haven`t created character. Use command "crt_char"')
        except KeyboardInterrupt:
            print(f'\n{"_" * 21}\n|{"=" * 19}|\n|{"Game Over":=^19}|\n|{"=" * 19}|\n|{" " * 19}|\n')
        finally:
            if input('Wana restart?[y/n]:\n') != 'y':
                print('Goodbye')
                break

# static
count_of_loot = 1
player:Unit = None
monster:Unit = None
select_save = input(
                f'Select a save:\n1.{"ZeroSave":=^20}\n2.{"SecondSave":=^20}\n3.{"ThirdSave":=^20}\n>>> ')
if select_save == "1":
    player_name = open('./GameFiles/Saves/ZeroSave_player_name.txt', "r").read()
elif select_save == '2':
    player_name = open('./GameFiles/Saves/SecondSave_player_name.txt', "r").read()
elif select_save == '3':
    player_name = open('./GameFiles/Saves/ThirdSave_player_name.txt', "r").read()



# shell
class Game(cmd.Cmd):
    global player, monster, player_name
    intro = 'Send "help" or ? for list commands.\n'
    prompt = f'<{player_name}> '
    doc_header = 'What can you do'

    def do_crt_player(self, arg):
        'Create your character, it`s simply if you can read english'
        global player, player_name, monster
        if player == None:
            player = Unit(input('Enter character name: '),)
            player_name = player.name
            player.statistics()
            self.do_save_the_game('')
            raise KeyboardInterrupt
        else:
            if input('You have character. Wana kill him and create new? [y/n]') == 'y':
                player = None
                monster = None
                player_name = None
                Game.do_save_the_game(self, arg)
                Game.do_stop_game(self, arg)
    def do_stat(self, arg):
        'statistics of your character and your opponent'
        global player, monster
        if player != None:
            player.statistics()
        if monster != None:
            monster.statistics()
        else:
            if player == None:
                print('You haven`t created character. Use command "crt_char"')
    def do_see_inventory(self,arg):
        'See your inventory'
        try:
            if player != None:
                Inventory(unit_inventory=player).cmdloop()
            else:
                print('You haven`t created character. Use command "crt_char"')
        except SystemExit:
            print(f'{"You backed":.^20}')

    def do_stop_game(self, arg):
        'send for stop the game'
        raise KeyboardInterrupt
    def do_save_the_game(self, arg):
        "Save your game"
        global player, monster, player_name
        select_save = input(
            f'Select a save:\n1.{"ZeroSave":=^20}\n2.{"SecondSave":=^20}\n3.{"ThirdSave":=^20}\n>>> ')
        if select_save == '1':
            with open('./GameFiles/Saves/ZeroSave_player.pickle', "wb") as file:
                pickle.dump(player, file)
            with open('./GameFiles/Saves/ZeroSave_monster.pickle', "wb") as file:
                pickle.dump(monster, file)
            with open('./GameFiles/Saves/ZeroSave_player_name.txt', "w") as file:
                file.write(player_name)
        elif select_save == '2':
            with open('./GameFiles/Saves/SecondSave_player.pickle', "wb") as file:
                pickle.dump(player, file)
            with open('./GameFiles/Saves/SecondSave_monster.pickle', "wb") as file:
                pickle.dump(monster, file)
            with open('./GameFiles/Saves/SecondSave_player_name.txt', "w") as file:
                file.write(player_name)
        elif select_save == '3':
            with open('./GameFiles/Saves/ThirdSave_player.pickle', "wb") as file:
                pickle.dump(player, file)
            with open('./GameFiles/Saves/ThirdSave_monster.pickle', "wb") as file:
                pickle.dump(monster, file)
            with open('./GameFiles/Saves/ThirdSave_player_name.txt', "w") as file:
                file.write(player_name)
        print(f'\n{"Game saved":=^20}\n')
    def do_go(self, arg):
        'Go into the next room of Dungeon'
        global monster,player, count_of_loot
        count_of_loot = 1
        if player != None and monster == None or player != None and monster.status == 'DEAD':
            monster = Unit('Monster', 10, 4, 3)
            armors = [Armor(Spell('ARMOR',0,0,1), 'Head of Orc', '', 'HEAD', monster),
                     Armor(Spell('ARMOR', 4, 0, 3), 'Body of Orc', '', 'BODY', monster)]
            for i in armors:
                i.pick_up(monster)
                i.take_on()
            weapon = Weapon(Spell('Damage of sword', 0, 5, 0), 'Sword', 'Just one-hand sword', size=1, holder=monster)
            weapon.pick_up(monster)
            weapon.take_on()
            monster.statistics()
        else:
            if monster != None:
                print('You fighting now!')
            if player == None:
                print('You haven`t created character.')

    def do_invent_opponent(self, arg):
        'See what wear and use your opponent'
        try:
            if monster != None:
                Inventory(unit_inventory=monster).cmdloop()
            else:
                print('Now you don`t see monsters. You need to go into the next room.')
        except SystemExit:
            print(f'{"You back":.^20}')
    def do_attack(self, arg):
        'Attack your enemy!!!'
        if player != None and monster != None:
            player.attacking(monster)
            monster.attacking(player)
            if player.attacking == 'DEAD':
                Game.do_stop_game()
        else:
            if monster == None:
                print('Now you don`t see monsters...')
            if player == None:
                print('You haven`t created character.')
    def do_looting(self, arg):
        'When your opponent loose, you can take him loot'
        global count_of_loot
        if count_of_loot >= 1:
            count_of_loot -= 1
            player.looting(monster)
        else:
            print('You wasted your looting point')
    def do_spoof_all_progress(self,arg):
        'Delete all your saves'
        if input('You absolutly right?[y/n]:\n') == 'y':
            spoof_progress.spoof()
            raise KeyboardInterrupt



class Inventory(cmd.Cmd):
    global monster, player
    intro = "\n-------------INVENTORY-------------\n\nSend 'help' or ? for list commands.\n"
    prompt = '>>> '
    doc_header = 'All what can you see'
    def __init__(self, unit_inventory:Unit):
        self.unit = unit_inventory
        cmd.Cmd.__init__(self)
    def do_armor(self, arg):
        'Look at armor'
        self.unit.get_armor()

    def do_item_info(self, arg):
        'Invent item from inventory. Use "item_info <item slot(head, body, etc.)>" struct.'
        if arg.upper() not in list(self.unit.inventory.keys()):
            print('Not supported key')
        else:
            if self.unit.inventory[arg.upper()] != None and arg.upper() != 'ITEMS':
                self.unit.inventory[arg.upper()].info()
            elif arg.upper() == 'ITEMS':
                for i in range(len(self.unit.inventory[arg.upper()])):
                    self.unit.inventory[arg.upper()][i].info()
            else:
                print('Nothin for inventing')

    def do_take_on_item(self, arg):
        'Take on item if you can. Use "take_on_item <item slot(1, 2, 3, etc.)>" struct.'
        try:
            self.unit.inventory['ITEMS'][int(arg)-1].take_on()
        except IndexError:
            print('Nope')
    def do_weapon(self, arg):
        'Look at weapon'
        self.unit.get_weapon()
    def do_items(self, arg):
        'Look at items'
        self.unit.get_items()
    def do_full_inventory(self,arg):
        'See on all what enemy have'
        self.unit.get_inventory()
    def do_back(self,arg):
        'Go back and fight!'
        raise SystemExit

# start the game
def main():
    global player, monster, player_name, select_save
    while True:
        try:
            # load save
            if select_save == '1':
                with open('./GameFiles/Saves/ZeroSave_player.pickle', "rb") as file:
                    player = pickle.load(file)
                with open('./GameFiles/Saves/ZeroSave_monster.pickle', "rb") as file:
                    monster = pickle.load(file)
            elif select_save == '2':
                with open('./GameFiles/Saves/SecondSave_player.pickle', "rb") as file:
                    player = pickle.load(file)
                with open('./GameFiles/Saves/SecondSave_monster.pickle', "rb") as file:
                    monster = pickle.load(file)
            elif select_save == '3':
                with open('./GameFiles/Saves/ThirdSave_player.pickle', "rb") as file:
                    player = pickle.load(file)
                with open('./GameFiles/Saves/ThirdSave_monster.pickle', "rb") as file:
                    monster = pickle.load(file)
            # game
            Game().cmdloop()
        # except AttributeError:
        #     print('You haven`t created character. Use command "crt_char"')
        except KeyboardInterrupt:
            print(f'\n{"_" * 21}\n|{"=" * 19}|\n|{"Game Over":=^19}|\n|{"=" * 19}|\n|{" " * 19}|\n')
        finally:
            if input('Wana restart?[y/n](Do not restarting for save the progress or changes):\n') != 'y':
                print('Goodbye')
                break


# start of script
if __name__ == '__main__':
    print('\nWelcome to pre-alfa-beta-test of the MySpecialDungeon.\n')
    main()
