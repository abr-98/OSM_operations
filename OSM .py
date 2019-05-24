#!/usr/bin/env python
# coding: utf-8

# In[5]:


import osmnx as ox
city = ox.gdf_from_place('Berkeley, California')
ox.plot_shape(ox.project_gdf(city))


# In[10]:


places = ox.gdf_from_places(['Botswana', 'Zambia', 'Zimbabwe'])
places = ox.project_gdf(places)
ox.save_gdf_shapefile(places)
ox.plot_shape(ox.project_gdf(places))


# In[11]:


G = ox.graph_from_bbox(37.79, 37.78, -122.41, -122.43, network_type='drive')
G_projected = ox.project_graph(G)
ox.plot_graph(G_projected)


# In[12]:


G = ox.graph_from_point((37.79, -122.41), distance=750, network_type='all')
ox.plot_graph(G)


# In[14]:


G = ox.graph_from_address('350 5th Ave, New York, New York', network_type='drive')
ox.plot_graph(G)


# In[31]:


import osmnx as ox
import pandas as pd
import numpy as np

df=pd.read_csv('6mar.csv')

st_lat=df['Start_Lat'].values
st_lng=df['Start_Lng'].values
end_lat=df['End_Lat'].values
end_lng=df['End_Lng'].values

print("a")

st_latl=st_lat.tolist()
st_lngl=st_lng.tolist()

print("b")

end_latl=end_lat.tolist()
end_lngl=end_lng.tolist()

print("c")

l=len(st_latl)

print("d")
print(st_latl[0])
print(st_lngl[0])
print(end_latl[0])
print(end_lngl[0])
G = ox.graph_from_bbox(st_latl[2], end_latl[2], st_lngl[2],end_lngl[2], network_type='drive')
G_projected = ox.project_graph(G)
ox.plot_graph(G_projected)


# In[36]:


import osmnx as ox
G = ox.graph_from_place('Modena, Italy')
ox.plot_graph(G)


# In[ ]:


import osmnx as ox
G = ox.graph_from_place('Kolkata, India')
ox.plot_graph(G)


# In[39]:


from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
df = pd.read_csv('6mar.csv')
# the columns of the DataFrame
df.columns
([u'ID', u'X', u'Y'], dtype='object')
df['geometry'] = df.apply(lambda row: Point(row.X, row.Y), axis=1)
df  = gpd.GeoDataFrame(df)


# In[ ]:




