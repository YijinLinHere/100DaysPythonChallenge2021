class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        # a simplifier statement!
        return self.question_number < len(self.question_list)
    
    def check_answer(self, u_ans, q_ans):
        if u_ans.lower() == q_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's a wrong answer.")
        print("The correct answer is {}".format(q_ans))
        print("Your current score is {}/{}".format(self.score, self.question_number))
        print("\n")

    def next_question(self):
        q_text = self.question_list[self.question_number].text
        q_ans = self.question_list[self.question_number].answer

        self.question_number += 1
        user_ans = input("Q.{}: {} (True/False).? ".format(self.question_number, q_text))

        self.check_answer(user_ans, q_ans)

        


