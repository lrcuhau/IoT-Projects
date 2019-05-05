<html>
    <head>
        <title>Sensoren Auswertung Jonny Hauer - Gesamtuebersicht</title>
    </head>
	<style type="text/css">
	  #Text03 { font:bold .9em Times; }
	  #Text02 { font:bold 70% Verdana;}
	  #Text01 { font:small-caps 70% Verdana; }
	  #Text04 { font:2em/180% Courier; }
    </style>
<body>
Temperatursensoren Jonny <br />

<table border="2" rules="groups" style="table-layout:fixed">
<thead>
  <tr>
  <td>
    <table border="1" rules="groups" style="table-layout:fixed">
      <thead>
        <tr>
          <th allign="center" valign="top"><p id="Text02">LfdNr</p></th>
          <th allign="center" valign="top"><p id="Text02">D_a_t_u_m</p></th>
          <th allign="center" valign="top"><p id="Text02">Name</p></th>
          <th allign="center" valign="top"><p id="Text02">Temp</p></th>
          <th allign="center" valign="top"><p id="Text02">Feucht</p></th>
          <th allign="center" valign="top"><p id="Text02">Luftdr</p></th>
          <th allign="center" valign="top"><p id="Text02">Batt</p></th>
          <th allign="center" valign="top"><p id="Text02">OK</p></th>         
          <th allign="center" valign="top"><p id="Text02">Status</p></th>
          <th allign="center" valign="top"><p id="Text02">U_p_d_a_t_e</p></th>
        </tr>
      </thead>

        <?php
        if (!$Verbindung = mysql_connect('localhost', 'root', 'PASSWORD')) {
            echo 'Keine Verbindung zu mysql';
            exit;
        }
        if (!mysql_select_db('DB_Solar', $Verbindung)) {
            echo 'Konnte Schema nicht selektieren';
            exit;
        }
        $SQL    = "SELECT LfdNr, Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, LetztUpdate FROM Sensor1 WHERE Name = 'Pool' ORDER BY LfdNr DESC";
        $Ergebnis = mysql_query($SQL, $Verbindung);
        if (!$Ergebnis) {
            echo "DB Fehler, konnte die Datenbank nicht abfragen\n";
            echo 'MySQL Error: ' . mysql_error();
            exit;
        }
        ?>
        
      <tbody>
       <?php
      
        while ($row = mysql_fetch_object($Ergebnis)) 
        {
        ?>
            <tr>
              <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->LfdNr; ?></p></td>
              <td style="width:140px" align="left" valign="middle"><p id="Text01"><?php echo $row->Datum; ?></p></td>
              <td style="width:70px" align="center" valign="middle"><p id="Text01"><?php echo $row->Name; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Temperatur; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Feuchtigkeit; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Luftdruck; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Batterie; ?></p></td>
              <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->Erreichbar; ?></p></td>
              <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->Status; ?></p></td>
              <td style="width:140px" align="left" valign="middle"><p id="Text01"><?php echo $row->LetztUpdate; ?></p></td>
            </tr>
        <?php
        }
        ?>
      </tbody>
    </table>
  </td>
  <td>
    <table border="1" rules="groups" style="table-layout:fixed">
      <thead>
        <tr>
          <th allign="center" valign="top"><p id="Text02">LfdNr</p></th>
          <th allign="center" valign="top"><p id="Text02">D_a_t_u_m</p></th>
          <th allign="center" valign="top"><p id="Text02">Name</p></th>
          <th allign="center" valign="top"><p id="Text02">Temp</p></th>
          <th allign="center" valign="top"><p id="Text02">Feucht</p></th>
          <th allign="center" valign="top"><p id="Text02">Luftdr</p></th>
          <th allign="center" valign="top"><p id="Text02">Batt</p></th>
          <th allign="center" valign="top"><p id="Text02">OK</p></th>         
          <th allign="center" valign="top"><p id="Text02">Status</p></th>
          <th allign="center" valign="top"><p id="Text02">U_p_d_a_t_e</p></th>
        </tr>
      </thead>

        <?php
        if (!$Verbindung = mysql_connect('localhost', 'root', 'PASSWORD')) {
            echo 'Keine Verbindung zu mysql';
            exit;
        }
        if (!mysql_select_db('DB_Solar', $Verbindung)) {
            echo 'Konnte Schema nicht selektieren';
            exit;
        }
        $SQL    = "SELECT LfdNr, Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, LetztUpdate FROM Sensor1 WHERE Name = 'Schacht' ORDER BY LfdNr DESC";
        $Ergebnis = mysql_query($SQL, $Verbindung);
        if (!$Ergebnis) {
            echo "DB Fehler, konnte die Datenbank nicht abfragen\n";
            echo 'MySQL Error: ' . mysql_error();
            exit;
        }
        ?>
        
      <tbody>
       <?php
      
        while ($row = mysql_fetch_object($Ergebnis)) 
        {
        ?>
            <tr>
              <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->LfdNr; ?></p></td>
              <td style="width:140px" align="left" valign="middle"><p id="Text01"><?php echo $row->Datum; ?></p></td>
              <td style="width:70px" align="center" valign="middle"><p id="Text01"><?php echo $row->Name; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Temperatur; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Feuchtigkeit; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Luftdruck; ?></p></td>
              <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Batterie; ?></p></td>
              <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->Erreichbar; ?></p></td>
              <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->Status; ?></p></td>
              <td style="width:140px" align="left" valign="middle"><p id="Text01"><?php echo $row->LetztUpdate; ?></p></td>
            </tr>
        <?php
        }
        ?>
      </tbody>
    </table>
  </td>
  <td>
    <table border="1" rules="groups" style="table-layout:fixed">
      <thead>
        <tr>
          <th allign="center" valign="top"><p id="Text02">LfdNr</p></th>
          <th allign="center" valign="top"><p id="Text02">D_a_t_u_m</p></th>
          <th allign="center" valign="top"><p id="Text02">Name</p></th>
          <th allign="center" valign="top"><p id="Text02">Temp</p></th>
          <th allign="center" valign="top"><p id="Text02">Feucht</p></th>
          <th allign="center" valign="top"><p id="Text02">Luftdr</p></th>
          <th allign="center" valign="top"><p id="Text02">Batt</p></th>
          <th allign="center" valign="top"><p id="Text02">OK</p></th>         
          <th allign="center" valign="top"><p id="Text02">Status</p></th>
          <th allign="center" valign="top"><p id="Text02">U_p_d_a_t_e</p></th>
        </tr>
      </thead>

    <?php
    if (!$Verbindung = mysql_connect('localhost', 'root', 'PASSWORD')) {
        echo 'Keine Verbindung zu mysql';
        exit;
    }
    if (!mysql_select_db('DB_Solar', $Verbindung)) {
        echo 'Konnte Schema nicht selektieren';
        exit;
    }
    $SQL    = "SELECT LfdNr, Datum, Name, Temperatur, Feuchtigkeit, Luftdruck, Batterie, Erreichbar, Status, LetztUpdate FROM Sensor1 WHERE Name = 'Outdoor' ORDER BY LfdNr DESC";
    $Ergebnis = mysql_query($SQL, $Verbindung);
    if (!$Ergebnis) {
        echo "DB Fehler, konnte die Datenbank nicht abfragen\n";
        echo 'MySQL Error: ' . mysql_error();
        exit;
    }
    ?>
      <tbody>
    <?php
    while ($row = mysql_fetch_object($Ergebnis)) 
    {
    ?>
        <tr>
          <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->LfdNr; ?></p></td>
          <td style="width:140px" align="left" valign="middle"><p id="Text01"><?php echo $row->Datum; ?></p></td>
          <td style="width:70px" align="center" valign="middle"><p id="Text01"><?php echo $row->Name; ?></p></td>
          <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Temperatur; ?></p></td>
          <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Feuchtigkeit; ?></p></td>
          <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Luftdruck; ?></p></td>
          <td style="width:50px" align="center" valign="middle"><p id="Text01"><?php echo $row->Batterie; ?></p></td>
          <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->Erreichbar; ?></p></td>
          <td style="width:30px" align="center" valign="middle"><p id="Text01"><?php echo $row->Status; ?></p></td>
          <td style="width:140px" align="left" valign="middle"><p id="Text01"><?php echo $row->LetztUpdate; ?></p></td>
        </tr>
    <?php
    }
    ?>
        </tbody>
       </table>
 </td>
</tr>
<?php
mysql_close($Ergebnis);

?>

(c) Jonny

</body>
</html>
