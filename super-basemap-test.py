import pandas as pd
import pylint.test.functional.duplicate_argument_name

m = folium.Map(location=[32.77460, -117.07195], zoom_start=15.4)

m.save('index.html')