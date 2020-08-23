import math 
import webbrowser
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
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
    return "+".join(DMSList)

def GMapsRoute(DMSCoordinate): 
    webbrowser.get('chrome').open_new("google.com/maps/place/"+DMSCoordinate) 
#Please enter the latlong coordinate in this format --> "lat, long"
ConvertedCoordinate = toDMS(input("Please enter the latlong coordinate to be converted: (should be comma separated)\n"))
GMapsRoute(ConvertedCoordinate)

