#recipient-id = Recipient's Facebook ID
#sender-id    = Sender's Facebook Login E-mail
#sender-passwd= Sender's Facebook Login password

from fbchat import log, Client
from fbchat.models import *
def sendmessage(message):
    client = Client("sender-id", "sender-passwd")
    client.send(Message(text=message), thread_id="recipient-id", thread_type=ThreadType.USER)
    client.logout()

name_keywords = ['What is your name?',"What's your name"]
thanks_keywords = ['Thanks','thanks']
hello_keywords = ['Hello','hello','Hi','hi']

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        log.info("{} from {} in {}".format(message_object, "recipient-id", thread_type.name))
        if author_id != self.uid:
            messagefb=str(message_object.text)
            if messagefb in name_keywords :
                sendmessage('My name is MessBot !')
                print("respont sent") #For debugging
            elif messagefb in thanks_keywords :
                sendmessage("You're Welcome !")
                print("respont sent") #For debugging
            elif messagefb in hello_keywords :
                sendmessage("You're Welcome !")
                print("Hi There !") #For debugging
            else:
                print("I can not understand")

client = EchoBot("sender-id", "sender-passwd")
client.listen()