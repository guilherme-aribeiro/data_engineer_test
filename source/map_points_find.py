import pandas as pd
from shapely import geometry
import database
import geopandas as gpd
from shapely.geometry import Point,Polygon


sql_pickup = "SELECT CAST(data ->> 'pickup_longitude' AS NUMERIC), CAST(data ->> 'pickup_latitude' AS NUMERIC) from dados WHERE EXTRACT(YEAR FROM(CAST (data ->> 'pickup_datetime' AS TIMESTAMP))) = 2010 and (CAST(data ->> 'pickup_longitude' AS NUMERIC) BETWEEN -74.3 AND -73.65) AND (CAST (data ->> 'pickup_latitude' AS NUMERIC) BETWEEN 40.45 AND 40.99) ;"
sql_dropoff = "SELECT CAST(data ->> 'dropoff_longitude' AS NUMERIC), CAST(data ->> 'dropoff_latitude' AS NUMERIC) from dados WHERE EXTRACT(YEAR FROM(CAST (data ->> 'pickup_datetime' AS TIMESTAMP))) = 2010 and (CAST(data ->> 'dropoff_longitude' AS NUMERIC) BETWEEN -74.3 AND -73.65) AND (CAST (data ->> 'dropoff_latitude' AS NUMERIC) BETWEEN 40.45 AND 40.99) ;"

df_pickup=pd.DataFrame(database.consulta_sql(sql_pickup),columns=['longitude','latitude'])
df_dropoff=pd.DataFrame(database.consulta_sql(sql_dropoff),columns=['longitude','latitude'])


def get_pickup_points():
    geometry_pickup = [Point(xy) for xy in zip(df_pickup['longitude'],df_pickup['latitude'])]
    geo_df = gpd.GeoDataFrame(df_pickup,crs='EPSG:4326',geometry=geometry_pickup)
    return geo_df
def get_dropoff_points():
    geometry_dropoff = [Point(xy) for xy in zip(df_dropoff['longitude'],df_dropoff['latitude'])]
    geo_df = gpd.GeoDataFrame(df_dropoff,crs='EPSG:4326',geometry=geometry_dropoff)
    return geo_df

