from parser_ import Parser

class QuestionGenerator:
    def __init__(self, question_filepath:str):
        self._questions = None
        self._questionIndices = []
        self._init(question_filepath)

    def _init(self, question_filepath):
        self._questions = Parser.ParseQuestionFile(question_filepath)
        self._questionIndices = range(len(self._questions))

    def GetBatch(self, start:int, stop:int):
        return self._questions[start: stop]