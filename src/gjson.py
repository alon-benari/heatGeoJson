import random
from geojson import Point, Feature, FeatureCollection,dumps, dump


class GeoPoints():
  
  def __init__(self):
    """
    """
    lon = [ random.uniform(-121.3,-121.6) for i in range(1000)]
    lat = [ random.uniform(38.5,38.6) for i in range(1000)]
    self.points = [ Feature(geometry = Point((ln,lt)),properties = {'value':random.randint(10,100)}) for ln,lt in zip(lon,lat)]
    self.fc = FeatureCollection(self.points)
    with open('test.geojson','w') as outfile:
      dump(FeatureCollection(self.points),outfile)
    outfile.close()

######
gp = GeoPoints()