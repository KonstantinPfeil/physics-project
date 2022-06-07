import pandas as pd
import json
import os


def readFromFile(path: str):
    times = []
    file = pd.read_excel(path)  # Daten  aus Datei lesen
    magnetData = pd.DataFrame(file, columns=["locationHeadingZ", "locationHeadingTimestamp_since1970"]).to_numpy()
    # gebrauchte colums entnehmen
    start = magnetData[0][1]  # start timestamp lesen
    magnetData = [(x, y - start) for x, y in magnetData]  # Datenvereinfachen
    positive = False  # startet mit Negativenmagneten
    for x, (value, time) in enumerate(magnetData):
        if x in range(5, len(magnetData)-5):
            Values = magnetData[x-5:x+5][0]  # vorherige und nachkommende Elemente in der Liste
            if positive and value > 500 and value >= max(Values) or \
                    not positive and value < -500 and value <= min(Values):
                # erkennung von Spitzen
                times.append(time)  # hinzufügen der Zeit
                positive = not positive # umkehren des Vorzeichen

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mtimes.txt"), "w") as f:
        f.write(
            json.dumps(dict(times=times), indent=4)
        )


if __name__ == "__main__":
    readFromFile(input("Filename: "))
