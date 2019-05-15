#!/usr/bin/python
# DeltaPV - Auslesen der Zigbee-Sensoren via JSON  
# Voraussetzung ist ein Raspberry mit ZigBee-Adapter mit der IP-Adresse 192.168.0.13
# Jonny Hauer
# Version 2 v. 11.05.2019



import MySQLdb
import time
import datetime
import urllib2
import json
import datetime
from datetime import datetime
from pytz import timezone
import pytz
from time import localtime, strftime

# Datum umwandeln in ein Datetime-Format und anpassen an die lokale Zeitzone

def Dateconvert(Dat1):
   utc_time = datetime(int(Dat1[0:4]), int(Dat1[5:7]), int(Dat1[8:10]), int(Dat1[11:13]), int(Dat1[14:16]), int(Dat1[17:19]), tzinfo=pytz.utc)
   local_time = utc_time.astimezone(timezone('Europe/Berlin'))
   return local_time


# Datenbank Connect - Initialabfrage
dbconnPV = MySQLdb.connect(db='DB_Solar', host='127.0.0.1', port=3306, user='Solar', passwd='PASSWORD')
cursor = dbconnPV.cursor()

sql = "SELECT * FROM Parameter where Init = 'APIKey'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    APIKey = row[1]

sql = "SELECT * FROM Parameter where Init = 'IP_Sensor'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    IP_Sensor = row[1]

sql = "SELECT * FROM Parameter where Init = 'S1_Temp'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S1_Temp = row[1]

sql = "SELECT * FROM Parameter where Init = 'S1_Feucht'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S1_Feucht = row[1]

sql = "SELECT * FROM Parameter where Init = 'S1_Druck'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S1_Druck = row[1]

sql = "SELECT * FROM Parameter where Init = 'S2_Temp'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S2_Temp = row[1]

sql = "SELECT * FROM Parameter where Init = 'S2_Feucht'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S2_Feucht = row[1]

sql = "SELECT * FROM Parameter where Init = 'S2_Druck'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S2_Druck = row[1]

sql = "SELECT * FROM Parameter where Init = 'S3_Temp'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S3_Temp = row[1]

sql = "SELECT * FROM Parameter where Init = 'S3_Feucht'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S3_Feucht = row[1]

sql = "SELECT * FROM Parameter where Init = 'S3_Druck'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S3_Druck = row[1]

sql = "SELECT * FROM Parameter where Init = 'S4_Temp'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S4_Temp = row[1]

sql = "SELECT * FROM Parameter where Init = 'S4_Feucht'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S4_Feucht = row[1]

sql = "SELECT * FROM Parameter where Init = 'S4_Druck'"
cursor.execute(sql)
Ergebnis = cursor.fetchall()
for row in Ergebnis:
    S4_Druck = row[1]


req = urllib2.Request("http://"+IP_Sensor+"/api/"+APIKey+"/sensors")
opener = urllib2.build_opener()

cursor.close()
dbconnPV.close()

if __name__ == '__main__':

    while True:
        dbconnPV = MySQLdb.connect(db='DB_Solar', host='127.0.0.1', port=3306, user='Solar', passwd='PASSWORD')
        cursor = dbconnPV.cursor()

        json1 = [[[]]]
        f = opener.open(req)
        json1 = json.loads(f.read())

        Datum2 = datetime.now()
        Datum = Datum2.strftime('%Y-%m-%d %H:%M:%S')

        # Sensor 1 - S1    Datum2 = datetime.datetime.now()
        if S1_Feucht <> '0':
           Name = json1[S1_Temp]['name']
           Erreichbar = json1[S1_Temp]['config']['reachable']
           Status = json1[S1_Temp]['config']['on']
           Batterie = json1[S1_Temp]['config']['battery']
           #Batterie = 0
           Temperatur = json1[S1_Temp]['state']['temperature'] / 100
           Letztupdate = Dateconvert(json1[S1_Temp]['state']['lastupdated'])
           Feuchtigkeit = json1[S1_Feucht]['state']['humidity'] /100
           Luftdruck = json1[S1_Druck]['state']['pressure']
    
           cursor = dbconnPV.cursor()
           Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
                                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
           Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
           cursor.execute(Feldnamen, Feldinhalt)
           dbconnPV.commit()
    
        # Sensor 2 - S2
        if S2_Feucht <> '0':
           Name = json1[S2_Temp]['name']
           Erreichbar = json1[S2_Temp]['config']['reachable']
           Status = json1[S2_Temp]['config']['on']
           Batterie = json1[S2_Temp]['config']['battery']
           #Batterie = 0
           Temperatur = json1[S2_Temp]['state']['temperature'] / 100
           Letztupdate = Dateconvert(json1[S2_Temp]['state']['lastupdated'])
           Feuchtigkeit = json1[S2_Feucht]['state']['humidity'] /100
           Luftdruck = json1[S2_Druck]['state']['pressure']
    
           cursor = dbconnPV.cursor()
           Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
                                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
           Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
           cursor.execute(Feldnamen, Feldinhalt)
           dbconnPV.commit()
        
        # Sensor 3 - S3
        if S3_Feucht <> '0':
           Name = json1[S3_Temp]['name']
           Erreichbar = json1[S3_Temp]['config']['reachable']
           Status = json1[S3_Temp]['config']['on']
           Batterie = json1[S3_Temp]['config']['battery']
           #Batterie = 0
           Temperatur = json1[S3_Temp]['state']['temperature'] / 100
           Letztupdate = Dateconvert(json1[S3_Temp]['state']['lastupdated'])
           Feuchtigkeit = json1[S3_Feucht]['state']['humidity'] /100
           Luftdruck = json1[S3_Druck]['state']['pressure']
    
           cursor = dbconnPV.cursor()
           Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
                                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
           Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
           cursor.execute(Feldnamen, Feldinhalt)
           dbconnPV.commit()
    
        
        # Sensor 4 - S4
        if S4_Feucht <> '0':
           Name = json1[S4_Temp]['name']
           Erreichbar = json1[S4_Temp]['config']['reachable']
           Status = json1[S4_Temp]['config']['on']
           Batterie = json1[S4_Temp]['config']['battery']
           #Batterie = 0
           Temperatur = json1[S4_Temp]['state']['temperature'] / 100
           Letztupdate = Dateconvert(json1[S4_Temp]['state']['lastupdated'])
           Feuchtigkeit = json1[S4_Feucht]['state']['humidity'] /100
           Luftdruck = json1[S4_Druck]['state']['pressure']

           cursor = dbconnPV.cursor()
           Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
                                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
           Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
           cursor.execute(Feldnamen, Feldinhalt)
           dbconnPV.commit()
    
        cursor.close()
        dbconnPV.close()
        time.sleep(900)
