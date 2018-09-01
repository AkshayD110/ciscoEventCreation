# ciscoEventCreation

This project is meant to create a messages of different kinds in Cisco Webex chat rooms.
It takes three parameters :
- The total number of messages that you want to create accross all the rooms. In config file.
- room id - which is taken as an array in config file

This tool can create messages at the rate of 150/minute.

New changes included :
- Supports multiroom data creation.
- A logging mechanism has been included to give the rate at which messages are created.
- User id has been included in config file rather than sys.arg file.
- Many other parameters handle within the code are moved to config file

Optimizations required :
- Make changes to pick random lines from a file
- Make the changes to include restricted phrase randomly in-between rather than all at once.
- Include test cases and unit tests
- Include the comments for code sections