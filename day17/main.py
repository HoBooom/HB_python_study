from question_model import QuestionModel
from data import questions
from quiz_brain import QuizBrain

questions_list = []
for _,quiz_set in enumerate(questions):
    question_set = QuestionModel(quiz_set["quiz"], quiz_set["ans"])
    questions_list.append(question_set)

#print(*questions_list, sep="\n")
quiz_game = QuizBrain(questions_list)
while quiz_game.still_has_questions():
    quiz_game.show_question()