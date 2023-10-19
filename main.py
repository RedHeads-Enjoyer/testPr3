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


class Game:
    def start(self):
        rewards = [100, 200, 300, 500]

        questions = []
        questions.append(Question('Какой сейчас год?', ['2000', '2020', '*2023', '2030']))
        questions.append(Question('2 + 2 = _ ?', ['1', '2', '3', '*4']))
        questions.append(Question('Кто первый полетел в космос?', ['*Гагарин', 'Михалков', 'Стивен Кинг', 'Ди Каприо']))
        questions.append(Question('Какого цвета трава?', ['Синяя', 'Красная', 'Черная', '*Зеленая']))

        player = Player('Дима', 6)

        for i in range(4):
            print(f'\nРаунд {i + 1}')
            print(f'У вас {player.getScore()} очков')
            print(questions[i].getQuestion())
            answers = questions[i].getAnswers()
            for j in range(1, 5):
                if answers[j - 1][0] == '*':
                    print(f'{j}. {answers[j - 1][1:]}')
                else:
                    print(f'{j}. {answers[j - 1]}')
            answer = input('Введите вариант ответа (1-4): ')
            while (answer == '' or int(answer) < 1 or int(answer) > 4):
                answer = input('Я же сказал 1-4: ')
            answer = int(answer)
            if answers[answer-1][0] == '*':
                print(f'Поздравляю! Вы ответили верно! Получено {rewards[i]} очков')
                player.addScore(rewards[i])
            elif i >= player.getCheckpoint() - 1:
                print(f'Вы дали неверный ответ, но дошли до несгараемой суммы, вы забираете {sum(rewards[:player.getCheckpoint()])} деняк')
                break
            else:
                print('Вы дали неверынй ответ и не дошли до несгараемой суммы, вы забираете 0 деняк')
                break
        else:
            print(f'Поздравляю, вы верно ответили на все вопросы и забираете {sum(rewards)} деняк')