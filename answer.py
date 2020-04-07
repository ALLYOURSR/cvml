from abc import abstractmethod
from enum import Enum
from typing import List


class Answer:
    def __init__(self, display_text):
        self.DisplayText = display_text

    def Pack(self):
        raise NotImplementedError("Answer.Pack is an abstract class")
        pass

class StringAnswer(Answer):
    def __init__(self, display_text:str):
        super(StringAnswer, self).__init__(display_text)

class CustomAnswer(Answer):
    def __init__(self, display_text:str):
        super(CustomAnswer, self).__init__(display_text)

class NumericalAnswer(Answer):
    def __init__(self, raw_text:str):
        super(NumericalAnswer, self).__init__(display_text)


class RangeAnswer(Answer):
    def __init__(self, min:int, max:int):
        super(RangeAnswer, self).__init__("")
        self.Min = min
        self.Max = max


class CustomAnswer(Answer):
    def __init__(self, display_text:str):
        super(StringAnswer, self).__init__(display_text)

class NumericalAnswer(Answer):
    def __init__(self, display_text:str):
        super(StringAnswer, self).__init__(display_text)

    @staticmethod
    def Parse(raw_text:str):
        """Expected format: 'ANSWER1 | ANSWER2 | ANSWERN"""
        if not a.contains('|'):
            sp = a.split('-')
            if len(sp) != 2:
                raise SyntaxError("Error parsing line {}. Attempted to parse range [min-max]".format(line_no))
            else:
                return RangeAnswer(int(sp[0]), int(sp[1]))

        ans = raw_text.split('|')
        ans = [a.strip() for a in ans]



        for line_no, a in enumerate(ans):
            if not (a.contains('_') or a.contains('(')): return StringAnswer(a)
            elif a == '_': return CustomAnswer(a)
            elif a == '_+': return MultiCustomAnswer(a)
            elif a == '_#': return CustumNumericalAnswer(a)