class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.question_number = 0
        self.points = 0

    def show_question(self):
        ans = input(f"Q {self.question_number}. {self.q_list[self.question_number].question} (True/False) ? : ")
        self.is_answer(ans, self.question_number)
        self.question_number += 1

    def print_ans(self,question_number):
        print(f"The correct answer is: {self.q_list[question_number].answer}")
        print(f"Your current score is: {self.points} / {self.question_number + 1}.")

    def is_answer(self,answer,question_number):
        if answer == self.q_list[question_number].answer:
            print("You got it right!")
            self.points += 1
        else:
            print("You got it wrong!")
        self.print_ans(question_number)
        print()


    def still_has_questions(self):
        return self.question_number < len(self.q_list)