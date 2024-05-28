import json
import os
import platform
import random
from Models.AnswerModel import AnswerModel
from Models.QuestionModel import QuestionModel
from Models.CategoryModel import CategoryModel


class QuizByCategory:

    def get_all_questions_from_json(self, selected_category):

        categoryyy = []

        with open('questions.json', 'r', encoding="utf-8") as file:
            data = json.load(file)

            for category in data['categories']:
                if category['categoryName'] == selected_category:
                    question = category['question']
                    id = category['id']
                    answer_list = []
                    for answer in category["answers"]:
                        answer_list.append(AnswerModel(answer['option'], answer['text'], answer['correct']))

                        quest = QuestionModel(id, question, answer_list)

                    categoryyy.append(CategoryModel(category['categoryName'], quest))

        return categoryyy

    def save_score(self, name, score):

        with open('score.json', 'r') as file:
            data = json.load(file)

        print(data)

        new_score = {"name": name, "points": score}
        data.append(new_score)

        with open('score.json', 'w') as file:
            json.dump(data, file, indent=4)

    def play_quiz(self, selected_category):

        all_questions = self.get_all_questions_from_json(selected_category)
        points = 0

        while all_questions:
            random_category = random.choice(all_questions)

            question = random_category.question

            print(question.question)
            for i in range(len(question.answer_list)):
                print(question.answer_list[i], end='')

            while True:
                user_answer = input("Wybierz poprawną odpowiedź (wpisz literę): ").strip().lower()

                for answer in question.answer_list:
                    if answer.option == user_answer:
                        if answer.correctness:
                            points += 1
                            print("Poprawna odpowiedź")
                        else:
                            print("Niepoprawna odpowiedź.")
                        break
                else:
                    print("Taka odpowiedz nie istnieje")
                    continue
                break
            all_questions.remove(random_category)

        self.save_score("kot", points)

        print(f"Liczba punktów: {points}")



