from ciscosparkapi import CiscoSparkAPI
import sys
import eventCreator

def main():
    try:
        msg_count = int("Enter the number of messages you want to create")
    except ValueError:
        print("Please enter an int value")

    eventCreator_obj = eventCreator.eventCreator(msg_count)
    eventCreator_obj.msg_distribution()