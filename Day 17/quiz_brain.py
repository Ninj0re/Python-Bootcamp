from data import question_data as data
from question import Question


class QuizBrain:
    def __init__(self):
        self.questions = [None] * len(data)
        self.length = 0
        self.count = 0

        for q in data:
            self.questions[self.length] = Question(q["text"], q["answer"])
            self.length += 1

    def pop_question(self):
        if not self.count > self.length:
            print(self.questions[self.count].text)
            self.count += 1
        else:
            print("Out of questions!!")

    def check_answer(self):
        string = input("What is your answer? ")

        if string == self.questions[self.count-1].answer:
            print("You are correct!")
        else:
            print("You are incorrect!")
