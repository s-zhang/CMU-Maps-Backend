from django.contrib.gis.db import models

class Building(models.Model):
    name = models.CharField(max_length=50)
    graph = models.FileField(upload_to="graphs")
    shape = models.PolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(max_length=50)
    level = models.FloatField()
    building = models.ForeignKey(Building)
    plan = models.FileField(upload_to="plans")

    objects = models.GeoManager()

    def __unicode__(self):
        return self.building.name + "_" + self.name

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor)
    building = models.ForeignKey(Building)
    anchor = models.PointField()
    
    objects = models.GeoManager()

    def __unicode__(self):
        return self.building.name + "_" + self.name