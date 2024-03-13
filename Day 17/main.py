from quiz_brain import QuizBrain

quiz_brain = QuizBrain()

for question in quiz_brain.questions:
    quiz_brain.pop_question()
    quiz_brain.check_answer()
