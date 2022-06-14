import pandas as pd
import json
import os


def readFromFile(path: str, toFile: bool = True):
    times = []
    if path.__contains__(".xlsx"): # check if it is a exel file
        file = pd.read_excel(path)  # read from exel
    else:
        file = pd.read_csv(path, header=0, sep=";") # read from csv
    magnetData = pd.DataFrame(file, columns=["locationHeadingZ", "locationHeadingTimestamp_since1970"]).to_numpy()
    # gebrauchte colums entnehmen
    start = magnetData[0][1]  # start timestamp lesen
    magnetData = [(m, t - start) for m, t in magnetData]  # Datenvereinfachen
    positive = False  # startet mit Negativenmagneten
    for x, (value, time) in enumerate(magnetData):
        if x in range(5, len(magnetData)-5):
            Values = [t for m, t in magnetData[x-5:x+5]]  # vorherige und nachkommende Elemente in der Liste
            if positive and value > 500 and value >= max(Values) or \
                    not positive and value < -500 and value <= min(Values):
                # erkennung von Spitzen
                times.append(time)  # hinzufügen der Zeit
                positive = not positive # umkehren des Vorzeichen

    if toFile:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mtimes.txt"), "w") as f:
            f.write(
                json.dumps(dict(times=times), indent=4)
            )
    return times


if __name__ == "__main__":
    readFromFile(input("Filename: "))
