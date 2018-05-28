from datetime import datetime
import sys
from ciscosparkapi import CiscoSparkAPI

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

    access_token = "Bearer "+str(sys.argv[1])
    print(access_token)
    room_id = sys.argv[2]
    print(room_id)

    def msg_distribution(self):
        normaltext_count = round((self.msgcount*80)/100)
        markdowntext_count = round((self.msgcount*17.5)/100)
        filetransfer_count = round((self.msgcount*1.5)/100)
        self.all_restricted_msgs()
        print(f"normal text will be : {normaltext_count}, markdown text will be : {markdowntext_count}, file transfer count will be :{filetransfer_count}")

    def normaltext_msg(self, text):
        pass

    def markdowntext_msg(self, text):
        pass

    def filetrasfer_msg(self, text):
        pass

    def all_restricted_msgs(self):
        restrictedwords_count = round((self.msgcount * 1) / 100)
        restricted_normal = round((restrictedwords_count * 0.5) / 100)
        restricted_markdown = round((restrictedwords_count * 0.25) / 100)
        restricted_files =  round((restrictedwords_count * 0.25) / 100)
        print(f"this is restricted phrase section : {restrictedwords_count}")




