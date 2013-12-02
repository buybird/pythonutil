f1=open('./xiangpeng1.csv','r')

for line in f1:
    content=line.split(',')
    pnr=content[3].strip()
    passengername=content[5].strip()
    orderid=content[4].strip()
    tktno=content[6].strip()
    print tktno+"==="+passengername+"==="+pnr+"==="+orderid
