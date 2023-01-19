import json
from pathlib import Path

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])

print(mags[:10])
print(lons[:5])
print(lats[:5])
