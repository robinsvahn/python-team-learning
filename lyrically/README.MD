#===============================================================#
Välkommen till lyrically, världens roligaste lyrics spel!
#===============================================================#
Vi som skapat progammet är:
Robin Svahn
Hanna Bergqvist
Mikaela Keegan
#===============================================================#
För att få programmet att köra:

För att spela spelet måste man skapa en lokal SQL Express Databank med namnet "python_test", med windows authentication.
Det finns en .bak fil i mappen "Other" -> "DB_Backup" som heter "db_backup_2022.03.22.bak" för att förenkla skapandet.
Det finns även ett ERM diagramm i mappen "Other" -> "DB_ERM" som heter "Database_ERM.png" för att få en överblick av tabellerna.

Programmet använder även bibloteken SqlAlchemy och PyODBC som måste installeras på datorn.

- https://www.sqlalchemy.org/
- https://pypi.org/project/pyodbc/

När man gjort detta kan man öppna filen "main.py" i root mappen och starta skriptet.
#===============================================================#
Vad gör programmet:
Vi har skapat en liten Databank med kända låtar och en av låtarnas textrader.
Till dessa har vi skapat tre alternativa versioner av textraden där vi ändrat minst ett morfem.

När man startar igång spelet kan man antingen ladda resultatet av en gammal match, eller starta en ny.
Matcherna spelas mellan två spelare/teams, där man ska gissa rätt version av textraden på 5 olika låtar.
Efter 5 omgångar, är det spelaren med mest rätt som vinner.

Efter en spelad match sparas matchen i databanken och man kommer tillbaks till huvudmenyn.
#===============================================================#
