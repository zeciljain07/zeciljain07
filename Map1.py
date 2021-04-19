import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name= list(data["NAME"])

html = """Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1700:
        return 'blue'
    elif 1700 <= elevation < 2500:
        return 'green'
    elif 2500 <= elevation < 3200:
        return 'orange'
    else :
        return 'red'


map = folium.Map(location=[23.05894, 72.58937], zoom_start=5, tiles= "Stamen Terrain")

fgv= folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev,name ):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location = (lt, ln),radius = 6, popup= folium.Popup(iframe), parse_html = True, icon=folium.Icon(color=color_producer(el)),
    fill_color= color_producer(el), color = 'grey', fill_opacity = 0.8))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'blue' if 20000000 <= x['properties']['POP2005'] < 30000000
else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map_html_popup_advanced.html")
