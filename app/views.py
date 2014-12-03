from django.shortcuts import render
from db_controller import *
from networkx import *
import json
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import LineString
from django.http import HttpResponse
import cPickle

def display(request, topLeftX, topLeftY, botRightX, botRightY, floorname):
    tlx = float(topLeftX)
    tly = float(topLeftY)
    brx = float(botRightX)
    bry = float(botRightY)
    rect = Polygon( ((tlx,tly),(brx,tly),(brx,bry),(tlx,bry),(tlx,tly)) )
    bldgList = get_buildings_from_rectangle(rect)
    plansList = []
    for bldg in bldgList:
        floorplan = get_plan_from_floor_and_building(floorname, bldg)
        plansList.append(floorplan)
    return HttpResponse("["+(','.join(str(fp) for fp in plansList))+"]")

def query(request, building_id):
    bldgID = int(building_id)
    roomList = get_rooms_from_building(bldgID)
    roomNameList = map(lambda x: x.name, roomList)
    return HttpResponse(json.dumps(roomNameList))

def route(request, room1_id, room2_id, building_id):
    bldgID = int(building_id)
    room1 = int(room1_id)
    room2 = int(room2_id)
    G = get_graph_from_building(bldgID)
    sp = shortest_path(G, room1, room2)
    pointList = map(get_anchor_from_room_id, sp)
    return HttpResponse((LineString(pointList)).json)

# Create your views here.
