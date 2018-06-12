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
    time_taken = time.time() - start #line 17 and line20 account the time taken between them.
    print(time_taken)
    logoutput(number_of_msgsToCreate, time_taken)
    print("done")

def logoutput(eventsCreated, time_taken):
    currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("eventCreatedlog.txt", "a") as myfile:
        myfile.write(f"\n Wrote {eventsCreated} new messages on {currentDateTime}. Took {time_taken}secs of time to complete")


if __name__ == '__main__':
    main()
