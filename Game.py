from GameFiles import *
import cmd

# static
player = None
monster = None
player_name = 'Player'

# shell
class Game(cmd.Cmd):
    global player, monster, player_name
    intro = '\nSend "help" or ? for list commands.\n'
    prompt = f'<{player_name}> '
    doc_header = 'What can you do'

    def do_crt_player(self, arg):
        'Create your character, it`s simply if you can read english'
        global player, player_name
        if player == None:
            player = Unit(input('Enter character name: '),)
            player_name = player.name
            player.statistics()
        else:
            print('You have character')
    def do_stat(self, arg):
        'statistics of your character and your opponent'
        global player, monster
        player.statistics()
        if monster != None:
            monster.statistics()
    def do_see_inventory(self,arg):
        'your inventory'
        global player
        player.get_inventory()
    def do_stop_game(self, arg):
        'send for stop the game'
        raise KeyboardInterrupt
    def do_go_next(self, arg):
        'Go into the next room of Dungeon'
        global monster,player
        if player != None and monster == None:
            monster = Unit('Monster', 100, 4, 7)
            # armors = [Armor(Spell('ARMOR','',0,0,1), 'Head of Orc', '', 'HEAD', monster),
            #          Armor(Spell('ARMOR', '', 4, 0, 3), 'Body of Orc', '', 'BODY', monster)]
            # for i in armors:
            #     i.pick_up(monster)
            #     i.take_on()
            # weapon = Weapon(Spell('Damage of sword', 'Harm of iron sword', 0, 5, 0), 'Sword', 'Just one-hand sword', size=1, holder=monster)
            # weapon.pick_up_weapon()
            monster.statistics()
        else:
            if monster != None:
                print('You fighting now!')
            if player == None:
                print('You haven`t created character.')

    def do_invent_opponent(self, arg):
        'See what wear and use your opponent'
        global monster
        if monster != None:
            monster.statistics()
            monster.get_inventory()
        else:
            print('Now you don`t see monsters. You need going into next room.')
    def do_attack(self, arg):
        'Attack your enemy!!!'
        global monster, player
        if player != None and monster != None:
            player.attacking(monster)
            monster.attacking(player)
        else:
            if monster == None:
                print('Now you don`t see monsters...')
            if player == None:
                print('You haven`t created character.')

# start game
if __name__ == '__main__':
    print('\nWelcome to alfa-pre-alfa-beta-test of the MySpecialDungeon.')
    while True:
        try:
            Game().cmdloop()
        except AttributeError:
            print('You haven`t created character. Use command "crt_char"')
