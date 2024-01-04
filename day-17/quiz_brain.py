class Quiz:
    def __init__(self, q_bank):
        self.q_no = 0
        self.q_list = q_bank
        self.score = 0

    def still_has_question(self):
        return self.q_no < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_no]
        self.q_no += 1
        user_ans = input(f"Q.{self.q_no}: {current_question.text} (True/False): ")
        if user_ans.lower() == current_question.ans.lower():
            self.score += 1
