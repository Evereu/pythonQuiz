class CategoryModel:
    def __init__(self, categoryName, question):
        self.categoryName = categoryName
        self.question = question

    def __str__(self):
        return f"Kategoria: {self.categoryName}\nPytanie: {self.question}"

    def __repr__(self):
        return str(self)

    def getCategories(self):
        return self.categoryName


