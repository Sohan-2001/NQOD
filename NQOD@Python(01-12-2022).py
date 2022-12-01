a,b,c=map(int,input().split())
count=0
while a>0:
    d,e=map(int,input().split())
    if d<b and e>c:
        count+=1
    
    a-=1

if count>0:
    print('Yes')
else:
    print('No')
