import json

# x = '{"name":"Green Mountain","id":1,"polypoints":[{"id":1,"trailId":1,"lat":53.5682315,"long":-113.5017332},{"id":2,"trailId":1,"lat":53.5682241,"long":-113.5017475},{"id":3,"trailId":1,"lat":53.5682241,"long":-113.5017475},{"id":4,"trailId":1,"lat":53.5682241,"long":-113.5017475},{"id":5,"trailId":1,"lat":53.5682043,"long":-113.5017375},{"id":6,"trailId":1,"lat":53.5682043,"long":-113.5017375},{"id":7,"trailId":1,"lat":53.5682043,"long":-113.5017375},{"id":8,"trailId":1,"lat":53.5681971,"long":-113.5016921},{"id":9,"trailId":1,"lat":53.5682256,"long":-113.5017192}],"pointOfInterests":[{"id":1,"trailId":1,"lat":53.5681971,"long":-113.5016921}]}'
with open('polytest.json') as json_data:
    data = json.load(json_data,)
try:
    index = 1200
    cityID = 2
    trailID = 5
    file = open("latlong.txt", "w")
    for element in data['polypoints']:
        value = """\n Insert into Polylines (polylineId, cityId, markerId, trailId, lat, long) Values ({0}, {1}, 1, {2}, {3}, {4});""".format(
            index, cityID, trailID, element['lat'], element['long'])
        file.write(value)
        index = index+1

except (ValueError, KeyError, TypeError):
    print('no dice')


