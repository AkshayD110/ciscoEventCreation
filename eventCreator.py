from datetime import datetime
import sys
from ciscosparkapi import CiscoSparkAPI
from multiprocessing import Process

class eventCreator:

    def __init__(self, msgcount):
        self.msgcount = msgcount

    def __repr__(self):
        return f'{self.__class__.__name__} class creates in the Events in CiscoSpark'

    @property
    def msgcount(self):
        return self._msgcount

    @msgcount.setter
    def msgcount(self, msgcount):
        self._msgcount = msgcount


    # include the details in property file
    accesstoken = "Bearer " + str(sys.argv[1])
    roomid = sys.argv[2]
    api = CiscoSparkAPI(access_token=sys.argv[1])
    #demo_room = api.rooms.get(room_id)


    def msg_distribution(self):
        normaltext_count = round((self.msgcount*80)/100)
        markdowntext_count = round((self.msgcount*17.5)/100)
        filetransfer_count = round((self.msgcount*1.5)/100)
        print(f"normal text will be : {normaltext_count}, markdown text will be : {markdowntext_count}, file transfer count will be :{filetransfer_count}")

        self.normaltext_msg(f"msg here : ", normaltext_count)
        self.markdowntext_msg(f"msg here : ", markdowntext_count)
        self.filetrasfer_msg(f"msg here : ", filetransfer_count)

        #self.all_restricted_msgs()


    def normaltext_msg(self, text, count):
        for i in range(count):
            message = self.api.messages.create(self.roomid, text=f"This is new - {text} {count}")

    def markdowntext_msg(self, text, count):
        for i in range(count):
            message = self.api.messages.create(self.roomid, markdown=f"**This is new - {text} {count}**" )

    def filetrasfer_msg(self, text, count):
        for i in range(count):
            message = self.api.messages.create(self.roomid, text="welcome to Python", files=["http://hanassets.nd.gov/images/product/test.png"])


    def all_restricted_msgs(self):
        dlp_phrases = ["stock", "salary", "compensation", "money"] #this list needs to be expanded
        restrictedwords_count = round((self.msgcount * 1) / 100)
        restricted_normal = round((restrictedwords_count * 0.5) / 100)
        restricted_markdown = round((restrictedwords_count * 0.25) / 100)
        restricted_files =  round((restrictedwords_count * 0.25) / 100)
        print(f"this is restricted phrase section : {restrictedwords_count}")

