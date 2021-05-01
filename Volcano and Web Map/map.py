import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
volname = list(data["NAME"])
location = list(data["LOCATION"])
voltype = list(data["TYPE"])


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My map")


for lt, ln, el, name, loc in zip(lat, lon, elev, volname, location,):
    html = """<h4>Volcano Information:</h4>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
    <br>Location: %s 
    <br>Height: %s m
    """
    iframe = folium.IFrame(html=html % (
        name, name, loc, el), width=200, height=150)
    fg.add_child(folium.Marker(location=[
                 lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("map.html")
