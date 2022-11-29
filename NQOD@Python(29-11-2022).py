a=int(input()) #Taking input - the size - in the runtime
lst=[] #Declaring a list to store the 'a' number of runtime inputs
count=0 #Initialising count to zero after declaring it
for i in range(0,a): #taking 'a' number of inputs in the runtime
    b=input() #Taking input in the runtime
    lst.append(b) #Storing the input in the list [*append=at the next]

for i in range(0,a): #Checking duplicate or repeated values
    for j in range(i+1,a): 
        if lst[i]==lst[j]:
            count+=1

for i in range(0,a-1): #Checking if last letter a word is same to the first letter of the next word
    x=lst[i]
    y=lst[i+1]
    ln=len(x)
    c=x[ln-1]
    d=y[0]
    if c!=d:
        count+=1

if count>0:
    print('No')
else:
    print('Yes')
