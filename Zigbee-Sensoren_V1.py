# DeltaPV - Auslesen der Zigbee-Sensoren via JSON  
# Voraussetzung ist ein Raspberry mit ZigBee-Adapter mit der IP-Adresse 192.168.0.13
# Jonny Hauer
# Version 1 v. 22.4.2019



import MySQLdb
# import sys, subprocess, serial
import time
import datetime
import urllib2
import json

from time import localtime, strftime
# from config import Configuration

req = urllib2.Request("http://192.168.0.9/api/B9A94AA41E/sensors")
opener = urllib2.build_opener()

if __name__ == '__main__':

    while True:
        json1 = [[[]]]
        f = opener.open(req)
        json1 = json.loads(f.read())

        dbconnPV = MySQLdb.connect(db='DB_Solar', host='127.0.0.1', port=3306, user='Solar', passwd='PASSWORD')
        cursor = dbconnPV.cursor()

        Datum2 = datetime.datetime.now()
        Datum = Datum2.strftime('%Y-%m-%d %H:%M:%S')

        # Schacht     Datum2 = datetime.datetime.now()
        Name = json1['13']['name']
        Erreichbar = json1['13']['config']['reachable']
        Status = json1['13']['config']['on']
        Batterie = json1['13']['config']['battery']
        Batterie = 0
        Temperatur = json1['13']['state']['temperature'] / 100
        Letztupdate = json1['13']['state']['lastupdated']
        Feuchtigkeit = json1['14']['state']['humidity'] /100
        Luftdruck = json1['15']['state']['pressure']
    
        cursor = dbconnPV.cursor()
        Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
                                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
        cursor.execute(Feldnamen, Feldinhalt)
        dbconnPV.commit()
    
        # Outdoor
        Name = json1['4']['name']
        Erreichbar = json1['4']['config']['reachable']
        Status = json1['4']['config']['on']
        Batterie = json1['4']['config']['battery']
        Batterie = 0
        Temperatur = json1['4']['state']['temperature'] / 100
        Letztupdate = json1['4']['state']['lastupdated']
        Feuchtigkeit = json1['8']['state']['humidity'] /100
        Luftdruck = json1['9']['state']['pressure']
    
        cursor = dbconnPV.cursor()
        Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
                                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
        cursor.execute(Feldnamen, Feldinhalt)
        dbconnPV.commit()
        
        # Pool
        Name = json1['5']['name']
        Erreichbar = json1['5']['config']['reachable']
        Status = json1['5']['config']['on']
        Batterie = json1['5']['config']['battery']
        Batterie = 0
        Temperatur = json1['5']['state']['temperature'] / 100
        Letztupdate = json1['5']['state']['lastupdated']
        Feuchtigkeit = json1['6']['state']['humidity'] /100
        Luftdruck = json1['7']['state']['pressure']
    
        cursor = dbconnPV.cursor()
        Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
                                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
        cursor.execute(Feldnamen, Feldinhalt)
        dbconnPV.commit()
    
        # Gartenhaus
        # Name = json1['5']['name']
        # Erreichbar = json1['5']['config']['reachable']
        # Status = json1['5']['config']['on']
        # Batterie = json1['5']['config']['battery']
        # Batterie = 0
        # Temperatur = json1['5']['state']['temperature'] / 100
        # Letztupdate = json1['5']['state']['lastupdated']
        # Feuchtigkeit = json1['6']['state']['humidity'] /100
        # Luftdruck = json1['7']['state']['pressure']
    
        # cursor = dbconnPV.cursor()
        # Feldnamen = ("INSERT INTO Sensor1"   "(Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)"
        #                          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        # Feldinhalt = (Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, Letztupdate)
        # cursor.execute(Feldnamen, Feldinhalt)
        # dbconnPV.commit()
    
        cursor.close()
        dbconnPV.close()
        time.sleep(900)
