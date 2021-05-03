import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
volname = list(data["NAME"])
location = list(data["LOCATION"])
voltype = list(data["TYPE"])


def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 2500:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")


for lt, ln, el, name, loc in zip(lat, lon, elev, volname, location,):
    html = """<h4>Volcano Information:</h4>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
    <br>Location: %s 
    <br>Height: %s m
    """
    iframe = folium.IFrame(html=html % (
        name, name, loc, el), width=200, height=150)
    fgv.add_child(folium.CircleMarker(location=[
        lt, ln], popup=folium.Popup(iframe), radius=7, fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(
    data=open("world.json", 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())


map.save("map.html")
