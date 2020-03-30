




class UserSession:
    def __init__(self, id):
        self._id = id #Needs to be generated as a hash that stays constant per user. Researching.

        self._question_indices = []#indices which index into QuestionGenerator master question list