import bpy
import bpy.types

import json
import math 

def to_degrees(radians):
    return radians * 180.0 / math.pi

def find_object_index(object):
    find_index = -1

    scene = bpy.context.scene
    index = 0
    for scene_object in scene.objects: 
        if scene_object == object:
            find_index = index
            break

        index += 1
        
    return find_index

def write_json_object(f, empties, meshes, lights, light_details, cams, cam_details):
    scene = bpy.context.scene

    json_object =  {}
    
    # info
    exporter_object = {}

    exporter_object["name"]= "MKS Blender JSON Exporter"
    exporter_object["version"]= "1.2"

    json_object["exporter"] = exporter_object

    # scene
    scene_object = {}

    scene_object["active_camera"]= scene.camera.name

    scene_gravity_object = {}
    scene_gravity_object["x"] = scene.gravity.x
    scene_gravity_object["y"] = scene.gravity.y
    scene_gravity_object["z"] = scene.gravity.z
    scene_object["gravity"]= scene_gravity_object

    scene_object["use_gravity"] = str(scene.use_gravity) 
    
    # first save
    json_object["scene"] = scene_object

    # objects
    index = 0
    exported_count = 0
    
    empties_array = []
    meshes_array = []
    lights_array = []
    cameras_array = []
    
    for scene_object in scene.objects: 
        
        if scene_object.type != 'EMPTY' and scene_object.type != 'MESH' and scene_object.type != 'LIGHT' and scene_object.type != 'CAMERA':
            index += 1
            continue
        
        if scene_object.type == 'EMPTY' and not empties:
            index += 1
            continue

        if scene_object.type == 'MESH' and not meshes:
            index += 1
            continue
        
        if scene_object.type == 'LIGHT' and not lights:
            index += 1
            continue

        if scene_object.type == 'CAMERA' and not cams:
            index += 1
            continue
                
        # common attributes
        json_sub_object = {}
        
        json_sub_object["name"] = scene_object.name
        json_sub_object["full_name"] = scene_object.name_full
        
        split_name = scene_object.name.split(".")
        if len(split_name) >= 1:
            json_sub_object["base_name"] = split_name[0]
        
        json_sub_object["type"] = scene_object.type
        
        # write to arrays
        if scene_object.type == 'EMPTY':
            empties_array.append(index)
        elif scene_object.type == 'MESH':
            meshes_array.append(index)
        elif scene_object.type == 'LIGHT':
            lights_array.append(index)
        elif scene_object.type == 'CAMERA':
            cameras_array.append(index)
        
        json_sub_object["scene_index"] = index

        json_sub_object["visibility"] = str(not scene_object.hide_render)
        
        json_sub_object["collider"] = "False"     
        if scene_object.collision:
            json_sub_object["collider"] = str(scene_object.collision.use)
        
        location = {}
        location["x"] = scene_object.location.x
        location["y"] = scene_object.location.y
        location["z"] = scene_object.location.z
        json_sub_object["location"] = location
 
        rotation_radians = {}
        rotation_radians["x"] = scene_object.rotation_euler.x
        rotation_radians["y"] = scene_object.rotation_euler.y
        rotation_radians["z"] = scene_object.rotation_euler.z      
        json_sub_object["rotation_radians"] = rotation_radians
        
        rotation_degrees = {}
        rotation_degrees["x"] = to_degrees(scene_object.rotation_euler.x)
        rotation_degrees["y"] = to_degrees(scene_object.rotation_euler.y)
        rotation_degrees["z"] = to_degrees(scene_object.rotation_euler.z)      
        json_sub_object["rotation_degrees"] = rotation_degrees
        
        scale = {}
        scale["x"] = scene_object.scale.x
        scale["y"] = scene_object.scale.y
        scale["z"] = scene_object.scale.z
        json_sub_object["scale"] = scale
       
        # parent scene index
        parent_index = find_object_index(scene_object.parent)     
        json_sub_object["parent_index"] = parent_index
        
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # custom properties if available
        #properties = scene_object.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        # light details
        if scene_object.type == 'LIGHT' and light_details:
            json_sub_object["light_type"] = scene_object.data.type
       
            light_color = {}
            light_color["r"] = scene_object.data.color[0]
            light_color["g"] = scene_object.data.color[1]
            light_color["b"] = scene_object.data.color[2]
            json_sub_object["light_color"] = light_color
        
            json_sub_object["cutoff_distance"] = scene_object.data.cutoff_distance
            
            json_sub_object["distance_half_intensity"] = scene_object.data.distance
            
            json_sub_object["specular_factor"] = scene_object.data.specular_factor
   
            json_sub_object["constant_coefficient"] = scene_object.data.constant_coefficient
            json_sub_object["contact_shadow_bias"] = scene_object.data.contact_shadow_bias
            json_sub_object["contact_shadow_distance"] = scene_object.data.contact_shadow_distance
            json_sub_object["contact_shadow_thickness"] = scene_object.data.constant_coefficient
            json_sub_object["energy"] = scene_object.data.energy
            json_sub_object["falloff_type"] = scene_object.data.falloff_type
            json_sub_object["linear_attenuation"] = scene_object.data.linear_attenuation
            json_sub_object["linear_coefficient"] = scene_object.data.linear_coefficient
            json_sub_object["quadratic_attenuation"] = scene_object.data.quadratic_attenuation
            json_sub_object["quadratic_coefficient"] = scene_object.data.quadratic_coefficient
            json_sub_object["shadow_buffer_bias"] = scene_object.data.shadow_buffer_bias
            json_sub_object["shadow_buffer_clip_start"] = scene_object.data.shadow_buffer_clip_start
            json_sub_object["shadow_buffer_samples"] = scene_object.data.shadow_buffer_samples
            json_sub_object["shadow_buffer_size"] = scene_object.data.shadow_buffer_size
                        
            shadow_color = {}
            shadow_color["r"] = scene_object.data.shadow_color[0]
            shadow_color["g"] = scene_object.data.shadow_color[1]
            shadow_color["b"] = scene_object.data.shadow_color[2]
            json_sub_object["shadow_color"] = shadow_color
            
            json_sub_object["shadow_soft_size"] = scene_object.data.shadow_soft_size
            json_sub_object["use_contact_shadow"] = str(scene_object.data.use_contact_shadow)
            json_sub_object["use_shadow"] = str(scene_object.data.use_shadow)
        
            if scene_object.data.type == 'POINT':
                pass

            elif scene_object.data.type == 'SUN':
                json_sub_object["angle_radians"] = scene_object.data.angle
                json_sub_object["angle_degrees"] = to_degrees(scene_object.data.angle)

                json_sub_object["shadow_cascade_count"] = scene_object.data.shadow_cascade_count
                json_sub_object["shadow_cascade_exponent"] = scene_object.data.shadow_cascade_exponent
                json_sub_object["shadow_cascade_fade"] = scene_object.data. shadow_cascade_fade
                json_sub_object["shadow_cascade_max_distance"] = scene_object.data.shadow_cascade_max_distance
                
            elif scene_object.data.type == 'SPOT':
                json_sub_object["show_cone"] = str(scene_object.data.show_cone)
                json_sub_object["spot_blend"] = scene_object.data.spot_blend
                json_sub_object["spot_size"] = scene_object.data.spot_size
                json_sub_object["use_square"] = str(scene_object.data.use_square)

            elif scene_object.data.type == 'AREA':
                json_sub_object["shape"] = scene_object.data.shape
                json_sub_object["size"] = scene_object.data.size
                json_sub_object["size_y"] = scene_object.data.size_y

        # camera details           
        elif scene_object.type == 'CAMERA' and cam_details:
            json_sub_object["camera_type"] = scene_object.data.type

            json_sub_object["angle_radians"] = scene_object.data.angle
            json_sub_object["angle_degrees"] = to_degrees(scene_object.data.angle)
            json_sub_object["angle_x_radians"] = scene_object.data. angle_x
            json_sub_object["angle_x_degrees"] = to_degrees(scene_object.data. angle_x)
            json_sub_object["angle_y_radians"] = scene_object.data. angle_y
            json_sub_object["angle_y_degrees"] = to_degrees(scene_object.data. angle_y)

            json_sub_object["clip_end"] = scene_object.data.clip_end
            json_sub_object["clip_start"] = scene_object.data.clip_start
            json_sub_object["display_size"] = scene_object.data.display_size
            if scene_object.data.dof:
                json_sub_object["dof_aperture_blades"] = scene_object.data.dof.aperture_blades
                json_sub_object["dof_aperture_fstop"] = scene_object.data.dof.aperture_fstop
                json_sub_object["dof_aperture_ratio"] = scene_object.data.dof.aperture_ratio
                json_sub_object["dof_aperture_rotation"] = to_degrees(scene_object.data.dof.aperture_rotation)    
                json_sub_object["dof_focus_distance"] = scene_object.data.dof.focus_distance
                if scene_object.data.dof.focus_object:
                    json_sub_object["dof_focus_object"] = scene_object.data.dof.focus_object.name
                json_sub_object["dof_use_dof"] = str(scene_object.data.dof.use_dof)
            json_sub_object["lens"] = scene_object.data.lens
            json_sub_object["lens_unit"] = scene_object.data.lens_unit
            json_sub_object["ortho_scale"] = scene_object.data.ortho_scale
            json_sub_object["sensor_fit"] = scene_object.data.sensor_fit
            json_sub_object["sensor_height"] = scene_object.data.sensor_height
            json_sub_object["sensor_width"] = scene_object.data.sensor_width
            json_sub_object["shift_x"] = scene_object.data.shift_x
            json_sub_object["shift_y"] = scene_object.data.shift_y

        # scene id to json object mapping 
        json_object[str(index)] = json_sub_object
        
        index += 1
        exported_count += 1
    
    scene_statistics = {}
    scene_statistics["total_scene_objects_count"]= len(scene.objects)
    scene_statistics["exported_scene_objects_count"]= exported_count
    
    if empties:
        scene_statistics["empties_indices"]= empties_array
        scene_statistics["empties_count"]= len(empties_array)
    
    if meshes:
        scene_statistics["meshes_indices"]= meshes_array
        scene_statistics["meshes_count"]= len(meshes_array)
    
    if lights:
        scene_statistics["lights_indices"]= lights_array
        scene_statistics["lights_count"]= len(lights_array)
    
    if cams:
        scene_statistics["cameras_indices"]= cameras_array
        scene_statistics["cameras_count"]= len(cameras_array)
    
    json_object["scene_statistics"] = scene_statistics

    f.write(json.dumps(json_object, indent=2))
    f.write("\n")
    
