import json
import os

from RandomQuestionQuiz import RandomQuestionQuiz
from CategoryQuestions import QuizByCategory

quiz_category = QuizByCategory()
quiz_random = RandomQuestionQuiz()


def print_score(score_type):
    if score_type == "random":
        file = "random-score.json"
        read_score(file)
    elif score_type == "category":
        file = "category-score.json"
        read_score(file)
    else:
        print("Taki ranking nie istnieje")


def read_score(file):
    if os.path.exists(file):
        if os.path.getsize(file) > 0:
            with open(file, 'r') as file:
                data = json.load(file)
                for player in data:
                    print(f"Imie: {player['name']}")
                    print(f"Punkty: {player['points']}")
                    print()
        else:
            print("Brak wyników do wyświetlenia")
    else:
        print("Plik z punktami nie istnieje")


while True:
    print("1 - Pytania z danej kategorii")
    print("2 - Losowe pytania ze wszystkich kategorii")
    print("3 - Pokaż ranking punktów")
    print("4 - Wyjście")

    value = input("Wybierz opcje \n")

    try:
        value = int(value)
    except ValueError:
        print("Proszę wprowadzić prawidłową liczbę.")
        continue

    if value == 1:
        quiz_random.get_categories()
        category = input("Wprowadź nazwę kategorii: ")
        player_name = input("Podaj swój nick")
        quiz_category.play_quiz(category.lower(), player_name)
    elif value == 2:
        player_name = input("Podaj swój nick")
        quiz_random.play_quiz(player_name)
    elif value == 3:
        print("random - Ranking losowej kategorii")
        print("category - Ranking gry w kategoriach")

        value = input("Podaj kategorie rankingu ktora cie interesuje: \n").lower().strip()

        print_score(value)
    elif value == 4:
        print("Dziękujemy za grę!")
        break
    else:
        print("Nieprawidłowa opcja. Proszę spróbować ponownie.")
