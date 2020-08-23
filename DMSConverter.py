import math 
def toDMS(coordinate): 
    coordinate = coordinate.replace(" ","")
    coordinateList = coordinate.split(",")
    DMSList = []
    if float(coordinateList[0]) > 0: 
        NSParam = 'N'
    else: 
        NSParam = 'S'
    if float(coordinateList[1]) > 0: 
        EWParam = 'E'
    else: 
        EWParam = 'W' 
    absoluteVal = abs(float(coordinateList[0]))
    degreesVal = math.floor(absoluteVal)
    minutesNTruncated = (absoluteVal - degreesVal) * 60
    minutesVal = math.floor(minutesNTruncated)
    secondsVal = round((minutesNTruncated - minutesVal) * 60)
    DMSList.append(str(degreesVal)+"°"+str(minutesVal)+"'"+str(secondsVal)+'"'+NSParam)
    absoluteVal = abs(float(coordinateList[1]))
    degreesVal = math.floor(absoluteVal)
    minutesNTruncated = (absoluteVal - degreesVal) * 60
    minutesVal = math.floor(minutesNTruncated)
    secondsVal = round((minutesNTruncated - minutesVal) * 60)
    DMSList.append(str(degreesVal)+"°"+str(minutesVal)+"'"+str(secondsVal)+'"'+EWParam)
    return " ".join(DMSList)

#print(toDMS(24.210959))
#Please enter the latlong coordinate in this format --> "lat, long"
ConvertedCoordinate = toDMS(input("Please enter the latlong coordinate to be converted: (should be comma separated)\n"))
