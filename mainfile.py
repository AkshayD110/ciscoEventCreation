####################################
# File name: mainfile.py           #
# Author: Akshay Deshpande         #
# Date created : 22nd May 2018     #
# Last modified : 6th June 2018    #
####################################


import threading
import eventCreator
from multiprocessing import Process
import time
from datetime import datetime

def main():
    number_of_msgsToCreate = int(input("How many messages do you want to create?"))
    start = time.time()
    eventCreator_obj = eventCreator.eventCreator(number_of_msgsToCreate)
    eventCreator_obj.msg_distribution()
    print(time.time() - start)
    logoutput(number_of_msgsToCreate)
    print("done")

def logoutput(eventsCreated):
    currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("eventCreatedlog.txt", "a") as myfile:
        myfile.write(f"\n wrote {eventsCreated} new messages on {currentDateTime}")


if __name__ == '__main__':
    main()
