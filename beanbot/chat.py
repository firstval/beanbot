import xmpp

try:
    from local_settings import *
except ImportError:
    raise Exception("You need a local_settings.py file!")

def send_jabber_message(messagebody):
    client = xmpp.Client(JABBER_SERVER)
    client.connect(server=(JABBER_SERVER, JABBER_PORT))
    client.auth(JABBER_USER,JABBER_PASS,JABBER_NAME)
    client.sendInitPresence()
    client.send(xmpp.Presence(to="%s/%s" % (JABBER_ROOM, JABBER_NAME)))
    message = xmpp.protocol.Message(body=messagebody)
    message.setTo(JABBER_ROOM)
    message.setType('groupchat')
    client.send(message)