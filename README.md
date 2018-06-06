# ciscoEventCreation

This project is meant to create a messages of different kinds in Cisco Webex chat rooms.
It takes three parameters :
- user access token [as a sys arg]
- room id [as a sys arg]
-- Number of messages to create given as user input param

This tool can create messages at the rate of 150/minute.

Optimizations required :
- A logging mechanism to check how many messages where created before any error occurs.