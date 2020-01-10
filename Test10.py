#coding = utf-8
import time
from Peiyinxiu_Client.Test import Chat_notices
from Peiyinxiu_Client.Test2 import device

def test():
    Chat_notices()
    time.sleep(2)
    device()
    time.sleep(2)


if __name__=="__main__":
    for i in range(4):
        test()