class QuestionModel:
    def __init__(self, id, question, answer_list):
        self.id = id
        self.question = question
        self.answer_list = answer_list

    def __str__(self):
        return (
            f"Pytanie: {self.question}\n"
            f"Odpowiedzi: {self.answer_list}\n"
        )

    def __repr__(self):
        return str(self)

