import pandas as pd 
import numpy as np

path = input("Filename: ")
print(path)
file = pd.read_excel(path)
magnet = pd.DataFrame(file, columns=["locationHeadingZ","locationHeadingTimestamp_since1970"])
print(magnet.to_numpy)