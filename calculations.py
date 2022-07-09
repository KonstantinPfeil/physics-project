import pandas as pd
import numpy as np
from typing import List, Optional


def readFromFile(path: str):
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
    return times


def calculate(distance: float, times: List[float]):
    if not times:
        print("no times")
        return None
    times = np.asarray(times)
    weg = np.linspace(0, distance * len(times), len(times) + 1)

    timeDifferences = np.diff(times)

    speeds = distance / timeDifferences
    speedDifferences = np.diff(speeds)
    averageDeltaTime = timeDifferences[:-1] / 2 + timeDifferences[1:] / 2

    accelerations = speedDifferences / averageDeltaTime
    averageAcceleration = np.average(accelerations)

    firstTime = np.sqrt(distance*2 / accelerations[0])
    times = times - times[0] + firstTime
    times = np.insert(times, 0, 0)

    # first and second speed
    speeds = np.insert(speeds, 0, distance / firstTime)
    speeds = np.insert(speeds, 0, 0)  # zero point

    for i in range(3):
        accelerations = np.insert(accelerations, 0, averageAcceleration)  # dummy data

    fun_paras_t_s = np.round_(np.polyfit(times, weg, 2), 4)
    fun_paras_t_v = np.round_(np.polyfit(times, speeds, 1), 4)
    fun_paras_t_a = np.round_(np.polyfit(times, accelerations, 0), 4)
    s_fit = np.poly1d(fun_paras_t_s)
    v_fit = np.poly1d(fun_paras_t_v)
    a_fit = np.poly1d(fun_paras_t_a)

    return times, weg, speeds, accelerations, s_fit(times), v_fit(times), a_fit(times), \
        fun_paras_t_s, fun_paras_t_v, fun_paras_t_a


def scatter(name: str, x, y, c: Optional[str] = None, size: Optional[int] = None):
    plt.scatter(x, y, color=c, s=size)
    xname, yname = name.split("-")
    plt.xlabel(xname)
    plt.ylabel(yname)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    ts = readFromFile(input("Filename"))
    calculation = calculate(0.2, ts)
    if calculation is not None:
        t, s, v, a, ps, pv, aa, paras_s, paras_v, paras_a = calculation
        scatter("t in s-s in m", t, s)
        scatter("t in s-s in m", t, ps, "red", 5)
        plt.show()
        scatter("t-v", t, v)
        scatter(r"t in s - v in $\frac{m}{s}$", t, pv, "red", 5)
        plt.show()
        scatter("t in s -a in m/s^2", t, a)
        scatter(r"t in s - a in $\frac{m}{s^{2}}$", t, aa, "red", 5)
        plt.show()
