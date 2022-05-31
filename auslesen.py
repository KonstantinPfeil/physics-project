import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

times: [int] = []

file = pd.read_excel(input("Filename: "))  # Daten  aus Datei lesen
magnetData = pd.DataFrame(file, columns=["locationHeadingZ", "locationHeadingTimestamp_since1970"]).to_numpy()
# gebrauchte colums entnehmen
start = magnetData[0][1]  # start timestamp lesen
magnetData = [(x, y - start) for x, y in magnetData]  # Datenvereinfachen
positive = False  # startet mit Negativenmagneten
for x, (value, time) in enumerate(magnetData):
    if x + 5 < len(magnetData):
        nextValues = [magnetData[i][0] for i in range(x + 1, x + 5)]  # vorherige und nachkommende Elemente in der Liste
        lastValues = [magnetData[i][0] for i in range(x - 5, x - 1)]
        if positive and value > 500 and value > max(nextValues) and value > max(lastValues) or \
                not positive and value < -500 and value < min(nextValues) and value < min(lastValues):
            # erkennung von Spitzen
            times.append(time)  # hinzufügen der Zeit
            positive = not positive # umkehren des Vorzeichen

with open(input("path: "), "w") as f:
    f.write(
        json.dumps(dict(times=times), indent=4)
    )
