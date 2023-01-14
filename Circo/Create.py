import simplekml
import math

circlePoints = []
counter=0
latitude = []
longitude = []
radius = []
def extract():
    file = open('input.txt', 'r')
    for i in file:
        lines = file.readlines()
        for j in lines:
            if 'latitude' in j:
                lat1 = j.split(':')
                lat = lat1[1].split(',')
                lat2 = lat[0]
                lat3 = lat2.replace(" ", "")
                latitude.append(float(lat3))
            if 'longitude' in j:
                lon1 = j.split(':')
                lon = lon1[1].split(',')
                lon2 = lon[0]
                lon3 = lon2.replace(" ", "")
                longitude.append(float(lon3))
            if 'cylinder_radius' in j:
                rad1 = j.split(':')
                rad = rad1[1].split(',')
                rad2 = rad[0]
                rad3 = rad2.replace(" ","")
                radius.append(int(rad3))
        return len(latitude)


def GenCirc(lat,long,rad):
    radius = rad         # m - the following code is an approximation that stays reasonably accurate for distances < 100km
    centerLat = lat      #Latitude in degree
    centerLon = long     #Longitute in degree
    N = 500
    for k in range(N):
        angle = math.pi * 2 * k / N
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        point = {}
        point[1] = centerLat + (180 / math.pi) * (dy / 6378137)
        point[0] = centerLon + (180 / math.pi) * (dx / 6378137) / math.cos(centerLat * math.pi / 180)
        circlePoints.append(point)

def create():
    num = extract()
    kml = simplekml.Kml()
    name = 'Roshan'
    width = 5
    for i in range(num):
        rad = radius[i]*0.3048
        GenCirc(latitude[i],longitude[i],rad)
        nname = name + str(i)
        gen = kml.newlinestring(name = nname,
                                coords=circlePoints)
        gen.style.linestyle.color = simplekml.Color.red
        gen.style.linestyle.width = width
        del circlePoints[:]

    kml.save('circle2.kml')

create()