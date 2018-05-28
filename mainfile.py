
import eventCreator

def main():
    number_of_msgsToCreate = int(input("How many messages do you want to create?"))

    eventCreator_obj = eventCreator.eventCreator(number_of_msgsToCreate)
    eventCreator_obj.msg_distribution()

if __name__ == '__main__':
    main()