#Mathéo Hima
#2023
#poo 2 et 3

import random


def attribut():
    random1 = random.randint(1,6)
    random2= random.randint(1,6)
    random3 = random.randint(1,6)
    random4 = random.randint(1,6)
    ran =[random1, random2, random3, random4]
    ran.remove(min(ran))
    sum(ran)
    return (ran)


class NPC:
    def __init__(self):
        self.Force = attribut()
        self.Agilite = attribut()
        self.Constitiution = attribut()
        self.Intelligence = attribut()
        self.Sagesse = attribut()
        self.Charisme = attribut()
        self.classedarmure = random.randint(1, 12)
        self.nom = None
        self.race = None
        self.espece = None
        self.pointdevie = random.randint(1, 20)
        self.Job = None

    def affichercaractyristiques(self):
        print("Force =", self.Force)
        print("Agilité =", self.Agilite)
        print("Constitiution =", self.Constitiution )
        print("Intelligence =", self.Intelligence )
        print("Sagesse =", self.Sagesse)
        print("Charisme =", self.Charisme)
        print("Class d'armure =", self.classedarmure)
        print("Nom =", self.nom)
        print("Espèce =", self.espece)
        print("Point de vie =", self.pointdevie)
        print("Job =", self.Job)

class  Dragon(NPC):

    def __init__(self):
        super().__init__()
        self.race = "Dragon"
        self.espece = "Monstre"
        self.Job = "méchant"

class Heros(NPC):

    def __init__(self):
        super().__init__()
        self.race = "blanc"
        self.espece = "humain"
        self.profession = "Héros"
        self.nom = "Mathéo"

