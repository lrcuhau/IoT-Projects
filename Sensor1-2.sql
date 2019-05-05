-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 05. Mai 2019 um 13:56
-- Server Version: 5.5.62-0+deb8u1
-- PHP-Version: 5.6.40-0+deb8u2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `DB_Solar`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Sensor1`
--

CREATE TABLE IF NOT EXISTS `Sensor1` (
`LfdNr` bigint(20) NOT NULL,
  `Datum` char(30) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Temperatur` decimal(5,2) NOT NULL,
  `Feuchtigkeit` decimal(5,2) NOT NULL,
  `Luftdruck` decimal(6,1) NOT NULL,
  `Batterie` varchar(3) NOT NULL,
  `Erreichbar` varchar(6) NOT NULL,
  `Status` varchar(6) NOT NULL,
  `LetztUpdate` varchar(25) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3747 DEFAULT CHARSET=latin1;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `Sensor1`
--
ALTER TABLE `Sensor1`
 ADD PRIMARY KEY (`LfdNr`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `Sensor1`
--
ALTER TABLE `Sensor1`
MODIFY `LfdNr` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3747;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
