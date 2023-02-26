from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
questions = []

for question in question_data:
    questions.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(questions)
quiz_brain.next_question()  