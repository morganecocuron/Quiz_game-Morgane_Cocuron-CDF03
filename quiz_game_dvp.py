# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:27:03 2025

@author: jean-
"""

import requests
import random

# URL de l'API Open Trivia
API_URL = "https://opentdb.com/api.php"

# Paramètres pour récupérer 10 questions de difficulté facile
params = {
    "amount": 10,           # Nombre de questions
    "difficulty": "easy",  # Difficulté des questions
    "type": "multiple"     # Type : choix multiple
}

# Récupérer les questions depuis l'API
response = requests.get(API_URL, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()
    questions = data["results"]  # Les questions sont dans le champ "results"
else:
    print(f"Erreur : impossible de récupérer les questions ({response.status_code})")
    exit()

# Variable pour suivre les réponses correctes
all_correct = True  # On part du principe que le joueur répondra bien à tout

# Parcourir et afficher les questions une par une
for idx, question in enumerate(questions, start=1):
    print(f"\nQuestion {idx}: {question['question']}")

    # Mélanger les réponses possibles (incorrectes + correcte)
    options = question["incorrect_answers"] + [question["correct_answer"]]
    random.shuffle(options)

    # Afficher les réponses
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")

    # Demander la réponse de l'utilisateur
    user_answer = input("Votre réponse (numéro) : ")

    # Vérifier si la réponse est correcte
    if options[int(user_answer) - 1] == question["correct_answer"]:
        print("✅ Correct ! 🎉")
    else:
        print(f"❌ Faux. La bonne réponse était : {question['correct_answer']}")
        all_correct = False  # Le joueur a échoué sur une question

# Vérifier si le joueur a gagné
if all_correct:
    print("\n🏆 Félicitations ! Vous avez répondu correctement à toutes les questions. Vous avez gagné ! 🎉")
else:
    print("\n❌ Dommage ! Vous n'avez pas répondu correctement à toutes les questions. Vous avez perdu !")

#Score
#True/False
#Difficulty level