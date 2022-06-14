import os
import json
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional
import math


# If you do type highlighting also highlight return values. use typing libary for giving back a Tuple[]
# filled with the datatypes
def calculate(times: Optional[List[float]] = None):
    if times is None:  # DO NEVER SET DEFAULTS WITH MUTABLE DATATYPES
        times = []

    if not times:
        try:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mtimes.txt")) as f:
                times = json.loads(f.read())["times"]  # read times from file
        except FileNotFoundError:
            print("no mtimes.txt file \n try auslesen.py")
            return None
        if not times:
            return None

    weg = [x * 0.20 for x in range(len(times) + 1)]

    # t and v are shadowing from outerscope (the "main" if) please create a main function and call that in the if
    timeDifferences = [t - times[x - 1] for x, t in enumerate(times) if x > 0]

    speeds = [0.20 / t for t in timeDifferences]
    speedDifferences = [v - speeds[x - 1] for x, v in enumerate(speeds) if x > 0]

    accelerations = [v / t for v, t in zip(speedDifferences, timeDifferences[1:])]
    averageAcceleration = sum(accelerations) / len(accelerations)

    firstTime = np.sqrt(0.4 / accelerations[0])
    times.insert(0, firstTime)
    times = [t - times[0] for t in times]

    averageSpeed = [averageAcceleration * t for t in times]
    predictedDistance = [(averageAcceleration / 2) * t**2 for t in times ]
    speedDifferences.insert(0, times[1] - times[0])  # create new difference with new time

    # first and second speed
    speeds.insert(0, 0.2 / firstTime)
    speeds.insert(0, 0)  # zero point

    accelerations.insert(0, averageAcceleration)  # dummy data
    accelerations.insert(0, averageAcceleration)
    accelerations.insert(0, averageAcceleration)

    averageAcceleration = [averageAcceleration for t in times]

    # you do know that you are giving back a mutable datatype?
    # the list you put into the function is also edited meaning that giving time is useless
    return times, weg, speeds, accelerations, predictedDistance, averageSpeed, averageAcceleration,


# again: highlight return values
def scatter(name: str, x, y, c: Optional[str] = None, size: Optional[int] = None):
    plt.scatter(x, y, color=c, s=size)
    # use underscores for variable names e.g. x_name
    # this is a pep standard
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
