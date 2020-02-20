#coding=utf-8
'''
create on 2020年2月9日
@author: Alvin_zhu
'''
# from dubbbingshow_99550.Public.devices import appium_desired
import multiprocessing
# from dubbbingshow_99550.operate.Operate import BaseOperate
# from dubbbingshow_99550.test_case import Dubbing

from dubbbingshow_99550.test_case.Dubbing import Dubbin

devices_list = ['4ebc78fd', 'f249f9f2']

def start_devices_action(udid,port):

    # appium_desired(udid,port)
    s = Dubbin(udid,port)
    s.start()



def devices_start_sync():

    print('==devices_start==')

    desiried_process = []

    for i in range(len(devices_list)):

        port = 4723 + 2 * i

        desired = multiprocessing.Process(target= start_devices_action, args=(devices_list[i],port))

        desiried_process.append(desired)

    for desired in desiried_process:
        desired.start()

    for desired in desiried_process:
        desired.join()


if __name__=='__main__':
    # appium_start_sync()

    devices_start_sync()

