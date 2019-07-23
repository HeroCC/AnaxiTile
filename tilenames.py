# Translates between lat/long and the slippy-map tile
# numbering scheme
# 
# http://wiki.openstreetmap.org/index.php/Slippy_map_tilenames
# 
# Written by Oliver White, 2007 (https://svn.openstreetmap.org/applications/routing/pyroute/tilenames.py)
# Adapted by Conlan Cesar, 2019
# This file is public-domain

from math import *


def numTiles(z):
    return (pow(2, z))


def sec(x):
    return (1 / cos(x))


def latlon2relativeXY(lat, lon):
    x = (lon + 180) / 360
    y = (1 - log(tan(radians(lat)) + sec(radians(lat))) / pi) / 2
    return (x, y)


def latlon2xy(lat, lon, z):
    n = numTiles(z)
    x, y = latlon2relativeXY(lat, lon)
    return (n * x, n * y)


def tileXY(lat, lon, z, raw=False):
    x, y = latlon2xy(lat, lon, z)
    if raw:
        return (x, y)
    return (int(x), int(y))


def xy2latlon(x, y, z):
    n = numTiles(z)
    relY = y / n
    lat = mercatorToLat(pi * (1 - 2 * relY))
    lon = -180.0 + 360.0 * x / n
    return (lat, lon)


def latEdges(y, z):
    n = numTiles(z)
    unit = 1 / n
    relY1 = y * unit
    relY2 = relY1 + unit
    lat1 = mercatorToLat(pi * (1 - 2 * relY1))
    lat2 = mercatorToLat(pi * (1 - 2 * relY2))
    return (lat1, lat2)


def lonEdges(x, z):
    n = numTiles(z)
    unit = 360 / n
    lon1 = -180 + x * unit
    lon2 = lon1 + unit
    return (lon1, lon2)


def tileEdges(x, y, z):
    lat1, lat2 = latEdges(y, z)
    lon1, lon2 = lonEdges(x, z)
    return ((lat2, lon1, lat1, lon2))  # S,W,N,E


def mercatorToLat(mercatorY):
    return (degrees(atan(sinh(mercatorY))))


def tileLayerBase(layer):
    layers = { \
        "tah": "http://cassini.toolserver.org:8080/http://a.tile.openstreetmap.org/+http://toolserver.org/~cmarqu/hill/",
        # "tah": "http://tah.openstreetmap.org/Tiles/tile/",
        "oam": "http://oam1.hypercube.telascience.org/tiles/1.0.0/openaerialmap-900913/",
        "mapnik": "http://tile.openstreetmap.org/mapnik/"
    }
    return (layers[layer])
