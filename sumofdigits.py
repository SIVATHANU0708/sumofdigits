a=int(raw_input())
sum=0
while(a!=0):
 digits=a%10
 sum=sum+digits
 a=a/10
print sum
