#coding = utf-8
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# os.system('shell.sh')
os.system('start /b appium --address 127.0.0.1 --port 4725 --session-override --platform-name Android --platform-version 25 --automation-name Appium --log-timestamp --local-timezone --no-reset  >> appium.log 2>&1&')