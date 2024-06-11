from routingpy import Graphhopper
import folium

filename = 'apikey'


def get_file_contents(filename):
    """ Given a filename, return the contents of that file """
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


api_key = get_file_contents(filename)
# Some locations in Berlin
coords = [[13.413706, 52.490202],
          [13.421838, 52.514105],
          [13.453649, 52.507987],
          [13.401947, 52.543373]]

client = Graphhopper(api_key=api_key)
route = client.directions(locations=coords, profile='car')


def convert_coord(coordinates):
    coordinates1 = [None, None]
    coordinates1[0] = coordinates[1]
    coordinates1[1] = coordinates[0]
    return coordinates1


# pprint((route.geometry, route.duration, route.distance, route.raw))
m = folium.Map(location=convert_coord(coords[0]), zoom_start=11)
geometry = []
for i in range(len(route.geometry)):
    geometry.append(convert_coord(route.geometry[i]))

for i in coords:
    folium.Marker(
        location=convert_coord(i),
        tooltip="Click me!",
        icon=folium.Icon(color="green"),
    ).add_to(m)
folium.PolyLine(geometry, tooltip="Coast").add_to(m)

m.save("index.html")
