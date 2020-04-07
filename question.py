from typing import List

from answer import Answer, StringAnswer


class Question:
    def __init__(self, text:str, answers:List[Answer]):
        self._text = text
        self.answers = answers

    @staticmethod
    def Parse(raw_line:str):
        """Eventually this will automagically select between different subclasses"""
        ind_txt__answers = raw_line.split('[')
        index = int(ind_txt__answers[0])
        text = ind_txt__answers[1]
        answers = ind_txt__answers[2]
        answers = answers.split(']')[0]

        Answer.Parse(answers)



        print("Parsing {}".format(raw_line))
        return Question("Parsing isn't set up yet", [StringAnswer("OK"), StringAnswer("Not OK")])
