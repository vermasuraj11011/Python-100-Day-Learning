import html


class Quiz:
    def __init__(self, q_bank):
        self.q_no = 0
        self.q_list = q_bank
        self.score = 0
        self.current_question = None

    def still_has_question(self):
        return self.q_no < len(self.q_list)

    def next_question(self):
        self.current_question = self.q_list[self.q_no]
        self.q_no += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.q_no}: {q_text}"

    def check_ans(self, user_ans):
        if user_ans.lower() == self.current_question.ans.lower():
            self.score += 1
            return True
        else:
            return False