def write_some_data(context, filepath, empties, meshes, lights, light_details, cameras, camera_details):
    print("running MKS JSON Scene export...")
    f = open(filepath, 'w', encoding='utf-8')

    write_json_object(f, empties, meshes, lights, light_details, cameras, camera_details)

    f.close()

    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportJSONScene(Operator, ExportHelper):
    """MKS Blender JSON Scene Hierarchy Exporter"""
    bl_idname = "export.json_scene"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export JSON Scene"

    # ExportHelper mixin class uses this
    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    empties_setting: BoolProperty(
        name="Export Empties",
        description="Export empty attributes",
        default=True,
    )
    
    meshes_setting: BoolProperty(
        name="Export Meshes",
        description="Export mesh attributes",
        default=True,
    )
    
    lights_setting: BoolProperty(
        name="Export Lights",
        description="Export light attributes",
        default=True,
    )

    light_details_setting: BoolProperty(
        name="Export Light Details",
        description="Export light details",
        default=False,
    )
    
    cameras_setting: BoolProperty(
        name="Export Cameras",
        description="Export camera attributes",
        default=True,
    )

    camera_details_setting: BoolProperty(
        name="Export Camera Details",
        description="Export camera details",
        default=False,
    )

    def execute(self, context):
        return write_some_data(context, self.filepath, 
            self.empties_setting,
            self.meshes_setting,
            self.lights_setting,
            self.light_details_setting,
            self.cameras_setting,
            self.camera_details_setting)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="MKS JSON Scene Export")


def register():
    bpy.utils.register_class(ExportJSONScene)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportJSONScene)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.export.json_scene('INVOKE_DEFAULT')
