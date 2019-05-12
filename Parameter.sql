-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 11. Mai 2019 um 17:47
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
-- Tabellenstruktur für Tabelle `Parameter`
--

CREATE TABLE IF NOT EXISTS `Parameter` (
  `Init` char(15) NOT NULL,
  `Wert` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `Parameter`
--

INSERT INTO `Parameter` (`Init`, `Wert`) VALUES
('APIKey', 'B9A94AA41E'),
('Dehnen', '1'),
('IP_Sensor', '192.168.0.9'),
('Letzter_S', '546705'),
('Letzter_S_Tag', '546704'),
('Letzter_W', '320334'),
('S1_Druck', '15'),
('S1_Feucht', '14'),
('S1_Temp', '13'),
('S2_Druck', '9'),
('S2_Feucht', '8'),
('S2_Temp', '4'),
('S3_Druck', '18'),
('S3_Feucht', '17'),
('S3_Temp', '16'),
('S4_Druck', '0'),
('S4_Feucht', '0'),
('S4_Temp', '0'),
('Schieben', '1'),
('STARTSTOP', '1'),
('VorZurueck', '1');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `Parameter`
--
ALTER TABLE `Parameter`
 ADD PRIMARY KEY (`Init`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
