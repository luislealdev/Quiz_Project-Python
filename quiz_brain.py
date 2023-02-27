class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input("Q."+ str(self.question_number+1) + " " + current_question.text+" (True/False)")
        self.check_answer(user_answer, current_question.answer)
        self.question_number +=1
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You got it right :P")
        else:
            print(f"That's wrong ;(, the correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("\n")