# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:27:03 2025

@author: jean-
"""

import requests
import random

# Open Trivia API URL
API_URL = "https://opentdb.com/api.php"

# Parameters to fetch 10 questions with easy difficulty and multiple types
params = {
    "amount": 10,           # Number of questions
    "difficulty": "easy",   # Difficulty of the questions
    "type": "multiple"      # Type: multiple choice (we will allow true/false as well)
}

# Fetch the questions from the API
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    questions = data["results"]  # Questions are in the "results" field
else:
    print(f"Error: Unable to fetch questions ({response.status_code})")
    exit()

# Variable to track correct answers
all_correct = True  # Assume the player will answer everything correctly

# Loop through and display each question one by one
for idx, question in enumerate(questions, start=1):
    print(f"\nQuestion {idx}: {question['question']}")

    # Check if it's a True/False question
    if question['type'] == 'boolean':
        options = ['True', 'False']  # True/False options
    else:
        # Shuffle the possible answers (incorrect + correct)
        options = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(options)

    # Display the answers
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")

    # Ask for the user's answer
    user_answer = input("Your answer (number): ")

    # Check if the answer is correct
    if options[int(user_answer) - 1] == question["correct_answer"]:
        print("✅ Correct! 🎉")
    else:
        print(f"❌ Incorrect. The correct answer was: {question['correct_answer']}")
        all_correct = False  # The player failed on a question

# Check if the player won
if all_correct:
    print("\n🏆 Congratulations! You answered all the questions correctly. You won!")
else:
    print("\n❌ Sorry! You didn't answer all the questions correctly. You lost!")

#Score
#True/False
#Difficulty level