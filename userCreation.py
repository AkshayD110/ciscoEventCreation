from ciscosparkapi import CiscoSparkAPI
import config
from random import choice
import time

class userCreation:
    def __init__(self, usercount):
        self.usercount = usercount

    def __repr__(self):
        return f'{self.__class__.__name__} class created in CiscoEventCreation'

    @property
    def usercount(self):
        return self._usercount

    @usercount.setter
    def usercount(self, usercount):
        self._usercount=usercount

    roomid = config.roomids
    api = CiscoSparkAPI(access_token=config.userid)

    def createUsers(self):
        usercount=config.INPUT_CONFIG['usercount']
        for i in range(usercount):
            currentroom = choice(self.roomid)
            user = self.api.memberships.create(roomId=currentroom, personEmail=f"dumyneww{i}@actiance.com", isModerator=False)
            time.sleep(2)




