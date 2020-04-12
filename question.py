from typing import List

from answer import Answer, StringAnswer, RangeAnswer


class Question:
    def __init__(self, text:str, id:int, answers:List[Answer]):
        self._text = text
        self._id = id
        self._answers = answers

    @staticmethod
    def ParseLine(raw_line:str):
        """Eventually this will automagically select between different subclasses"""
        print("Parsing {}".format(raw_line))

        id_txt__answers = raw_line.split('[')
        index = int(id_txt__answers[0].split()[0])
        text = id_txt__answers[0][id_txt__answers[0].find(' '):] #Grab all text after first space
        ans_text = id_txt__answers[1]
        ans_text = ans_text.split(']')[0]

        answers = []

        """Expected format: 'ANSWER1 | ANSWER2 | ANSWERN"""
        if ans_text.find('|') == -1:
           answers = [Answer.Parse(ans_text)]
        else:
            for a in ans_text.split(']')[0].split('|'):
                answers.append(Answer.Parse(a.strip()))

        return Question(text, index, answers)
