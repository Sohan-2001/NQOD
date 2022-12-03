a=int(input())
b=4
i=2
def prime(n):
    for j in range(2,n):
        if n%j==0:
            return False
            break
        
    return True


while prime(a^i)=='False':
    while i>0:
        if a^i%2==0 and prime(a^i)=='True':
            break
        else:
            i+=i

print(a^i,end='')
