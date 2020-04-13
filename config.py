
class ServerConfig:
    def __init__(self):
        self.Host = "LocalHost"
        self.Port = "6666"
        self.Name = "CVML_0.0"
        self.QuestionFilepath = "./questions.txt"

        #UI stuff
        self.QuestionsPerPage = 5

        self.WelcomeMessage = "Please answer the following questions to the best of your ability. Your responses will be used to study the COVID-19 outbreak. All collected data is anonymous and will not be used for any other purpose or sold."

