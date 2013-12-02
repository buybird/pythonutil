s=set()
f1=open('./tripp1.txt','r')
for i in f1:
    s.add(i)

print len(s)

s1=set()
f2=open('./tripp2.txt','r')
for i in f2:
    s1.add(i)
print len(s1)
