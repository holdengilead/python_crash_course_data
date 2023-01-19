import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)
reader = list(reader)

highs = [int(row[4]) for row in reader]
lows = [int(row[5]) for row in reader]
dates = [datetime.strptime(row[2], "%Y-%m-%d") for row in reader]

# Plot the high  and low temperatures.
plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
