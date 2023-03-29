import googlemaps, requests, json, xmltodict
api_key = 'AIzaSyAXuWzRXEXR12699Z24GUNDgBhJy2_CYKs'
locs = [
    'UMT, Lahore',
    'Government College Township,Lahore For Boys',
    'Ilam Deen Chowk Lahore',
    'FAST NUCES Lahore Campus, 852-B Milaad St, Block B Faisal Town, Lahore, Punjab 54000, Pakistan',
    'Forks N Knives Pizza Kitchen Lahore'
]


def find_all_markets_near(place):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/xml?query=market+near+{}&key={}'.format(place, api_key)
    r = requests.get(url)
    places = xmltodict.parse(r.text)
    for _place in places['PlaceSearchResponse']['result']:
        find_dist(str(_place), place)
        print(_place['name'])


def find_all_schools_near(place):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/xml?query=school+near+{}&key={}'.format(place, api_key)
    r = requests.get(url)
    places = xmltodict.parse(r.text)
    for _place in places['PlaceSearchResponse']['result']:
        find_dist(str(_place), place)
        print(_place['name'])


def find_dist(place_1, place_2):
    gmaps = googlemaps.Client(key=api_key)
    my_dist = gmaps.distance_matrix(place_1, place_2)['rows'][0]['elements'][0]
    print(my_dist['distance']['text'])


def find_nearest_by_filter(long, lat, radius, type):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?location={},{}&radius={}&type={}&key={}'\
        .format(long, lat, radius, type, api_key)
    r = requests.get(url)
    places = xmltodict.parse(r.text)
    for _place in places['PlaceSearchResponse']['result']:
            print(_place['name'])


if __name__ == '__main__':
    # find_nearest_by_filter('31.4815258', '74.3008254', '400', 'market')
    find_all_schools_near('fast lahore')