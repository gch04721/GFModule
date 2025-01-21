import requests, googlemaps

# this method using google maps api and convert address to gps coord
def convertGPSCoord(origin: str):
    gmaps = googlemaps.Client(key = tmp)

    geocode_res = gmaps.geocode(origin)

    if geocode_res:
        loc = geocode_res[0]['geometry']['location']
        lat = loc['lat']
        lng = loc['lng']
        return lat, lng
    else:
        return None, None
