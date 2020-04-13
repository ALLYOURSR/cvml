from pages import WelcomePageData
from state.user_session import UserSession


class PageGenerator:
    def __init__(self, config, question_generator):
        self.QuestionGenerator = question_generator
        self.Config = config

    def Generate(self, user_session:UserSession):
        pg = user_session.CurrentPage

        if pg == 0:
            return WelcomePageData(self.Config.WelcomeText, self.Config.VersionString)
        elif pg == 1:
                