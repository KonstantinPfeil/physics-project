import os
import json
import matplotlib.pyplot as plt
import numpy as np


def calculate(times: [float] = []):
    if not times:
        try:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mtimes.txt")) as f:
                times = json.loads(f.read())["times"]  # read times from file
        except FileNotFoundError:
            print("no mtimes.txt file \ntry auslesen.py")
            return None
        if not times:
            return None
    times = np.asarray(times)
    weg = np.linspace(0, 2, len(times) + 1)

    timeDifferences = np.diff(times)

    speeds = 0.2 / timeDifferences
    speedDifferences = np.diff(speeds)
    averageDeltaTime = timeDifferences[:-1]/2+timeDifferences[1:]/2

    accelerations = speedDifferences / averageDeltaTime
    averageAcceleration = np.average(accelerations)

    firstTime = np.sqrt(0.4 / accelerations[0])
    times = times - times[0] + firstTime
    times = np.insert(times, 0, 0)

    averageSpeed = averageAcceleration * times
    predictedDistance = (averageAcceleration / 2) * times**2
    speedDifferences = np.insert(speedDifferences, 0, times[1] - times[0])  # create new difference with new time

    # first and second speed
    speeds = np.insert(speeds, 0, 0.2 / firstTime)
    speeds = np.insert(speeds, 0, 0)  # zero point

    for i in range(3):
        accelerations = np.insert(accelerations, 0, averageAcceleration)  # dummy data

    averageAcceleration = [averageAcceleration for t in times]

    return times, weg, speeds, accelerations, predictedDistance, averageSpeed, averageAcceleration


def scatter(name: str, x, y, c: str = None, size: str = None):
    plt.scatter(x, y, color=c, s=size)
    xname, yname = name.split("-")
    plt.xlabel(xname)
    plt.ylabel(yname)


if __name__ == "__main__":
    calculation = calculate()
    if calculation is not None:
        t, s, v, a, ps, pv, aa = calculation
        scatter("t in s-s in m", t, s)
        scatter(" t in s-s in m", t, ps, "red", 5)
        plt.show()
        scatter("t-v", t, v)
        scatter(r"t in s - v in $\frac{m}{s}$", t, pv, "red", 5)
        plt.show()
        scatter("t in s -a in m/s^2", t, a)
        scatter(r"t in s - a in $\frac{m}{s^{2}}$", t, aa, "red", 5)
        plt.show()
