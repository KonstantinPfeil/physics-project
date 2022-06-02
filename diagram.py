import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

with open("mtimes.txt") as f:
    times = json.loads(f.read())["times"]   # read times from file

weg = [(x+1)*0.20 for x, v in enumerate(times)]
timeDifferences = [t - times[x - 1] for x, t in enumerate(times) if x > 0]
speeds = [0.20/t for t in timeDifferences]
speedDifferences = [v - speeds[x - 1] for x, v in enumerate(speeds) if x > 0]
accelerations = [v / t for v, t in zip(speedDifferences, timeDifferences[1:])]
meanAcceleration = sum(accelerations) / len(accelerations)
firstSpeed = speeds[0] - np.sqrt(meanAcceleration * 2 * 0.2)
speeds.insert(0, firstSpeed)
print(firstSpeed)
print(0.2 / firstSpeed)
firstTimeDifference = times[0] - 0.2 / firstSpeed
timeDifferences.insert(0, firstTimeDifference)
times.insert(0, firstTimeDifference)
"""for x, t in enumerate(times):
    print(f"{x}: {t}")"""
times = [t - times[0] for t in times]
# print(times)
timeDifferences.insert(0, firstTimeDifference)
accelerations.insert(0, [None, None])   # dummy data
""" Adding zero points"""

