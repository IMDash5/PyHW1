from queue import Empty


Num = 39.23
def FindSum(arg):
    sum = 0
    arg = round(arg, 2)
    arg = arg * 100
    while arg != 0:
        sum = sum + arg % 10
        arg = arg // 10        
    return int(sum)
print(FindSum(Num))
