# ESCAPE GAME DEV BY AUB 23/09/2025
from termcolor import colored
import time

ascii_aub = """
  _____  ________      __    ______     __          _    _ ____  
 |  __ \|  ____\ \    / /   |  _ \ \   / /     /\  | |  | |  _ \ 
 | |  | | |__   \ \  / /    | |_) \ \_/ /     /  \ | |  | | |_) |
 | |  | |  __|   \ \/ /     |  _ < \   /     / /\ \| |  | |  _ < 
 | |__| | |____   \  /      | |_) | | |     / ____ \ |__| | |_) |
 |_____/|______|   \/       |____/  |_|    /_/    \_\____/|____/ 
"""
print(ascii_aub)
print("\n")

#Histoire

print(colored("Bienvenue à vous jeune(s) aventuriers(s) !", "red"))
time.sleep(3)
print("Thème : “Mission Spatiale : Sauver la Station Orbitale”")
time.sleep(4)
print("Voici le contexte : ")
time.sleep(3)
print("Tu es un astronaute coincé dans une station spatiale en orbite autour de Mars.")
time.sleep(4)
print("Une panne a bloqué tous les systèmes et tu dois réparer la station et retrouver le module de survie avant que l’oxygène ne s’épuise !")
time.sleep(5)
print("Pour cela, il va falloir découvrir plusieurs codes pour accéder à la cabine où se trouve le module de survie !")
time.sleep(3)
print("Voici la première enigme : \n")
time.sleep(2)
response = input("Chaque chiffre du code correspond au nombre de lettres dans chaque mot de cette phrase :‘Mars rouge orbit rapide’. Mais attention, additionne 1 à chaque chiffre si le mot contient une voyelle répétée. --> ")
if response == 4556:
    print("Bravo tu as réussi la première étape ! Passons à la suivante !")
else:
    print("Nan essaie encore ! ")
