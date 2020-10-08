from ItemsLab import ItemsLab
from Heroes import Heroes

labyrinth = ItemsLab() # new game with walls and spaces
mcgyver = Heroes() # new heroe in labyrinth, at start point
labyrinth.randomstuff() # add 3 objects in a random location on labyrinth
print(labyrinth.stuff) # print the location of 3 items on map

game = True

while game: #check if mcgyver : move, take stuff, find the ending point
    while mcgyver.loc != 1214: # mcgyver is not at 1214 = ending point
        mcgyver.inmotion(labyrinth.path) # he can ONLY move on the path
        analyse_case = labyrinth.errase_stuff(mcgyver.loc) #check if is stuff on map
        mcgyver.getstuff(analyse_case) #check if add or not stuff in invent
        print(mcgyver.loc) #print where is actualy mc gyver

    if (mcgyver.loc == 1214) and (mcgyver.inventory == [1,1,1]):
        print("you win, congratulation :)") #ending location with invent : full
        game = False # GOOD ending
    elif (mcgyver.loc == 1214) and (mcgyver.inventory != [1,1,1]):
        print("you lose, :/ :)") #ending location with invent : not full
        game = False # BAD ending
    else:
        pass # it's note the ending location, the game continue
        
