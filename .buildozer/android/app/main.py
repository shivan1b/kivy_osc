'''
Activity
'''

from kivy.app import App
from kivy.utils import platform
from kivy.lib import osc
from kivy.clock import Clock
from kivy.uix.button import Button

activity_port = 8008
service_port = 8000

class MyActivity(App):
    '''
    Defines the actions to be performed by Activity
    '''
    def build(self):
        if platform == 'android':
            from android import AndroidService
            service = AndroidService('My Activity', 'running')
            service.start('service started')
            self.service = service
        
        osc.init()
        osc_id = osc.listen(ipAddr='127.0.0.1', port=activity_port)
        osc.bind(osc_id, self.my_callback, '/message')

        # Listen for messages regularly
        Clock.schedule_interval(lambda *x: osc.readQueue(osc_id), 0)

        btn = Button(text='Push me to see OSC working')
        btn.bind(on_release=self.send_msg_to_service)
        return btn

    def my_callback(self, message, *args):
        print "Activity callback message ", message[2]
    
    def send_msg_to_service(self, instance):
        '''
        Send message to the service
        '''
        osc.sendMsg('/message',
            ['Activity: Hey there', ],
            port=service_port,
            typehint=None)


if __name__ == '__main__':
    MyActivity().run()