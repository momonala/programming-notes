
import httplib2
import json 

def getLocation(loc): 
    key = 'AIzaSyAVozrGa_UhjJ8SpjNQIYEbbCeStWN4WrE'
    loc = loc.replace(' ', '+')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(loc, key)

    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)

    lat = result['results'][0]['geometry']['location']['lat']
    lng = result['results'][0]['geometry']['location']['lng']
    return lat, lng

addresses = ['Tokyo, Japan',
             'Jakarta, Indonesia',
             'Maputo, Mozabique', 
             'Geneva, Switerland', 
             'Los Angeles, California, USA']

r = []
for a in addresses: 
    lat, lon = getLocation(a)
    print (a, lat, lon)

print (r)
