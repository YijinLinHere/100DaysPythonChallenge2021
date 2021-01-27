from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# get questions from https://opentdb.com/
# https://opentdb.com/api_config.php

if __name__ == '__main__':
    
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))

    quiz_brain = QuizBrain(question_bank) 
    
    while(quiz_brain.still_has_questions()):
        quiz_brain.next_question()   
        
    print("You completed the quiz!")
    print("Your final score was {}/{}".format(quiz_brain.score, quiz_brain.question_number))
    