import threading
import eventCreator
from multiprocessing import Process

def main():
    number_of_msgsToCreate = int(input("How many messages do you want to create?"))

    eventCreator_obj = eventCreator.eventCreator(number_of_msgsToCreate)
    eventCreator_obj.msg_distribution()
    print("done")

if __name__ == '__main__':
    # t1 = threading.Thread(target=main())
    # t2 = threading.Thread(target=main())
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

    main()
