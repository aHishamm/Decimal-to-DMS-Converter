import math 
import webbrowser
import os 
import pandas as pd 
import firebase_admin 
from firebase_admin import credentials 
from firebase_admin import db 
#firebase configuration 
databaseURLFile = open('C:\\Users\\Abdulrahman\\Desktop\\Firebase database address\\firebaseDatabaseAddress.txt','r')
databaseURL = databaseURLFile.read()
cred = credentials.Certificate('C:\\Users\\Abdulrahman\\Desktop\\python requests\\testpython-b2fae-firebase-adminsdk-mnt86-8d01d7b825.json')
firebase_admin.initialize_app(cred, {'databaseURL':databaseURL})

if os.name == 'nt': 
    webbrowser.register('chrome',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
else: 
    webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("/usr/bin/google-chrome"))
def toDMS(coordinate):
    try:
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
    except:
        print("Please enter the coordinates in the proper format: \"Latitude, Longitude\"")
        return "Please enter a proper format: \"Latitude, Longitude\""

def GMapsRoute(DMSCoordinate): 
    DMSCoordinate = DMSCoordinate.split() 
    newDMS = "+".join(DMSCoordinate)
    webbrowser.get('chrome').open_new("google.com/maps/place/"+newDMS) 

def exportCSV(originalValList,convertedValList): 
    coordinateDict = {'Decimal Coordinate History':originalValList, 'DMS Coordinate History': convertedValList}
    coordinateDataFrame = pd.DataFrame(coordinateDict)
    #check if csv file is already in path
    if(os.path.exists('export_DMS_coordinate_history.csv')):
        with open('export_DMS_coordinate_history.csv','a') as f: 
            coordinateDataFrame.to_csv(f,header=f.tell()==0)
    coordinateDataFrame.to_csv('export_DMS_coordinate_history.csv',index=False)
    print(coordinateDataFrame)


def passToFirebase(DMSCoordinate, DecimalCoordinate): 
    ref = db.reference('/')
    dictionary = {'Decimal Coordinate': DecimalCoordinate, 'DMS Coordinate': DMSCoordinate}
    ref.push(dictionary)

#deprecated 
# def toJSON(DMSCoordinate,DecimalCoordinate): 
#     jsonData = {"Decimal Coordinate":DecimalCoordinate,"DMS Coordinate":DMSCoordinate}
#     with open('JSONDump.json','w') as outfile:
#         json.dump(jsonData,outfile)
