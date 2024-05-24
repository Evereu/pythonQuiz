from Models import CategoryModel
from RandomQuestionQuiz import RandomQuestionQuiz
from CategoryQuestions import QuizByCategory


quiz_category = QuizByCategory()
quiz_random = RandomQuestionQuiz()

print("1 - Pytania z danej kategorii")
print("2 - Losowe pytania ze wszystkich kategorii")

value = input("Wybierz opcje \n")

try:
    value = int(value)
except Exception:
    print("Proszę wprowadzić prawidłową liczbę.")
    exit(1)

if value == 1:
    quiz_random.get_categories()
    category = input("Wprowadź nazwę kategorii")
    quiz_category.play_quiz(category.lower())

elif value == 2:
    RandomQuestionQuiz().play_quiz()


