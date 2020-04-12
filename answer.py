from abc import abstractmethod
from enum import Enum
from typing import List


class Answer:
    def __init__(self, display_text):
        self.DisplayText = display_text

    def Pack(self):
        raise NotImplementedError("Answer.Pack is an abstract class")
        pass

    @staticmethod
    def Parse(raw_text: str):
        a = raw_text

        if a.find('-') != -1 and a.find('(') != -1:
            text = a.split('(')[0].strip()
            sp = a.split('(')[1].split('-')
            if len(sp) != 2:
                raise SyntaxError("Error parsing line. Attempted to parse range [min-max]")
            else:
                return(RangeAnswer(text, float(sp[0]), float(sp[1].rstrip(')'))))
        elif a.find('-') != -1:
            sp = a.split('-')
            if len(sp) != 2:
                raise SyntaxError("Error parsing line. Attempted to parse range [min-max]")
            else:
                return (RangeAnswer("", float(sp[0]), float(sp[1].rstrip(')'))))

        if not (a.find('_') == 1 or a.find('(') == 1):
            return StringAnswer(a)
        elif a == '_':
            return CustomAnswer(a)
        elif a == '_+':
            return MultiCustomAnswer(a)
        elif a == '_#':
            return CustumNumericalAnswer(a)

class StringAnswer(Answer):
    def __init__(self, display_text:str):
        super(StringAnswer, self).__init__(display_text)

class CustomAnswer(Answer):
    def __init__(self, display_text:str):
        super(CustomAnswer, self).__init__(display_text)

class NumericalAnswer(Answer):
    def __init__(self, display_text:str):
        super(NumericalAnswer, self).__init__(display_text)


class RangeAnswer(Answer):
    def __init__(self, text, min:int, max:int):
        super(RangeAnswer, self).__init__(text)
        self.Min = min
        self.Max = max


class MultiCustomAnswer(Answer):
    def __init__(self, display_text:str):
        super(MultiCustomAnswer, self).__init__(display_text)

class CustumNumericalAnswer(Answer):
    def __init__(self, display_text:str):
        super(CustumNumericalAnswer, self).__init__(display_text)

