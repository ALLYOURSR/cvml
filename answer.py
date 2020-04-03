

class Answer:
    def __init__(self, display_text):
        self.DisplayText = display_text

class StringAnswer(Answer):
    def __init__(self, display_text):
        super(StringAnswer, self).__init__(display_text)