import pandas as pd
import folium 
import geopandas

buildings = 'https://raw.githubusercontent.com/sdsu-fis/super-basemap-test/master/buildings.geojson'

m = folium.Map(location=[32.77460, -117.07195], zoom_start=15.4)

folium.GeoJson(
    buildings,
    name='geojson'
).add_to(m)

folium.LayerControl().add_to(m)


m.save('index.html')
