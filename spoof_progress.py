import pickle
from GameFiles import *

list_of_static = [None, None, 'Player', 1, BiomClass(lst_Units=lst_un(), lst_Items=lst_it(), player=None)]

def spoof():
    with open('./GameFiles/Saves/ZeroSave.pickle', "wb") as file:
        pickle.dump(list_of_static, file)
    with open('./GameFiles/Saves/SecondSave.pickle', "wb") as file:
        pickle.dump(list_of_static, file)
    with open('./GameFiles/Saves/ThirdSave.pickle', "wb") as file:
        pickle.dump(list_of_static, file)

if __name__ == '__main__':
    spoof()