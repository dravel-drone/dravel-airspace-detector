import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import time

shp_file_path = './data/areas.shp'
shp_data = gpd.read_file(shp_file_path)
print(shp_data.head())
shp_data.info()

shp_data.convex_hull.plot(color='gray', edgecolor="w")
plt.show()

point = Point(126.717336, 37.269765)

start = time.time()

region = shp_data[shp_data.geometry.contains(point)]
print(region)
print(region.shape[0])
if not region.empty:
    for c in range(region.shape[0]):
        print(f"{region.iloc[c, 0]} {region.iloc[c, 1]} {region.iloc[c, 2]}")
