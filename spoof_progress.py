import pickle

def spoof():
    with open('./GameFiles/Saves/ZeroSave_player.pickle', "wb") as file:
        pickle.dump(None, file)
    with open('./GameFiles/Saves/ZeroSave_monster.pickle', "wb") as file:
        pickle.dump(None, file)
    with open('./GameFiles/Saves/ZeroSave_player_name.txt', "w") as file:
        file.write('Player')

    with open('./GameFiles/Saves/SecondSave_player.pickle', "wb") as file:
        pickle.dump(None, file)
    with open('./GameFiles/Saves/SecondSave_monster.pickle', "wb") as file:
        pickle.dump(None, file)
    with open('./GameFiles/Saves/SecondSave_player_name.txt', "w") as file:
        file.write('Player')

    with open('./GameFiles/Saves/ThirdSave_player.pickle', "wb") as file:
        pickle.dump(None, file)
    with open('./GameFiles/Saves/ThirdSave_monster.pickle', "wb") as file:
        pickle.dump(None, file)
    with open('./GameFiles/Saves/ThirdSave_player_name.txt', "w") as file:
        file.write('Player')

if __name__ == '__main__':
    spoof()