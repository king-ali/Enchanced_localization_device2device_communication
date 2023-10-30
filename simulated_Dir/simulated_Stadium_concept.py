import math
import matplotlib.pyplot as plt
import random
import secrets
import numpy as np
from datetime import datetime
from datetime import timedelta
from Device import Device
import pandas as pd
# import geopandas
  # more options can be specified also

plt.rcParams['axes.facecolor'] = 'black'

points = 1000
# radius of the circle
circle_r = 100
# center of the circle (x, y)
circle_x = 110
circle_y = 110
# error_x = 0.2
# error_y = 0.2

bottomLeft = (0, 0)
bottomRight = (250,0)
topLeft = (0, 250)
topRight = (250, 250)

cols = np.linspace(bottomLeft[0], bottomRight[0], num=50)
rows = np.linspace(bottomLeft[1], topLeft[1], num=50)


datapoints = []
devices={}
data = []
# random angle

for number in range(points):
##############################################################
    ### Generate Hash
    hash = secrets.token_hex(nbytes=16)
##########################################################
    alpha = 2 * math.pi * round(random.random(), 3)
    # random radius
    r = circle_r * math.sqrt(round(random.uniform(0.8, 1),2))
    # calculating coordinates
    org_x = round(r * math.cos(alpha) + circle_x, 7)
    org_y = round(r * math.sin(alpha) + circle_y, 7)
    plt.plot(org_x,org_y, 'bo')
############################################################
############## Randomized GPS position for that position ########
    alpha = 2 * math.pi * random.random()
    random_GPS_error = random.uniform(2,15)

    err = random_GPS_error * math.sqrt(random.uniform(1,2))
    # calculating coordinates
    gps_x = round(err * math.cos(alpha) + org_x, 7)
    gps_y = round(err * math.sin(alpha) + org_y, 7)
    plt.plot(gps_x, gps_y, 'rx')

    # print("Hash: " + hash + " original points: " + str(org_x) + " " + str(org_y) + " gps: " + str(gps_x) + " " + str(gps_y) )

    devices[hash] = Device(hash, gps_x,gps_y,org_x,org_y)
    data.append([hash, gps_x,gps_y,org_x,org_y])

plt.show()


df = pd.DataFrame(data, columns=['Hash', 'gpsX', 'gpsY', 'orgX', 'orgY'])

print(df.head())





gps_points = [df["gpsX"].tolist(),df["gpsY"].tolist()]
# distances, bt = distance(gps_points)




df['col'] = np.searchsorted(cols, df['gpsY'])
df['row'] = np.searchsorted(rows, df['gpsX'])

plt.plot(df['col'], df['row'], 'wo', alpha= 0.1)

plt.show()

# df1 = df.loc[(df['row'] > 5) | (df['col'] >= 5)]
# df2 = df.loc[(df['row'] <= 5) & (df['col'] <= 5)]

df1 = df.loc[(df['row'] > 5)]
df2 = df.loc[(df['row'] <= 5)]

plt.plot(df1['orgX'], df1['orgY'], 'gx', alpha= 0.1)
plt.plot(df2['orgX'], df2['orgY'], 'wo', alpha= 0.1)

plt.show()

# print(df)
df.to_csv("simulated_stadium_concept.csv")





def wave_gen(df, show_Time_seconds, grid, start_Time):
    def neighbours(x, y):
        pn = [(x - 1, y), (x + 1, y), (x - 1, y - 1), (x, y - 1),
              (x + 1, y - 1), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        for i, t in enumerate(pn):
            if t[0] < 0 or t[1] < 0 or t[0] >= grid or t[1] >= grid:
                pn[i] = None
        return [c for c in pn if c is not None]

    def column_Wave(df, time_lap, grid):
        for index in range(grid):
            df.loc[df['row'] == index, 'play_Time'] = time_lap[index]
        return df

    time_lap = []
    UTC_Time_Delta = timedelta(seconds=show_Time_seconds/grid)
    for i in range(grid):
        start_Time = start_Time + UTC_Time_Delta
        time_lap.append(start_Time)

    cols = np.linspace(bottomLeft[0], bottomRight[0], num=grid)
    rows = np.linspace(bottomLeft[1], topLeft[1], num=grid)

    df['col'] = np.searchsorted(cols, df['gpsY'])
    df['row'] = np.searchsorted(rows, df['gpsX'])

    traversed_Blocks = []
    start_Point = (0,0)

    df = column_Wave(df,time_lap,grid)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df.head(10))





UTC_Time = datetime.utcnow()
UTC_Time.strftime("%Y-%m-%dT%H:%M:%S%Z")
scheduled_UTC_Time = UTC_Time + timedelta(seconds=30)
show_Time_seconds = 10
grain = 50

# wave_gen(df, show_Time_seconds,grain, scheduled_UTC_Time)

