import os
import json
import matplotlib.pyplot as plt
import numpy as np

def calculate():
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mtimes.txt")) as f:
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
    return times, weg, speeds, accelerations, meanAcceleration


if __name__ == "__main__":
    calculation = calculate()
    if calculation is not None:
        t, s, v, a, ma = calculation
        plt.plot(t, s)
        plt.show()
        plt.plot(t, v)
        plt.show()
        plt.plot(t, a)
        plt.show()
