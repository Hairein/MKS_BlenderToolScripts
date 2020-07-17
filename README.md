# MKS_BlenderToolScripts

MKS Blender Scene Definition Exporter v1.0 (JSON)

by Micah Koleoso Software, 2020

[www.micahkoleoso.de](http://www.micahkoleoso.de)


For fixes, changes, feature requests, email [maakoleoso@gmx.de](mailto:maakoleoso@gmx.de)

but please add "Blender JSON Exporter" in the header to speed up me reading the mail.


This script exports the hierachical scene defintion in a JSON format for parsing in 

other applications and tools.


## OBJECTS OUTPUT DATA:

### MESHES/LIGHTS/CAMERAS
"name" = scene_object.name  [Text with name as shown in Blender]

"type" = scene_object.type  [Text: 'MESH','LIGHT','CAMERA']

"visibility" = scene_object.hide_render [True/False]

"collider" = scene_object.collision.use [True/False]


"location" = (x,y,z) [floats, scene_object.location]

"rotation" = (x,y,z) [floats, Converted to degrees from scene_object.rotation_euler]

"scale" = (x,y,z) [floats, scene_object.scale]


"parent_index" = [Number, finds a parent's index or -1]   


Also, additional parameters for lights and cameras are output.

## Tested on Blender v2.83.2 LTS