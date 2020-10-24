# OCR-projet-3

### PRESENTATION:
This is my first project with python and pygame, it's a small game with 2 levels in a labyrinth.

### INSTALLATION:
It's created with python 3.8 AND pygame==2.0.0.dev12 in a PIPENV (linux/mac interface)
you can use requirement OR pipefile to install.

Be careful : pygame is not complicated to install but cannot be open with each system and 
each version ... 

### GAME:
- 2 levels
- 1 position specific to hero, Gard, exit point
- 3 objects (random position)
- use arrow to move (keyboard)

the end : if you have 3 objects collected you can kill the Gard and walk 
into the staircase for next lvl

### FILES
level:
a level.txt file is used to create à new labyrinth with this element (case 15X15):
0 = wall
1 = path
2 = hero
3 = Gard
4 = exit

the game must only with 15 lines with 15 columns

images: 
the game contain images "free to use" [source link](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/macgyver_ressources.zip)
