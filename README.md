# Anaxi Tile Downloader
Downloads and stitches images downloaded from Map Tile servers.

## Dependencies
Assuming you have Python 3 installed and in your `$PATH`, you can run `pip3 install -r requirements.txt` and all required dependencies will be installed. For best results, use a [VirtualEnv](https://virtualenv.pypa.io/en/stable/userguide/#). If you'd prefer not to use requirements.txt, the manual install instructions are below.

* Python 3
* Python Requests (`pip3 install --user requests==2.*`)
* Python Pillow (`pip3 install --user Pillow=6.*`) -- optional, used for image stitching

## Usage
After ensuring your dependencies are installed, you can run the program with `python3 tsdl.py`. It will prompt you for your bounding Lat and Long coordinates, zoom, and tile server URL. For best results, the larger the area you select with your lat & long, the smaller you should have your zoom. If your zoom is too big, downloading will take longer, your resulting stitched file will be larger, and the tile server may throttle / restrict your usage. See this [OpenStreetMap Wiki page](https://wiki.openstreetmap.org/wiki/Zoom_levels) for scaling and examples.

The program will tell you the coords it rounded to (make a note of these for geolocation, they are the top right and bottom left of the generated image), and start downloading the tiles to the `tiles/` folder. 

After downloading all tiles, you will be asked if you'd like to stitch together the images. Type "y" to continue, or anything else to exit. The tiles will be stitched together, and saved to a file named with the pattern `Map_XMIN-XMAX_YMIN-YMAX.(.png|.jpg)`. 

## Example
The following example will download and stitch tiles within an area of the MIT campus in Cambridge, Massachusetts.
```
$ python3 tsdl.py
Starting Anaxi Tile Downloader...
Enter Starting Latitude: 42.363531
Enter Starting Longitude: -71.096362
Enter Ending Latitude: 42.354185
Enter Ending Longitude: -71.069741
Zoom / Level of Detail (usually 0-18, larger = more data & detail): 16
Tile Server URL: https://b.tile.openstreetmap.org/%zoom%/%xTile%/%yTile%.png
Starting at North-West corner: [42.366661663732735, -71.0980224609375]
Ending at South-East corner: [42.34636533160188, -71.0595703125]
Downloading X tiles 19825 through 19831
Downloading Y tiles 24238 through 24242
Downloading a total of 35 tiles
Downloading https://b.tile.openstreetmap.org/16/19825/24238.png to 16_19825_24238.png
Downloading https://b.tile.openstreetmap.org/16/19826/24238.png to 16_19826_24238.png
Downloading https://b.tile.openstreetmap.org/16/19827/24238.png to 16_19827_24238.png
...
Downloading successful! Would you like to stitch images together? (y/N) y
Stitching 16_19829_24242.png
Stitching 16_19830_24242.png
Stitching 16_19831_24242.png
...
Format to save as [Blank for suggested, or .jpg, .png, .tiff, etc]: 
Saving to Map_16_19825-19831_24238-24242.png...
Stitched image saved to /Users/conlanc/TSdl/tiles/Map_16_19825-19831_24238-24242.png
```

## Potential Servers
Below is a small list of sources for Tile Servers. Beware, some of the linked servers have restrictions on usage, zoom, and may throttle or deny service if you violate their terms. 

To format the URL correctly, replace the zoom, x tile, and y tile spot with %zoom%, %xTile%, and %yTile% respectively. Ensure that the URL ends in a file extension (usually .jpg for satellite / terrain maps and .png for others), and that the tile server returns images that are 256px by 256px. You should have something that looks like this: `https://b.tile.openstreetmap.org/%zoom%/%xTile%/%yTile%.png` 

* [MapTiler Cloud](https://cloud.maptiler.com/maps/) (free account for non-commercial use)
* https://wiki.openstreetmap.org/wiki/Tile_servers
* https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Tile_servers
* https://www.trailnotes.org/FetchMap/TileServeSource.html
* https://raw.githubusercontent.com/klakar/QGIS_resources/master/collections/Geosupportsystem/python/qgis_basemaps.py
