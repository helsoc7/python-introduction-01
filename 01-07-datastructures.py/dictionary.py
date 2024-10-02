# Beispiel eines Wörterbuchs
person = {
    "name": "Alice",
    "alter": 30,
    "stadt": "Berlin"
}
print(person)  # Ausgabe: {'name': 'Alice', 'alter': 30, 'stadt': 'Berlin'}

# Wert ändern
person["alter"] = 31
print(person)  # Ausgabe: {'name': 'Alice', 'alter': 31, 'stadt': 'Berlin'}

# Neuen Schlüssel-Wert hinzufügen
person["beruf"] = "Ingenieurin"
print(person)  # Ausgabe: {'name': 'Alice', 'alter': 31, 'stadt': 'Berlin', 'beruf': 'Ingenieurin'}
