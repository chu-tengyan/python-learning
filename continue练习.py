#continue是跳出本次循环
i=1
sum=0
while i <=100 :
    i=i+1
    if i%2!=0 :
        continue
    sum=sum+i
print(sum)