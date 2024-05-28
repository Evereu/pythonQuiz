from RandomQuestionQuiz import RandomQuestionQuiz
from CategoryQuestions import QuizByCategory

quiz_category = QuizByCategory()
quiz_random = RandomQuestionQuiz()

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
        quiz_category.play_quiz(category.lower())
    elif value == 2:
        quiz_random.play_quiz()
    elif value == 3:
        print("das")

    elif value == 4:
        print("Dziękujemy za grę!")
        break
    else:
        print("Nieprawidłowa opcja. Proszę spróbować ponownie.")
