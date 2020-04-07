from question import Question


class Parser:

    @staticmethod
    def ParseQuestionFile(path):
        f = open(path, "r")
        lines = f.readlines()
        f.close()
        questions = []

        for l in lines:
            if l.startswith('//') or l == "\n":
                continue


            questions.append(Question.FromReadLine(l))

        return questions
