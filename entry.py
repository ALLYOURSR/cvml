from config import ServerConfig
from question_generator import QuestionGenerator
from server import Server

c = ServerConfig()
qg = QuestionGenerator(c.QuestionFilepath)
qg.PrintAll()

s = Server(c, qg)
s.Run()