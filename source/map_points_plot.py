from matplotlib.colors import Colormap
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point,Polygon
import map_points_find as mp

ny_map= gpd.read_file('maps\geo_export_93bd3506-1879-4393-aeb2-96d9386527cd.shp')

fig,ax= plt.subplots(figsize=(15,15))
ny_map.plot(ax=ax,color='grey')

print("já consultou")
mp.get_dropoff_points().plot(ax=ax,color='blue',marker='o',markersize=1 , label='Dropoff points')
mp.get_pickup_points().plot(ax=ax,color='red',marker='o',markersize=1, label= 'Pickup Points')
plt.legend(prop={'size' : 15})
plt.show()
