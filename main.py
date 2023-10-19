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


class Player:
    def __init__(self, name, checkpoint):
        self.name = name
        self.score = 0
        if (checkpoint <= 0 or checkpoint >= 6):
            self.checkpoint = 3
        else:
            self.checkpoint = checkpoint

    def addScore(self, number):
        self.score += number

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def getCheckpoint(self):
        return self.checkpoint