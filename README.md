# MKS Blender Scene Definition Exporter (JSON)

This script exports the hierarchical scene definition in a JSON format for parsing in other applications and tools.


by Micah Koleoso Software, 2020, 2025

[www.micahkoleososoftware.com](http://www.micahkoleososoftware.com)



For bug reports, fixes, change or feature requests, please email [micah@micahkoleososoftware.com](mailto:micah@micahkoleososoftware.com)

and please add "Blender JSON Exporter" in the header to speed up me reading the mail.



## OBJECTS OUTPUT DATA:

### Common Empty|Mesh|Light|Camera parameters

    "name" = [Text with name as shown in Blender]

    "full_name" = [Text with name and postfix (aaa.bbb) as shown in Blender]

    "base_name" = [Text with name without postfix as shown in Blender]

    "type" = ['EMPTY'|'MESH'|'LIGHT'|'CAMERA']

    "id_type" = ['SCENE'|'OBJECT' only based on the type parsed above in type]

    "tag" = ['True'|'False']

    "visibility" = ['True'|'False']

    "collision_settings" = [Collision settings where use is set to true]
        - absorption = [float]
        - cloth_friction = [float]
        - damping = [float]
        - damping_factor = [float]
        - damping_random = [float]
        - friction_factor = [float]
        - friction_random = [float]
        - permeability = [float]
        - stickiness = [float]
        - thickness_inner = [float]
        - thickness_outer = [float]
        - use [= 'True'|'False']
        - use_culling = 'True'|'False']
        - use_normal = 'True'|'False']
        - use_particle_kill = 'True'|'False']

    "location" = (x,y,z) [floats]

    "rotation" = (x,y,z) [floats in degrees]

    "scale" = (x,y,z) [floats]

    "parent_index" = [Number, finds a parent's index or -1]   


### Common light parameters

    "light_type" = ['POINT'|'SUN'|'SPOT'|'AREA']

    "light_color" = (r,g,b) [floats]    

    "cutoff_distance" = [float]       

    "distance_half_intensity" = [float]

    "specular_factor" = [float]  
    
    "contact_shadow_distance" = [float]

    "contact_shadow_thickness" = [float]

    "energy" = [float]

    "falloff_type" = [‘CONSTANT’|‘INVERSE_LINEAR’|‘INVERSE_SQUARE’|‘INVERSE_COEFFICIENTS’|‘CUSTOM_CURVE’|‘LINEAR_QUADRATIC_WEIGHTED’]

    "linear_attenuation" = [float]

    "linear_coefficient" = [float]

    "quadratic_attenuation" = [float]

    "quadratic_coefficient" = [float]

    "shadow_buffer_bias" = [float]

    "shadow_buffer_clip_start" = [float]

    "shadow_buffer_samples" = [float]

    "shadow_buffer_size" = [float]    

    shadow_color = (r,g,b) [floats]  

    "shadow_soft_size" = [float]

    "use_contact_shadow" = ['True'|'False']

    "use_shadow" = ['True'|'False']

#### Point light

    -

#### Sun light

    "angle" = [float in degrees]

    "shadow_cascade_count" = [int]

    "shadow_cascade_exponent" = [float]

    "shadow_cascade_fade" = [float]

    "shadow_cascade_max_distance" = [float]

#### Spot light

    "show_cone" = ['True'|'False']

    "spot_blend" = [float]

    "spot_size" = [float]

    "use_square" = ['True'|'False']

#### Area light

    "shape" =  [‘SQUARE’|‘RECTANGLE’|‘DISK’|‘ELLIPSE’]
    
    "size" = [float]
    
    "size_y" = [float]


### Camera

    "camera_type" = scene_object.data.type

    "angle" = [float in degrees]

    "angle_x" = [float in degrees]

    "angle_y" = [float in degrees]

    "clip_end" = [float]

    "clip_start" = [float]

    "display_size" = [float]

    "lens" = [float]

    "lens_unit" =  [‘MILLIMETERS’|‘FOV’]

    "ortho_scale" = [float]

    "sensor_fit" = [‘AUTO’|‘HORIZONTAL’|‘VERTICAL’]

    "sensor_height" = [float]

    "sensor_width" = [float]

    "shift_x" = [float]

    "shift_y" = [float]

    if DOF information is present:

        "dof_aperture_blades" = [int]

        "dof_aperture_fstop" = [float]

        "dof_aperture_ratio" = [float]

        "dof_aperture_rotation" = [float in degrees]

        "dof_focus_distance" = [float]

        "dof_use_dof" = ['True'|'False']

        if a DOF focus_object is set:

            "dof_focus_object" = [focus object name as shown in Blender]


### Scene
     
    "active_camera" = [Text with name of active camera]

    scene_gravity = [3 floats, x y z]

    scene_object["use_gravity"] = = ['True'|'False']

    "session_uid" = [Integer showing a unique session ID]


### Scene Statistics

    "total_scene_objects_count" = [Number, total objects in scene. Not all may be set to be exported]
    "exported_scene_objects_count" = [Number, total exported objects in scene]
    
    if empties are exported:
        "empties_indices" = [Number array, indices of empties]
        "empties_count" = [Number, count of empties if exported]
    
    if meshes are exported:
        "meshes_indices" = [Number array, indices of meshes]
        "meshes_count" = [Number, count of meshes if exported]
    
    if lights are exported:
        "lights_indices" = [Number array, indices of lights]
        "lights_count" = [Number, count of lights if exported]
    
    if cams are exported:
        "cameras_indices" = [Number array, indices of cameras]
        "cameras_count" = [Number, count of cameras if exported]


### Exporter Information
    "name" = [Text with the exporter name]
    "version" = [Text with the exporter version, given as ##Main Number##.##Sub Number## e.g. "1.1"]


## Tested 
- Blender v4.3.2

## Versions

v1.2
- Export full name attribute for scene and all objects
- Export scene, objects id_type attribute
- Export object tag where available
- Changed boolean values from string type to booleans
- Export detailed collision settings
- Various small bugfixes

v1.1 
- Bugfixed SUN LIGHT angle radians and degrees export
- Added object base name, which is the name without anything after a first dot
- Added general radians and degrees exports to all applicable attributes, such as rotations
- Added scene statistics, arrays and object type (EMPTY, MESH, LIGHT, CAMERA) counts to indicate object type based on exported index
- Refactored exporter information and version to seperate JSON sub-object 

v1.0 
- Initial Release