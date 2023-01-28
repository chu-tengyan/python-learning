#写一个简单的程序，通过输入两个变量的值到a和b，要求使用三目运算返回a,b两个数中较大的数，如果相等，则返回任意一个值
a=int(input("请输入数字a："))
b=int(input("请输入数字b:"))
print(a if a > b else b)


'''写一个程序，（模拟通过返回值打印不同的log），输入一个参数（success / fail），判断参数并打印相应的log，
success的时候打印“[INFO] Task complete!”, fail的时候打印“[ERROR] Task failed with error…”'''
c=input("请输入参数：")
print(c)
print("[INFO] Task complete!" if c=="success" else "[ERROR] Task failed with error…")