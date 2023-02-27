from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
questions = []

for question in question_data:
    questions.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(questions)
while quiz_brain.still_has_question():
    quiz_brain.next_question() 

print("You have completed the quiz!")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")