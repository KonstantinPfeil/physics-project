import json
import matplotlib.pyplot as plt
import numpy as np


def calculate():
    try:
        with open("mtimes.txt") as f:
            times = json.loads(f.read())["times"]  # read times from file
    except FileNotFoundError:
        print("no mtimes.txt file")
        return None

    weg = [x * 0.20 for x in range(len(times) + 1)]

    timeDifferences = [t - times[x - 1] for x, t in enumerate(times) if x > 0]

    speeds = [0.20 / t for t in timeDifferences]
    speedDifferences = [v - speeds[x - 1] for x, v in enumerate(speeds) if x > 0]

    accelerations = [v / t for v, t in zip(speedDifferences, timeDifferences[1:])]
    meanAcceleration = sum(accelerations) / len(accelerations)

    firstTime = np.sqrt(0.4 / meanAcceleration)
    times.insert(0, firstTime)
    times = [t - times[0] for t in times]

    speedDifferences.insert(0, times[1] - times[0])  # create new difference with new time

    speeds.insert(0, 0.2 / timeDifferences[0])  # first and second speed
    speeds.insert(0, 0.2 / firstTime)

    accelerations.insert(0, None)  # dummy data
    accelerations.insert(0, None)
    accelerations.insert(0, None)
    return times, weg, speeds, accelerations


if __name__ == "__main__":
    calculation = calculate()
    if calculation is not None:
        t, s, v, a = calculation
        plt.plot(t, s)
        plt.show()
        plt.plot(t, v)
        plt.show()
        plt.plot(t, a)
        plt.show()
