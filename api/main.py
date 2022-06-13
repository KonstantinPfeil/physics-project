from fastapi import FastAPI, File, UploadFile
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import pandas as pd
import io
import numpy as np
import json

app = FastAPI()

app.mount("/html/", StaticFiles(directory=r"..\physics-Website", html=True))


@app.post("/getDiagramData/")
async def get_data_from_csv(file: UploadFile = File(...)):
    file = pd.read_csv(io.BytesIO(await file.read()), sep=";", header=0)
    times = []
    magnetData = pd.DataFrame(file, columns=["locationHeadingZ", "locationHeadingTimestamp_since1970"]).to_numpy()
    # gebrauchte colums entnehmen
    start = magnetData[0][1]  # start timestamp lesen
    magnetData = [(m, t - start) for m, t in magnetData]  # Datenvereinfachen
    positive = False  # startet mit Negativenmagneten
    for x, (value, time) in enumerate(magnetData):
        if x in range(5, len(magnetData) - 5):
            Values = [t for m, t in magnetData[x - 5:x + 5]]  # vorherige und nachkommende Elemente in der Liste
            if positive and value > 500 and value >= max(Values) or \
                    not positive and value < -500 and value <= min(Values):
                # erkennung von Spitzen
                times.append(time)  # hinzufügen der Zeit
                positive = not positive  # umkehren des Vorzeichen

    weg = [x * 0.20 for x in range(len(times) + 1)]

    timeDifferences = [t - times[x - 1] for x, t in enumerate(times) if x > 0]

    speeds = [0.20 / t for t in timeDifferences]
    speedDifferences = [v - speeds[x - 1] for x, v in enumerate(speeds) if x > 0]

    accelerations = [v / t for v, t in zip(speedDifferences, timeDifferences[1:])]
    meanAcceleration = sum(accelerations) / len(accelerations)

    firstTime = np.sqrt(0.4 / accelerations[0])
    times.insert(0, firstTime)
    times = [t - times[0] for t in times]

    speedDifferences.insert(0, times[1] - times[0])  # create new difference with new time

    speeds.insert(0, 0.2 / firstTime)  # first and second speed
    speeds.insert(0, 0)  # zero point

    accelerations.insert(0, meanAcceleration)  # dummy data
    accelerations.insert(0, meanAcceleration)
    accelerations.insert(0, meanAcceleration)

    return dict(times=times, weg=weg, speeds=speeds, accelerations=accelerations)


@app.get("/data/")
async def get_data():
    try:
        with open(r"C:\Users\chris\projekts\physics-project\mtimes.txt") as f:
            times = json.loads(f.read())["times"]  # read times from file
    except FileNotFoundError:
        print("no mtimes.txt file \n try auslesen.py")
        return None
    if not times:
        return None

    weg = [x * 0.20 for x in range(len(times) + 1)]

    timeDifferences = [t - times[x - 1] for x, t in enumerate(times) if x > 0]

    speeds = [0.20 / t for t in timeDifferences]
    speedDifferences = [v - speeds[x - 1] for x, v in enumerate(speeds) if x > 0]

    accelerations = [v / t for v, t in zip(speedDifferences, timeDifferences[1:])]
    meanAcceleration = sum(accelerations) / len(accelerations)

    firstTime = np.sqrt(0.4 / accelerations[0])
    times.insert(0, firstTime)
    times = [t - times[0] for t in times]

    speedDifferences.insert(0, times[1] - times[0])  # create new difference with new time

    speeds.insert(0, 0.2 / firstTime)  # first and second speed
    speeds.insert(0, 0)  # zero point

    accelerations.insert(0, meanAcceleration)  # dummy data
    accelerations.insert(0, meanAcceleration)
    accelerations.insert(0, meanAcceleration)

    return dict(times=times, weg=weg, speeds=speeds, accelerations=accelerations)