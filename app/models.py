from django.contrib.gis.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor)
    building = models.ForeignKey(Building)
    anchor = models.PointField()
    
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name

class Building(object):
    name = models.CharField(max_length=50)
    graph = models.CharField() # To be revised
    shape = models.PolygonField()

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name

class Floor(object):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    building = models.ForeignKey(Building)
    plan = models.CharField() # To be revised

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name