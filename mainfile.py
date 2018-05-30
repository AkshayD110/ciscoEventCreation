import threading
import eventCreator
from multiprocessing import Process
import time

def main():
    number_of_msgsToCreate = int(input("How many messages do you want to create?"))
    start = time.time()
    eventCreator_obj = eventCreator.eventCreator(number_of_msgsToCreate)
    eventCreator_obj.msg_distribution()
    print(time.time() - start)
    print("done")

if __name__ == '__main__':
    main()
