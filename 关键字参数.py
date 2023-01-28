#定义一个函数，接受长宽高（顺序是长宽高）3个参数，返回立方体的体积，使用基于位置的调用方法，输入三个参数分别是长、宽、高，打印长宽高和体积
def rectangle(length,width,height):
    volume=length*width*height
    return volume
cfx=rectangle(10,5,6)
print(cfx)

#定义一个函数，接受长宽高（顺序是长宽高）3个参数，返回立方体的体积，使用基于关键字的调用方法，输入三个参数分别是高、长、宽，打印长宽高和体积
def rectangle1(length1,width1,height1):
    volume1=length1*width1*height1
    return volume1
cfx1=rectangle1(width1=3,height1=5,length1=6)
print(cfx1)