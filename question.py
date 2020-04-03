from typing import List

from answer import Answer, StringAnswer


class Question:
    def __init__(self, text:str, answers:List[Answer]):
        self._text = text
        self.answers = answers

    @staticmethod
    def FromReadLine(raw_line:str):
        """Eventually this will automagically select between different subclasses"""
        print("Parsing {}".format(raw_line))
        return Question("Parsing isn't set up yet", [StringAnswer("OK"), StringAnswer("Not OK")])
