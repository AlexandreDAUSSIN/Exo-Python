Niveau 1

print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel
je pense, il se situe entre 1 et 100")

import numpy.random as rd
x = rd.rand(1, 100)

try = input("Avez vous une idée ?")

if try < x:
	print("C'est plus")
else if try > x:
	print("C'est moins")
else:
	print("C'est ça")

Niveau 2

print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel
je pense, il se situe entre 1 et 100")

import numpy.random as rd
x = rd.rand(1, 100)
try = input("Avez vous une idée ?")
i = 0


while try != x:

	if i >= 5:
		print("C'est perdu")
	else if try < x:
		print("C'est plus")
		i += 1
	else if try > x:
		print("C'est moins")
		i += 1
	else:
		print("C'est ça")

	try = input("Avez vous une idée ?")


Niveau 3

import tkinter
fenetre = tkinter.Tk()
fenetre.config(bg = "#24f720")
entrée1 = Entry (fenetre)






