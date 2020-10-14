import random

class ItemsLab:
    """ creating labyrinth with walls, path, and 3 stuffs on random location"""
    def __init__(self):
        self.path = [
            5, 10, 11,
            102, 103, 104, 105, 107, 108, 110, 111, 113, 114,
            202, 204, 205, 208, 210, 211, 212, 213, 214, 215,
            302, 303, 304, 305, 306, 307, 308, 310, 312,
            401, 402, 408, 409, 410, 412, 413, 414,
            501, 502, 503, 504, 505,
            602, 604, 605, 607, 609, 610, 611, 612, 613, 614,
            702, 703, 704, 705, 707, 709, 713,
            802, 804, 805, 807, 809, 811, 812, 813, 814,
            902, 903, 904, 905, 906, 907, 909, 911,
            1002, 1004, 1009, 1011, 1012, 1013, 1014, 1015,
            1102, 1103, 1104, 1105, 1106, 1107,1108, 1109, 1111, 1114,
            1202, 1204, 1205, 1211, 1214,
            1302, 1303, 1304, 1305, 1307, 1308, 1309, 1310, 1311, 1314,
            1404, 1407, 1408, 1409, 1410
            ]
        self.gard = [1314]
        self.stuff = []
        self.stuff1 = []
        self.stuff2 = []
        self.stuff3 = []
        
        
    def randomstuff(self):
        """ put on the path 3 stuffs in random location """
        freelocation = [102, 107, 114, 607, 614, 703, 814, 1302, 1307]
        random.shuffle(freelocation)
        self.stuff = freelocation[:3]
        self.stuff1.append(freelocation[0])
        self.stuff2.append(freelocation[1])
        self.stuff3.append(freelocation[2])
    
    def errase_stuff(self, nb):
        """ check if the hero si on the same location of a stuff,
        and errase it, on the map """
        if nb == self.stuff1 :
            self.stuff1 = 0
            return 1
        elif nb == self.stuff2 :
            self.stuff2 = 0
            return 2
        elif nb == self.stuff3 :
            self.stuff3 = 0
            return 3
        else:
            return 4
        
        



