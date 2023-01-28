'''定义个函数可接受年、月、日、时、分、秒6个参数， 返回24小时之后的年月日时分秒，时分秒为可选，如果没有输入，默认值时0时0分0秒'''

def time(year,month,day,hour=0,minute=0,second=0):
    if  day<=30 and month!=2:
        return year,month,day+1,hour,minute,second
    elif day>27 and month==2 and year%4==0 and year%100 !=0 or year%400==0:
        return year, month, day + 1, hour, minute, second
    elif day>27 and month==2:
        day=1
        return year, month+1, day, hour, minute, second
    elif day>30 and month<=11:
        day=1
        return year,month+1,day,hour,minute,second
    else:
        month=1
        day=1
        return year+1,month,day,hour,minute,second

# 输入时间不带含有默认值的参数
sj=time(2015,12,1)
# 输入时间带所有参数（会覆盖默认参数）
sj1=time(2015,12,1,23,59,59)
# 输入时间为一个月的最后一天
sj2=time(2015,1,31)
# 输入时间为一年的最后一天
sj3=time(2015,12,31)
# 输入时间为闰年的2/28   #能被4整除但不能整除100或者能被400整除
sj4=time(2020,2,28)
# 输入时间为非闰年的2/28
sj5=time(2022,2,28)
print(sj[0],sj[1],sj[2],sj[3],':',sj[4],':',sj[5])
print('{0} {1} {2} {3}:{4}:{5}'.format(sj[0],sj[1],sj[2],sj[3],sj[4],sj[5]))
print(sj1[0],sj1[1],sj1[2],sj1[3],':',sj1[4],':',sj1[5])
print(sj2[0],sj2[1],sj2[2],sj2[3],':',sj2[4],':',sj2[5])
print(sj3[0],sj3[1],sj3[2],sj3[3],':',sj3[4],':',sj3[5])
print(sj4[0],sj4[1],sj4[2],sj4[3],':',sj4[4],':',sj4[5])
print(sj5[0],sj5[1],sj5[2],sj5[3],':',sj5[4],':',sj5[5])