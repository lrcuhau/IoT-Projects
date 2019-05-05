Temperatur Sensoren auslsesen

Benötigte Hardware:
   Raspberry PI
   Raspberry ZigBee Adapter
   AQARA Sensoren

1. Nach Anbringen des ZigBee Adapters am Raspberry ist die Software zu installieren:
   Details dazu: https://www.dresden-elektronik.de/funktechnik/solutions/wireless-light-control/raspbee/

2. Der API-Key ist zu ermitteln.
   Var A. Mit Hilfe der DeConz-Software
   Var B. Mit Hilfe des Programms "Postman".

3. Mit Hilfe des API-Keys lässt sich folgende Seite öffnen.
http://IP-Adresse_Raspi/api/B9A94AA41E(->API-Key)/sensors

4. Diese Url zeigt eine JSON-Datei, die im folgenden Verlauf von einem Python-Programm ausgelesen wird.

5. Das Python-Programm benötigt 2 Bibliotheken:
  import urllib2
  import json
Diese sind mit 
  sudo pip install urllib2 und 
  sudo pip install json zu installieren.

Damit werden wie im Python-Code beschrieben, die Daten aus der angegeben URL ausgelesen und als Python-Variable in eine MySQL-DB geschrieben.

6. Die Datenstruktur der Datenbank ist in der Datei 'Sensor1-2.sql' angeführt.

7. Für die Visualisierung dieser Daten in Form einer 3-spaltigen Tabelle wird der das php-Script:
     Sensoren1.php
   verwendet.
