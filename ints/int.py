

#Takes number to the power of power
def power(number = 1, power = 1):
    try:
        number = int(number)
        power = int(power)
        return number**power
    except:
        return "Not numbers"
    
#Multiplies a variable amount of numbers with eachother, will skip any non numbers
def multiply(*args):
    sum = 1
    for arg in args:
        try:
            arg = int(arg)
            sum *= arg
        except:
            continue
    return sum

