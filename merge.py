fred=open('tripp-useRedpckage-02.log','r')
tmp={}
for line in fred:
    orderId=line.split(',')[0].strip()
    price=line.split(',')[1].strip()
    tmp[orderId]=price

out=open('redfinal111102.csv','w')
fall=open('red111102.csv','r')
for line in fall:
    orderId=line.split(',')[0].strip()
    #print orderId
    try:
        price=tmp[orderId]
        print price
        finalLine=line.strip()+","+str(price)+"\n"
        out.write(finalLine)
    except Exception,e:
        pass
