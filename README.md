## Aufgabe 1
Schreibe ein Programm, das Variablen für den Namen, das Alter, die Körpergröße und den Status als Student definiert und diese auf der Konsole ausgibt.
```
# Definieren der Variablen
name = "Helen Haveloh"  # String
age = 26                 # Ganzzahl
height = 1.80            # Fließkommazahl
is_student = True         # Boolean (True oder False)

# Ausgabe der Variablen
print("Name:", name)
print("Alter:", age)
print("Körpergröße:", height, "Meter")
print("Ist Student:", is_student)
```
### Erklärung
Der Name wird als String definiert, da es eine Zeichenkette ist.
Das Alter wird als int (Ganzzahl) definiert.
Die Körpergröße ist eine float (Fließkommazahl).
Der Status als Student wird als Boolean definiert (True oder False).
print() gibt die Variablen mit beschreibenden Texten auf der Konsole aus.
## Aufgabe 2
Schreibe ein Programm, das zwei Ganzzahlen definiert und verschiedene mathematische Operationen durchführt.
```
# Definieren der Variablen
a = 10
b = 3

# Berechnungen und Ausgabe
print("Summe:", a + b)
print("Differenz:", a - b)
print("Produkt:", a * b)
print("Ganzzahliger Quotient:", a // b)
print("Rest der Division:", a % b)
print("a hoch b:", a ** b)
```
### Erklärung
+ berechnet die Summe.
- berechnet die Differenz.
* berechnet das Produkt.
// berechnet den ganzzahligen Quotienten (Division ohne Nachkommastellen).
% gibt den Rest der Division zurück.
** hebt a auf die Potenz b.
## Aufgabe 3
Schreibe ein Programm, das eine Fließkommazahl und einen String kombiniert und den Datentyp der Fließkommazahl umwandelt.
```
# Definieren der Variablen
c = 4.5
d = "Python"

# c und d kombinieren
combined = str(c) + " " + d
print("Kombiniert:", combined)

# Umwandlung von c in eine Ganzzahl
c_as_int = int(c)
print("c als Ganzzahl:", c_as_int)
```
### Erklärung
str(c) wandelt die Fließkommazahl c in einen String um, damit sie mit d kombiniert werden kann.
int(c) wandelt die Fließkommazahl c in eine Ganzzahl um, indem die Nachkommastellen abgeschnitten werden (keine Rundung).
