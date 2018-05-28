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
        pass

    def normaltext_msg(self):
        pass

    def markdowntext_msg(self):
        pass

    def filetrasfer_msg(self):
        pass



