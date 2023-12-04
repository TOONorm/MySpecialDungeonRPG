import spoof_progress
from GameFiles import *
import cmd
import pickle


select_save = input(f'Select a save:\n1.{"ZeroSave":=^20}\n2.{"SecondSave":=^20}\n3.{"ThirdSave":=^20}\n>>> ')
if select_save == '1':
    with open('./GameFiles/Saves/ZeroSave.pickle', "rb") as file:
        static_for_load = pickle.load(file)
        player_name = static_for_load[2]
elif select_save == '2':
    with open('./GameFiles/Saves/SecondSave.pickle', "rb") as file:
        static_for_load = pickle.load(file)
        player_name = static_for_load[2]
elif select_save == '3':
    with open('./GameFiles/Saves/ThirdSave.pickle', "rb") as file:
        static_for_load = pickle.load(file)
        player_name = static_for_load[2]




# shell
class Game(cmd.Cmd):
    global player, monster, player_name
    intro = 'Send "help" or ? for list commands.\nSend ?/help before command for show description of command like <help attack>\n'
    prompt = f'<{player_name}> '
    doc_header = 'What can you do'

    def do_crt_player(self, arg):
        'Create your character, it`s simply if you can read english'
        global player, player_name, monster
        if player == None:
            player = Unit(input('Enter character name: '),)
            player_name = player.name
            player.statistics()
            Game.do_save_the_game(self, arg)
            Game.do_stop_game(self, arg)
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
                print('You haven`t created character. Use command "crt_player"')
    def do_see_inventory(self,arg):
        'See your inventory'
        try:
            if player != None:
                Inventory(unit_inventory=player).cmdloop()
            else:
                print('You haven`t created character. Use command "crt_player"')
        except SystemExit:
            print(f'{"You backed":.^20}')

    def do_stop_game(self, arg):
        'send for stop the game'
        raise KeyboardInterrupt
    def do_save_the_game(self, arg):
        "Save your game"
        global player, monster, player_name, count_of_loot, list_of_static, biom

        list_of_static = [player, monster, player_name, count_of_loot, biom]

        select_save = input(
            f'Select a save:\n1.{"ZeroSave":=^20}\n2.{"SecondSave":=^20}\n3.{"ThirdSave":=^20}\n>>> ')

        if select_save == '1':
            with open('./GameFiles/Saves/ZeroSave.pickle', "wb") as file:
                pickle.dump(list_of_static, file)
        elif select_save == '2':
            with open('./GameFiles/Saves/SecondSave.pickle', "wb") as file:
                pickle.dump(list_of_static, file)
        elif select_save == '3':
            with open('./GameFiles/Saves/ThirdSave.pickle', "wb") as file:
                pickle.dump(list_of_static, file)

        print(f'\n{"Game saved":=^20}\n')
    def do_go(self, arg):
        'Go into the next room of Dungeon'
        global monster, player, count_of_loot
        count_of_loot = 1
        if player != None and monster == None or player != None and monster.status == 'DEAD':
            monster = None
            monster = biom.summon_some_monsters()
            monster.statistics()
        else:
            if monster != None:
                print('\nYou fighting now!\n')
            if player == None:
                print('\nYou haven`t created character. Use command "crt_player"\n')

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
            if player.attacking(monster) == 'DEAD':
                Game.do_stop_game(self, arg)
        else:
            if monster == None:
                print('Now you don`t see monsters...')
            if player == None:
                print('You haven`t created character. Use command "crt_player"')
    def do_looting(self, arg):
        'When your opponent loose, you can take him loot'
        global count_of_loot
        if count_of_loot >= 1:
            count_of_loot -= 1
            player.looting(monster)
        else:
            print('\nYou wasted your looting point\n')
    def do_spoof_all_progress(self,arg):
        'Delete all your saves'
        if input('You absolutly right?[y/n]:\n') == 'y':
            spoof_progress.spoof()
            raise KeyboardInterrupt



class Inventory(cmd.Cmd):
    global monster, player
    intro = f'\n{"INVENTORY":-^32}\n\nSend "help" or ? for list commands.\nSend ?/help before command for show description of command like <help attack>\n'
    prompt = '>>> '
    doc_header = 'All what can you see'
    def __init__(self, unit_inventory:Unit):
        self.unit = unit_inventory
        cmd.Cmd.__init__(self)
    def do_armor(self, arg):
        'Look at armor'
        self.unit.get_armor()

    def do_item_info(self, arg):
        'Invent item from inventory. Use "item_info <item slot or inventory position(head, body, 1, 2, 3, etc.)>" struct.'
        if arg.upper() not in list(self.unit.inventory.keys()):
           print('Not supported key')
        else:
            # if int(arg) == int:
            #     self.unit.inventory['ITEMS'][int(arg)-1].info()
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


# functions
def load_static(name_save:str) -> None:
    global player, monster, player_name, select_save, count_of_loot, biom
    with open(f'./GameFiles/Saves/{name_save}Save.pickle', "rb") as file:
        static_for_load = pickle.load(file)
        player = static_for_load[0]
        monster = static_for_load[1]
        player_name = static_for_load[2]
        count_of_loot = static_for_load[3]
        biom = BiomClass(lst_Units=lst_un(), lst_Items=lst_it(), player=static_for_load[0])

def load_save() -> None:
    # load save
    if select_save == '1':
        load_static('Zero')

    elif select_save == '2':
        load_static('Second')

    elif select_save == '3':
        load_static('Third')


# start of script
if __name__ == '__main__':
    print('\nWelcome to pre-alfa-beta-test of the MySpecialDungeon.\n')
    while True:
        try:
            # load save
            load_save()

            # game
            Game().cmdloop()

        except KeyboardInterrupt:
            print(f'\n{"_" * 21}\n|{"=" * 19}|\n|{"Game Over":=^19}|\n|{"=" * 19}|\n|{" " * 19}|\n')
            break
        except NameError:
            print('Not supported key\n')
        # finally:
        #     if input('(Do not restart for save the progress or changes)\nWana restart?[y/n]:\n') != 'y':
        #         print('Goodbye')
        #         break