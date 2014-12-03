from models import Room, Floor, Building
import cPickle, json

def get_buildings_from_rectangle(rectangle):
    return Building.objects.filter(shape__intersects=rectangle)

def get_plan_from_floor_and_building(floor_name, building):
    floor = Floor.objects.get(name=floor_name, building=building)
    floor.plan.open(mode="r")
    with floor.plan.file:
        return floor.plan.file.file.readlines()

def get_floors_from_building(building):
    return building.floor_set.order_by("level")

def get_building_from_room(room):
    return room.building

def get_graph_from_building(building):
    building.graph.open(mode="r")
    with building.graph.file:
        return cPickle.load(building.graph.file.file)

def get_anchor_from_room_id(room_id):
    return Room.objects.get(id=room_id).anchor

def get_rooms_from_building(building_id):
    return Room.objects.filter(building_id=building_id)
