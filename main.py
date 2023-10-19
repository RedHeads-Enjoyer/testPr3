class Question:
    def __init__(self, question, answers):
        if question[-1] != '?':
            question += '?'
        self.question = question
        self.answers = answers

    def getAnswers(self):
        return self.answers

    def getQuestion(self):
        return self.question