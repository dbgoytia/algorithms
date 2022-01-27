class QuizBrain:


    def __init__(self, question_bank:list) -> None:
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0


    def next_question(self) -> str:
        q = self.questions_list[self.question_number]
        q_text = q.text
        self.question_number += 1
        answer = input(f'Q.{self.question_number} {q_text} (True/False)?: ')
        self.check_answer(answer, q.answer)
        return answer
    

    def has_next_question(self) -> bool:
        return self.question_number < len(self.questions_list)

    
    def check_answer(self, user_answer:str, correct_answer:str) -> None:
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else: 
            print('That is wrong.')
            print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')

    

    