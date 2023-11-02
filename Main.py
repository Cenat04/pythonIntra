import random


class Candidat:
    def __init__(self, code, nom, prenom, niveau_universitaire, sexe, specialisation):
        self.code = code
        self.nom = nom
        self.prenom = prenom
        self.niveau_universitaire = niveau_universitaire
        self.sexe = sexe
        self.specialisation = specialisation


class CandidatProgrammation(Candidat):
    def __init__(self, code, nom, prenom, niveau_universitaire, sexe, specialisation, note_programmation):
        super().__init__(code, nom, prenom, niveau_universitaire, sexe, specialisation)
        self.note_programmation = note_programmation


class CandidatBaseDeDonnees(Candidat):
    def __init__(self, code, nom, prenom, niveau_universitaire, sexe, specialisation, note_conception_bd,
                 note_question1, note_question2):
        super().__init__(code, nom, prenom, niveau_universitaire, sexe, specialisation)
        self.note_conception_bd = note_conception_bd
        self.note_question1 = note_question1
        self.note_question2 = note_question2


class CandidatReseaux(Candidat):
    def __init__(self, code, nom, prenom, niveau_universitaire, sexe, specialisation, note_reseaux, note_question1,
                 note_question2, note_question3):
        super().__init__(code, nom, prenom, niveau_universitaire, sexe, specialisation)
        self.note_reseaux = note_reseaux
        self.note_question1 = note_question1
        self.note_question2 = note_question2
        self.note_question3 = note_question3


# Dictionnaires pour stocker les candidats dans chaque domaine
candidats_programmation = {}
candidats_bd = {}
candidats_reseaux = {}


def enregistrer_candidat():
    code = str(random.randint(1000, 9999))
    nom = input("Nom du candidat : ")
    prenom = input("Prénom du candidat : ")
    niveau_universitaire = input("Niveau universitaire : ")
    sexe = input("Sexe : ")
    specialisation = input("Spécialisation : ")
    domaine = input("Domaine (Programmation/BaseDeDonnees/Reseaux) : ")

    if domaine == "Programmation":
        note_programmation = int(input("Note en Programmation (sur 1200) : "))
        candidat = CandidatProgrammation(code, nom, prenom, niveau_universitaire, sexe, specialisation,
                                         note_programmation)
        candidats_programmation[code] = candidat
    elif domaine == "BaseDeDonnees":
        note_conception_bd = int(input("Note de conception de base de données (sur 500) : "))
        note_question1 = int(input("Note pour la Question 1 (sur 300) : "))
        note_question2 = int(input("Note pour la Question 2 (sur 150) : "))
        candidat = CandidatBaseDeDonnees(code, nom, prenom, niveau_universitaire, sexe, specialisation,
                                         note_conception_bd, note_question1, note_question2)
        candidats_bd[code] = candidat
    elif domaine == "Reseaux":
        note_reseaux = int(input("Note en Réseaux (sur 450) : "))
        note_question1 = int(input("Note pour la Question 1 (sur 250) : "))
        note_question2 = int(input("Note pour la Question 2 (sur 150) : "))
        note_question3 = int(input("Note pour la Question 3 (sur 150) : "))
        candidat = CandidatReseaux(code, nom, prenom, niveau_universitaire, sexe, specialisation, note_reseaux,
                                   note_question1, note_question2, note_question3)
        candidats_reseaux[code] = candidat
    else:
        print("Domaine non reconnu.")


