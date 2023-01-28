number1=int(input("请输入一个数字："))
i=0
while i < number1 :
    i=i+1
    if number1%i==0 and i==1 or i==number1 :
        print("这个数是素数")
        break
    else:
        print("这个数不是素数")
        break