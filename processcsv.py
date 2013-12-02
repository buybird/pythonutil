import sys
import urllib

def getLineNum(f):
    rs=0
    for i in f:
        rs+=1
    f.seek(0)
    return rs


filename=filename=sys.argv[1]
f=open('./'+filename,'r')
orderid=0
data=[]
result={}
currline=0
totalline=getLineNum(f)
for line in f:
    currline+=1
    content=line.split(',')
    name=urllib.quote(content[1].strip())
    orderidtmp=content[0].strip()
    pnr=content[2].strip()
    tktno=content[3].strip()
    #print "debug:"+str(orderid)+", currorderid:"+orderidtmp+" tkt:"+tktno
    if orderid==0:
        orderid=orderidtmp
        data.append(name+";"+name+";"+pnr+";"+tktno)
        if currline==totalline:
           result[orderid]=data
    else:
        if orderidtmp == orderid:
            data.append(name+";"+name+";"+pnr+";"+tktno)
            if currline==totalline:
                result[orderid]=data

        else:
            result[orderid]=data
            #print "--debug put :"+str(orderid)+":"+",".join(data)
            orderid=orderidtmp
            data=[]
            data.append(name+";"+name+";"+pnr+";"+tktno)
            if currline==totalline:
                result[orderid]=data
                #print "--debug: put after diff "+str(orderid)+":"+",".join(data)
    #cmd= '"http://172.23.229.91:7001/agent.ateye?type=INVOKER&action=invoke&beanName=atoApiAgentOrderService&signature=successOrder(java.lang.String,java.lang.String,java.lang.String,java.lang.Long,java.lang.Long)&param1='+name+'&param2='+pnr+'&param3='+tktno+'&param4='+orderid+'&param5=2108"'
    #print "echo "+cmd
    #print "curl "+cmd


for k,v in result.items():
    #print k+":"+(",".join(v))
    orderid=k
    tktinfo=",".join(v)
    cmd= '"http://172.23.229.91:7001/agent.ateye?type=INVOKER&action=invoke&beanName=atoApiAgentOrderService&signature=successOrderByAteye(java.lang.String,java.lang.Long,java.lang.Long)&param1='+tktinfo+'&param2='+orderid+'&param3=2108"'
    print "echo "+cmd
    print "curl "+cmd


