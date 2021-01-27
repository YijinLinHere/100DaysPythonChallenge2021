# from data import question_data
from data import question_data_tdb
from question_model import Question
from quiz_brain import QuizBrain

# get questions from https://opentdb.com/
# https://opentdb.com/api_config.php

if __name__ == '__main__':
    question_bank = []
    for question in question_data_tdb['results']:
        question_text = question['question']
        question_answer = question['correct_answer']
        new_qutsion = Question(question_text, question_answer)
        question_bank.append(new_qutsion)

    quiz_brain = QuizBrain(question_bank)
    
    while(quiz_brain.still_has_questions()):
        quiz_brain.next_question()   
        
    print("You completed the quiz!")
    print("Your final score was {}/{}".format(quiz_brain.score, quiz_brain.question_number))
    
    '''
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))

    quiz_brain = QuizBrain(question_bank) 
    
    while(quiz_brain.still_has_questions()):
        quiz_brain.next_question()   
        
    print("You completed the quiz!")
    print("Your final score was {}/{}".format(quiz_brain.score, quiz_brain.question_number))
    '''