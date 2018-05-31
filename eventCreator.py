####################################
# File name: eventCreator.py       #
# Author: Akshay Deshpande         #
# Date created : 22nd May 2018     #
# Last modified : 30th May 2018    #
####################################


from datetime import datetime
import sys
from ciscosparkapi import CiscoSparkAPI
import threading
from random import *

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

        t1 = threading.Thread(target=self.normaltext_msg(f"msg here : ", normaltext_count)).start()
        t2 = threading.Thread(target=self.markdowntext_msg(f"msg here : ", markdowntext_count)).start()
        t3 = threading.Thread(target=self.filetrasfer_msg(f"msg here : ", filetransfer_count)).start()
        t4 = threading.Thread(target=self.all_restricted_msgs()).start()

        #self.all_restricted_msgs()


    def normaltext_msg(self, text, count):
        for i in range(count):
            message = self.api.messages.create(self.roomid, text=f"some generic text here - {text} {i}")

    def markdowntext_msg(self, text, count):
        for i in range(count):
            message = self.api.messages.create(self.roomid, markdown=f"**some generic text here - {text} {i}**" )

    def filetrasfer_msg(self, text, count):
        for i in range(count):
            message = self.api.messages.create(self.roomid, text="some generic text here ", files=["http://hanassets.nd.gov/images/product/test.png"])


    def all_restricted_msgs(self):
        #Generates 40k restricted phrases and picks one
        listofphrase = [f'ThisIsABigResTrictedPhrase{x}' for x in range(1, 40000)]

        restrictedwords_count = round((self.msgcount * 1) / 100)
        restricted_normal = round((restrictedwords_count * 0.5) / 100)
        restricted_markdown = round((restrictedwords_count * 0.25) / 100)
        restricted_files =  round((restrictedwords_count * 0.25) / 100)
        print(f"Here are the rest_wordsCount :{restrictedwords_count}, rest_normal :{restricted_normal}, rest_markdown :{restricted_markdown}, rest_files :{restricted_files    }")

        for i in range(restricted_normal):
            restricted_word = choice(listofphrase)
            message = self.api.messages.create(self.roomid, text=f"some generic text here and restword : {restricted_word}")

        for i in range(restricted_markdown):
            restricted_word = choice(listofphrase)
            message = self.api.messages.create(self.roomid, text=f"**some generic text here and restword : {restricted_word}**")

        for i in range(restricted_files):
            restricted_word = choice(listofphrase)
            message = self.api.messages.create(self.roomid, text=f"some generic text here and restword : {restricted_word}")

        print("done with creating restricted phrases")

