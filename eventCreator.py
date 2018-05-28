from datetime import datetime
import sys

class eventCreator:

    def __init__(self, msg_count):
        self.msg_count = msg_count

    def __repr__(self):
        return f'{self.__class__.__name__} class creates events in the Cisco Spark'

    @property
    def msg_count(self):
        return self._msg_count

    @msg_count.setter
    def msg_count(self, msg_count):
        self._msg_count
        """include validation - is input a digit or not """

    access_token = "Bearer "+str(sys.argv[1])
    room_id = sys.argv[2]

    def msg_distribution(self):
        normaltext_count = round((self.msg_count*80)/100)
        markdowntext_count = round((self.msg_count*17.5)/100)
        filetransfer_count = round((self.msg_count*1.5)/100)
        self.all_restricted_msgs()


    def normaltext_msg(self, text):
        pass

    def markdowntext_msg(self, text):
        pass

    def filetrasfer_msg(self, text):
        pass

    def all_restricted_msgs(self):
        restrictedwords_count = round((self.msg_count * 1) / 100)
        restricted_normal = round((restrictedwords_count * 0.5) / 100)




