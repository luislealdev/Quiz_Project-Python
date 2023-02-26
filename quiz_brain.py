class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        self.question_number +=1
        user_answer = input("Q."+ str(self.question_number) + " " + self.question_list[self.question_number].text+" (True/False)")