BUILD_ID=dontKillMe
ps -ef |grep appium |grep -v grep |awk '{print $2}' |xargs kill -9 
echo "" > appium.log
nohup appium --address 127.0.0.1 --port 4725 --session-override --platform-name Android --platform-version 25 --automation-name Appium --log-timestamp --local-timezone --no-reset  >> appium.log 2>&1&