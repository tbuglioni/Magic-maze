with open("extra.txt","r") as mon_fichier:
    texte = mon_fichier.read()
#---------------------------------------
liste1 = []
for elt in texte :
    if elt in "01":
        liste1.append(int(elt))
#---------------------------------------
mur = []
couloir = []
i = 1
endincolumn = [15,115,215,215,315,415,515,615,715,815,
                 915,1015,1115, 1215, 1315, 1415]
for elt in liste1:
    if elt == 1:
        mur.append(i)
        if i in endincolumn:
            i += 86
        else:
            i += 1
    elif elt == 0:
        couloir.append(i)
        if i in endincolumn:
            i += 86
        else:
            i += 1

print(mur)
print(couloir)

