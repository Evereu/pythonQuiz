class AnswerModel:
    def __init__(self, option, answer, correctness):
        self.option = option
        self.answer = answer
        self.correctness = correctness

    def __str__(self):

        return f"{self.option} - {self.answer}\n" #({self.correctness})

    def __repr__(self):
        return str(self)
