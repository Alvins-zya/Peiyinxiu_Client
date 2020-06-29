from PyQt5.QtCore import *

class MyTypeSignal(QObject):
    sendmsg = pyqtSignal(object)

    def run(self):
        self.sendmsg.emit("Hello")

class MySlot(QObject):
    def get(self,msg):
        print('hhhh'+ msg)

if __name__=='__main__':
    send = MyTypeSignal()
    slot = MySlot()
    send.sendmsg.connect(slot.get)
    send.run()
    send.sendmsg.disconnect(slot.get)
    send.run()