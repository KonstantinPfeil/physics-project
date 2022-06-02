import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

with open("mtimes.txt") as f:
    times = json.loads(f.read())["times"]   # read times from file

weg = [(x+1)*0.20 for x, v in enumerate(times)]
weg.insert(0, 0)  # insert zero point
timeDifferences = [t - times[x - 1] for x, t in enumerate(times) if x > 0]

speeds = [0.20/t for t in timeDifferences]
speedDifferences = [v - speeds[x - 1] for x, v in enumerate(speeds) if x > 0]

accelerations = [v / t for v, t in zip(speedDifferences, timeDifferences[1:])]
meanAcceleration = sum(accelerations) / len(accelerations)

firstTime = np.sqrt(0.4 / meanAcceleration)
times.insert(0, firstTime)
times = [t - times[0] for t in times]

speedDifferences.insert(0, times[1] - times[0])  # create new difference with new time

speeds.insert(0, 0.2 / timeDifferences[0])  # first and second speed
speeds.insert(0, 0.2/firstTime)

accelerations.insert(0, None)# dummy data
accelerations.insert(0, None)
accelerations.insert(0, None)


plt.plot(times, weg)
plt.show()

plt.plot(times, speeds)
plt.show()

plt.plot(times, accelerations)
plt.show()
