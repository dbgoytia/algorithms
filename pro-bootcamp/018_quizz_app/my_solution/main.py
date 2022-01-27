# std library

# third party modules

# custom modules
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def ui() -> None:
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))

    quizbrain = QuizBrain(question_bank)

    while quizbrain.has_next_question():
        quizbrain.next_question()

    print("Quiz completed!")
    print(f"Your score is: {quizbrain.score}/{len(question_bank)}")

if __name__ == '__main__':
    ui()