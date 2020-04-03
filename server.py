from time import sleep
import inspect
from flask import Flask

from config import ServerConfig


class Server(Flask):
    def __init__(self, config, question_generator):
        self.Config = config
        super(Server, self).__init__(__name__)
        self.QuestionGenerator = question_generator
        self._init()

    def _init(self):
        for k, v in self.GetMethodMap().items():
            self.add_url_rule(k, handler=v)

    @property
    def c(self):
        return self.Config

    def Run(self):
        self.run(self.c.Host, self.c.Port)

    def GET_HelloWorld(self):
        return "Hello World"

    def GetMethodMap(self):
        """Format:
            key=route(str), value=method"""
        return {
            "/welcome":self.GET_HelloWorld()
        }