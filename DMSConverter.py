import math 
def toDMS(coordinate): 
    absoluteVal = abs(coordinate)
    degreesVal = math.floor(absoluteVal)
    minutesNTruncated = (absoluteVal - degreesVal) * 60 
    minutesVal = math.floor(minutesNTruncated)
    secondsVal = round((minutesNTruncated - minutesVal) * 60)
    return str(degreesVal)+"°"+str(minutesVal)+"'"+str(secondsVal)

print(toDMS(24.210959))