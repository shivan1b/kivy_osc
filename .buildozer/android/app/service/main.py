import sys, os; sys.path = [os.path.join(os.getcwd(),"..", "_applibs")] + sys.path
'''
Service
'''

from time import sleep
from kivy.lib import osc

service_port = 8000
activity_port = 8008

def my_callback(message, *args):
    print "Service callback message ", message[2]
    reply_to_activity()

def reply_to_activity():
    osc.sendMsg('/message',
        ['Service: Hi!', ],
        port=activity_port,
        typehint=None)

if __name__ == '__main__':
    '''
    OSC
    ===
    * Open Sound Control protocol
      (Read: https://en.wikipedia.org/wiki/Open_Sound_Control)
    * Connectionless
    * Can be used not just for networking sound but P2P communication

    OSC flow:
    --------------
    | Initialize |
    --------------
           |
    --------------
    |   Listen   |  <-- Set the ip Address and port to listen to
    --------------
           |
    --------------
    |    Bind    |  <-- Bind the osc ID
    --------------

    '''
    osc.init()
    osc_id = osc.listen(ipAddr='127.0.0.1', port=service_port)
    osc.bind(osc_id, my_callback, '/message')


    # Keep on listening for messages regularly
    while True:
        osc.readQueue(osc_id)
        sleep(.5)