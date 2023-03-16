# Projektdokumentation

## Einleitung
### Ziel des Projekts
### Überblick über die REST-Schnittstelle und FastAPI
### Installation und Einrichtung
Die Installation und Einrichtung des Projektes erfordert einige kleinere Schritte. Grundsätzlich ist eine Installation 
von Python erforderlich, in diesem Projekt wird Python in der Version 3.10 genutzt, sodass mit dieser Version die 
Funktionalität gewährleistet werden kann (https://www.python.org/downloads/).  

Für die REST-Schnittstelle ist die Installation von diversen Paketen erforderlich, unter anderem FastAPI, 
SQLAlchemy und Pydantic (siehe Installation von FastAPI und benötigten Paketen). 
## Systemanforderungen
### Installation von FastAPI und benötigten Paketen
Für die Umsetzung der REST-Schnittstelle wurde das Framework FastAPI von openai verwendet. Das Paket hierfür muss über pip
vor der Nutzung der Schnittstelle installiert werden ("pip install fastapi"). Ebenfalls wird zum Starten der Schnittstelle
das Paket uvicorn genutzt, welches ebenfalls über pip installiert werden muss ("pip install uvicorn"). Sind die Pakete installiert
so kann die Schnittstelle über "uvicorn main:app --reload" gestartet werden. Nach einigen Sekunden sollte die Anwendung gestartet
sein und kann genutzt werden.

Weiterhin werden für die Datenbank verschiedene Pakete benötigt, konkret handelt es sich hierbei um SQLAlchemy sowie Pydantic.
Diese werden ebenfalls über die zugehörigen pip Befehle installiert. Sie werden benötigt um eine Kommunikation mit der Datenbank
und der damit einhergehenden persistenten Datenspeicherung zu gewährleisten. 
### Konfiguration der Umgebung
## API-Spezifikation
### Beschreibung der verfügbaren Endpunkte
Mithilfe des Frameworks FastAPI von openai können verschiedene Endpunkte für die Schnittstelle aufgebaut werden. Über diese 
Endpunkte treffen die Http-Requests auf die Schnittstelle und können mit den entsprechenden Daten verarbeitet werden. 
Damit ist die persistente Speicherung von Entitäten und Daten, sowie Relationen recht trivial. Außerdem lassen sich so
Daten über simple Http-Get-Requests erfragen. Auch Auswertungen über beispielsweise den höchsten Preis in der Historie
oder andere lassen sich darüber zurückgeben. 

Eine Liste der verfügbaren Endpunkte:

- #### /item/new
    Lirum Larum Löffelstiel
- #### /items/{itemId}
    Lirum Larum Löffelstiel
- #### /items
    Lirum Larum Löffelstiel
### Parameter und Rückgabetypen für jeden Endpunkt
### Beispielanforderungen und -antworten für jeden Endpunkt
## Implementierungsdetails
### Architektur des Projekts
### Verwendung von Datenbanken oder anderen Backend-Services
### Behandlung von Fehlern und Ausnahmen
### Authentifizierung und Autorisierung
## Testen und Bereitstellung
### Unit-Tests für die einzelnen Endpunkte
### Integrationstests für das gesamte System
### Bereitstellung der API auf einem Server
### Überwachung und Skalierung
## Anhang
### Glossar der verwendeten Begriffe
### Beispielimplementierung des Projekts
### Links zu weiteren Ressourcen und Dokumentation
