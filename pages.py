from enum import Enum
from typing import List

from flask import Flask, jsonify
from OpenSSL import SSL

from question import Question
from serialization.utils import PackOne

context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')




app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)



class PageTypes(Enum):
    WelcomePage=0,
    StartPage=1,
    SurveyPage=2,
    EndPage=3,
    AboutPage=4

class PackableList(list):
    def __init__(self, list_):
        """list_ members must have method _pack()"""
        super(PackableList, self).__init__(list_)

    def _pack(self):
        return [i._pack() for i in self]

"""Abstract class
In derived classes, automatically serializes any properties with names of the format JSON_[key_name]=key_value"""
class PageData(dict):
    def __init__(self, page_type:PageTypes, version_string:str):
        super(PageData, self).__init__({"page_type":page_type})
        self.JSON_page_type = page_type
        self.JSON_version_string = version_string

    @property
    def PageType(self):
        """Redonly! Go away!"""
        return self._page_type

    def Pack(self, msg_dict):
        atr = [a for a in self.__dict__.keys() if a.startswith("JSON_")]
        for a in atr:
            elem = self.__dict__[a]
            pack_name = a[5:]
            PackOne(self, pack_name, elem)

        msg_dict["page_data"] = self


class WelcomePageData(PageData):
    def __init__(self, welcome_text:str, version_string:str):
        super(WelcomePageData, self).__init__(PageTypes.Welcome, version_string)
        self.JSON_welcome_string = welcome_text

class StartPageData(PageData):
    def __init__(self, start_page_text:str, version_string:str):
        super(StartPageData, self).__init__(PageTypes.StartPage, version_string)
        self.JSON_start_page_string = start_page_text

class SurveyPageData(PageData):
    def __init__(self, survey_page_no:int, questions:List[Question], version_string:str):
        super(SurveyPageData, self).__init__(PageTypes.Welcome, version_string)
        self.JSON_survey_page_number_int = survey_page_no
        self.JSON_questions = questions
