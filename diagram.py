import os
import json
import matplotlib.pyplot as plt
import numpy as np
import math

def calculate():
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mtimes.txt")) as f:
            times = json.loads(f.read())["times"]  # read times from file
    except FileNotFoundError:
        print("no mtimes.txt file \n try auslesen.py")
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
    averageSpeed = [meanAcceleration * t for t in times]
    weg2 = [(meanAcceleration / 2) * t**2 for t in times ]
    speedDifferences.insert(0, times[1] - times[0])  # create new difference with new time

      # first and second speed
    speeds.insert(0, 0.2 / firstTime)
    speeds.insert(0, 0)  # zero point

    accelerations.insert(0, meanAcceleration)  # dummy data
    accelerations.insert(0, meanAcceleration)
    accelerations.insert(0, meanAcceleration)

    return weg2, meanAcceleration, averageSpeed, times, weg, speeds, accelerations

def scatter(name: str, x, y, c: str, size: str):
    plt.scatter(x,y, color = c, s = size)
    xname, yname = name.split("-")
    plt.xlabel(xname)
    plt.ylabel(yname)


if __name__ == "__main__":
    calculation = calculate()
    if calculation is not None:
        s2, a2, v2, t, s, v, a = calculation
        scatter("t in s -s in m",t,s, None, None)
        scatter(" t in s - s in m", t, s2, "red", 5)
        plt.show()
        scatter("t-v", t, v, None, None)
        scatter("t in s - v2 in m/s", t, v2, "red", 5)
        plt.show()
        scatter("t in s -a in m/s^2" , t, a, None, None)
        scatter("t in s - a2 in m/s^2", t, [a2 for i in t], "red", 5)
        plt.show()
