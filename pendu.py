import random

def length(list):             # Little function to return length of a list
    c = 0
    for i in list:
        c += 1
    return c

# This function will transform any string in a string containing only lower char.
def myLower(string):
	lowercase = "abcdefghijklmnopqrstuvwxyzéèêëàîïôö\n"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZÉÈÊËÀÎÏÔÖ\n"
	lowered = ''
	for c in string:
		if c == ' ':
			lowered += c
		for x in range(length(lowercase)):
			if c == uppercase[x]:
				lowered += lowercase[x]
			elif c == lowercase[x]:
				lowered += c
	return lowered

def string_to_list(string):   #function to convert a string to a list (each char of the string as a value of the list)
    LIST = []
    for i in string:
        LIST.append(i)
    return LIST

def list_to_string(LIST):   #function to convert a list to a string (each value of the list as a char in the string)
    string = ''
    for i in LIST:
        string += i
    return string


#############################################################################



with open("dico_france.txt", encoding = "ISO-8859-1") as dico:   #We need to replace each special char by a normal char
    string = myLower(dico.read())
    list = string_to_list(string)
    for l in range(length(list)-1):
        if list[l] == "é" or list[l] == "è" or list[l] == "ê" or list[l] == "ë":
            list[l] = "e"
        elif list[l] == "à" or list[l] == "ä" or list[l] == "â":
            list[l] = "a"
        elif list[l] == "î" or list[l] == "ï":
            list[l] = "i"
        elif list[l] == "ô" or list[l] == "ö":
            list[l] = "o"
        elif list[l] == "ù" or list[l] == "ü" or list[l] == "û":
            list[l] = "u"
    string = list_to_string(list)

with open("dico_france.txt", "w") as dic:
    dic.write(string)
with open("dico_france.txt", encoding = "ISO-8859-1") as d:
    dlist = d.readlines()

# Then we use randint to randomly select an element of the list
word = dlist[random.randint(0,length(dlist)-1)]

######################################################################

nb_lettres_trouve = 0         # counters for letters found and hit points
hp = 0

already_tried = ''            # string to store char already tried
lettre = ''                   # string to store user's input
lvl = 0

#####################################################################

while lvl != 1 and lvl != 2 and lvl != 3:
    lvl = int(input ("Choisissez un niveau :\n1 = Debutant / 2 = Intermediaire / 3 = Expert\n"))

    if lvl == 1:
        hp = 10                             # Here the user can choose the difficulty
    elif lvl == 2:                          # His choice will set the amount of hit point he get
        hp = 7
    elif lvl == 3:
        hp = 4
    else:
        print("Erreur, choisissez 1, 2 ou 3")


#########################################################################

# And let's go for the main loop :

while nb_lettres_trouve != length(word)-1 and hp > 0:    # While the whole word isn't found, while user still has
    print("Nombre de vie(s) restante(s) : ", hp)         # hit points
                                                         # print how many hit points he has
    print ("%d lettres à trouver pour gagner !" % (length(word)-nb_lettres_trouve-1))
    if (lvl != 3):                                       # if we're not in "expert mode",
        print("Lettres proposées : ", already_tried)     # print letters he has already tried

    for i in range(length(word)-1):                     # let's use a "for" loop to parse the word
        if word[i] not in already_tried:                # if the current letter is not in "already tried" string
            print ("_ " , end = '')                     # then the user didn't find it yet, so print "_ "
        else:                                           # else, the current letter is in the string, so he found it
            print (word[i] + " " , end = '')            # let's print this letter
    print ("\n")

    lettre = input("Quelle lettre proposes-tu ? : ")    # user is prompted to put a letter
    already_tried += " " + lettre                       # we add this letter to "already_tried" string

    for j in word:                                      # Another "for" loop to count how many letters he found.
        if lettre == j:                                 # if letter (user's input) is in word, increase our counter
            nb_lettres_trouve += 1
    if lettre not in word:                              # if it's not , then the user has failed ! He loses one hit point
        hp -= 1

##########################################################

if nb_lettres_trouve == length(word)-1:                 # Two case if we are out of the main loop :
    print("Bravo, tu as gagné ! Tu as trouvé : ", word )                       # if number of letters found is equal to length of the word,
elif hp <= 0:                                           # Then he found the word and we print "Bravo you've wun"
    print("C'est perdu ! Le mot était : ", word)        # Else he doesn't have anymore hit point and he has lost
