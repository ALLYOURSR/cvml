from question import Question


class Parser:

    @staticmethod
    def ParseQuestionFile(path):
        f = open(path, "r")
        lines = f.readlines()
        f.close()
        questions = []

        for l in lines:
            questions.append(Question.FromReadLine(l))

        return questions
