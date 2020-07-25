# MKS Blender Scene Definition Exporter (JSON)

This script exports the hierarchical scene definition in a JSON format for parsing in other applications and tools.


by Micah Koleoso Software, 2020

[www.micahkoleoso.de](http://www.micahkoleoso.de)



For bug reports, fixes, change or feature requests, please email [contact@micahkoleoso.de](mailto:contact@micahkoleoso.de)

but please add "Blender JSON Exporter" in the header to speed up me reading the mail.



## OBJECTS OUTPUT DATA:

### Common Empty|Mesh|Light|Camera parameters

    "name" = [Text with name as shown in Blender]

    "type" = ['EMPTY'|'MESH'|'LIGHT'|'CAMERA']

    "visibility" = ['True'|'False']

    "collider" = ['True'|'False']

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


## Tested on Blender v2.83.2/3 LTS