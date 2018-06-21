# ciscoEventCreation

This project is meant to create a messages of different kinds in Cisco Webex chat rooms.
It takes three parameters :
- user access token [as a sys arg]
- room id [as a sys arg]
-- Number of messages to create given as user input param

This tool can create messages at the rate of 150/minute.

Optimizations required :
- A logging mechanism to check how many messages where created before any error occurs.
    -- completed : checked in on 7th June
- Make changes to pick random lines from a file
- Make it pick all the configurations from the property file
    - messages count is picked from config file now
- Make the changes to include restricted phrase randomly in-between rather than all at once.
- Include test cases and unit tests