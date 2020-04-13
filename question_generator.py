from parser_ import Parser

class QuestionGenerator:
    def __init__(self, user_session:UserSession, question_filepath:str):
        self._questions = []
        self._questionIndices = []
        self._init(question_filepath)

    def _init(self, question_filepath):
        self._questions = Parser.ParseQuestionFile(question_filepath)
        self._questionIndices = range(len(self._questions))

    def GetBatch(self, start:int, stop:int):
        return self._questions[start: stop]

    def PrintAll(self):
        for q in self._questions:
            print("===========")
            print("{}. {} ".format(q._id, q._text))
            for a in q._answers:
                print(a.DisplayText)