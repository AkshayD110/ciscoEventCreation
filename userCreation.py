from ciscosparkapi import CiscoSparkAPI

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

    
