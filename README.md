# 🌼 Pollenflug Bayern (ePIN) für Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![maintainer](https://img.shields.io/badge/maintainer-%40GernotAlthammer-blue.svg)](https://github.com/GernotAlthammer)

Eine Home Assistant Custom Component (Integration) zur Einbindung der aktuellen Pollenflugdaten des Bayerischen Landesamts für Gesundheit und Lebensmittelsicherheit (LGL Bayern). Die Daten stammen aus dem elektronischen Polleninformationsnetzwerk (ePIN).

## ✨ Funktionen

* 🖥️ **Einfache UI-Konfiguration (Config Flow):** Einrichtung komplett über die Home Assistant Oberfläche – kein YAML erforderlich!
* 📍 **Dynamische Standortwahl:** Die verfügbaren Messstationen (z. B. München, Altötting, Viechtach) werden live von der API geladen und können in einem Dropdown-Menü ausgewählt werden.
* 🌍 **Multi-Instanz fähig:** Du kannst die Integration mehrfach hinzufügen, um verschiedene Orte gleichzeitig zu überwachen (z. B. Wohnort und Arbeitsort).
* 📊 **Umfassende Daten:** Erstellt automatisch Sensoren für **41 verschiedene Pollenarten** (Birke, Hasel, Gräser, etc.).
* ⚡ **Ressourcenschonend:** Nutzt den Home Assistant `DataUpdateCoordinator`, um alle Daten mit nur einer einzigen API-Abfrage alle 3 Stunden gesammelt abzurufen (schont die Server des LGL).

## 📥 Installation

### Methode 1: Über HACS (Empfohlen)
1. Öffne **HACS** in deiner Home Assistant Oberfläche.
2. Gehe zu **Integrationen**.
3. Klicke auf das Drei-Punkte-Menü oben rechts und wähle **Benutzerdefinierte Repositories**.
4. Füge die URL dieses Repositories ein: `https://github.com/GernotAlthammer/pollenflug-bayern`
5. Wähle als Kategorie **Integration** und klicke auf Hinzufügen.
6. Suche in HACS nach "Pollenflug Bayern", klicke auf **Herunterladen**.
7. **Starte Home Assistant neu.**

### Methode 2: Manuell
1. Lade das Repository als ZIP-Datei herunter.
2. Entpacke die ZIP-Datei.
3. Kopiere den Ordner `custom_components/pollenflug_bayern` in das `custom_components` Verzeichnis deiner Home Assistant Installation.
4. **Starte Home Assistant neu.**

## ⚙️ Konfiguration

Nach dem Neustart von Home Assistant kann die Integration über die Benutzeroberfläche hinzugefügt werden:

1. Gehe zu **Einstellungen** ➡️ **Geräte & Dienste**.
2. Klicke unten rechts auf **Integration hinzufügen**.
3. Suche nach **Pollenflug Bayern** und klicke darauf.
4. Wähle im Dropdown-Menü deine gewünschte Messstation aus und bestätige.
5. *(Optional)* Wiederhole den Vorgang, wenn du weitere Messstationen hinzufügen möchtest.

## 🔍 Sensoren

Nach der erfolgreichen Einrichtung werden Sensoren für die ausgewählte Messstation erstellt. 
Beispiel für die Namensgebung: `sensor.pollenflug_munchen_demun_betula` (Pollenflug München Birke).
Einheit: `Pollen/m³`

Folgende Pollenarten werden derzeit (sofern von der Station gemeldet) unterstützt:
Abies, Acer, Aesculus, Alnus, Ambrosia, Artemisia, Asteraceae, Betula, Carpinus, Castanea, Chenopodium, Corylus, Cruciferae, Cyperaceae, Erica, Fagus, Fraxinus, Fungus, Galium, Humulus, Impatiens, Juglans, Larix, Picea, Pinaceae, Pinus, Plantago, Platanus, Poaceae, Populus, Quercus, Quercus ilex, Rumex, Salix, Sambucus, Secale, Taxus, Tilia, Ulmus, Urtica, Varia.

---
*Disclaimer: Diese Integration ist kein offizielles Produkt des LGL Bayern. Die Nutzung der ePIN-Daten erfolgt auf Basis der vom LGL bereitgestellten öffentlichen API.*
