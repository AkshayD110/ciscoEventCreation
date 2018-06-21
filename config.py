# This file contains all the config parameters to be read and used for the script

totalmessages = 2
normaltext_count = round((totalmessages * 80) / 100)
markdowntext_count = round((totalmessages * 17.5) / 100)
filetransfer_count = round((totalmessages * 1.5) / 100)
restrictedwords_count = round((totalmessages * 1) / 100)


INPUT_CONFIG = {
    'accesstoken': '<-User Access Token here->',
    'roomid': '<-Id of the room here->',
    'Total_messages_to_create': totalmessages,
    'normal_messages': normaltext_count,
    'markdowntext_messages': markdowntext_count,
    'filetransfer_messages': filetransfer_count,
    'restricted_messages': restrictedwords_count,

}