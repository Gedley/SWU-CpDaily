import urllib.request
res=urllib.request.urlopen(url='https://raw.githubusercontent.com/F-19-F/SWU-CpDaily/master/index.py')#注意国内访问github的raw需要特殊手段。
code=res.read().decode('utf-8')
#######-----单用户配置----##############
#CLOUDUSERNAME学号
CLOUDUSERNAME='你的学号'
#CLOUDPASSWORD密码(西大为身份证后6位)
CLOUDPASSWORD='你身份证后6位'
#签到延迟，默认准点
CLOUDDELAY=0
#######################################
#CLOUDPUSHTOKEN微信推送打卡日志的token
CLOUDPUSHTOKEN=''
#######################################
#百度OCR的密钥，一般可以不填
CLOUDAPP_ID=''
CLOUDAPI_KEY=''
CLOUDSECRET_KEY=''
#######################################
exec(code)