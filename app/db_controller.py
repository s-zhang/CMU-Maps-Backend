from models import Room, Floor, Building
import marshal

def get_buildings_from_rectangle(rectangle):
    return Building.objects.filter(shape__intersects=rectangle)

def get_plan_from_floor_and_building(floor_name, building):
    floor = Floor.objects.get(name=floor_name, building=building)
    return floor.plan

def get_floors_from_building(building):
    return building.floor_set.order_by("level")

def get_building_from_room(room):
    return room.building

def get_graph_from_building(building):
    building.graph.open(mode="r")
    with building.graph.file:
        return marshal.load(building.graph.file.file)

def get_anchor_from_room_id(room_id):
    return Room.objects.get(id=room_id).anchor