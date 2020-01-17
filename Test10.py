import os
import multiprocessing

def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'appium -a %s -p %s' % (host, port)
    os.system(cmd)


appium_process = []  # 进程组

for i in range(2):
    host = '127.0.0.1'
    port = 4723 + 2*i
    appium = multiprocessing.Process(target=appium_start, args=(host, port))
    appium_process.append(appium)


if __name__ == '__main__':
    for appium in appium_process:
        appium.start()

    for appium in appium_process:
        appium.join()