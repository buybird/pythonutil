import sys

filename=filename=sys.argv[1]
f=open('./'+filename,'r')
for line in f:
    cmd= '"http://172.23.174.127:7001/agent.ateye?type=INVOKER&action=invoke&beanName=notifySyncTripPProcesser&signature=sync2Tripp%28java.lang.Long%29&param1='+line
    print "curl "+cmd




