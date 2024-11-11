# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Image, Operator, ShaderNodeTree

try:
	import PyOpenColorIO as OCIO
except ImportError:
	print('Blender 3.5 or newer is required when working with OCIO v2')

# keywords orded for readability
KEYWORDS = (
    'displacement', 'displace', 'disp', 'dsp', 'heightmap', 'height',
    'glossiness', 'glossy', 'gloss',
    'normal', 'norm', 'nor', 'nrml', 'nrm',
    'normalbump', 'bump', 'bmp',
    'specularity', 'specular', 'spec', 'spc',
    'roughness', 'rough', 'rgh',
    'metalness', 'metallic', 'metal', 'mtl',
    'ao', 'ambient', 'occlusion',
    'sss', 'subsurface',
    'transparency', 'opacity', 'alpha',
    'transmission', 'thickness',
    'curvature', 'curv',
    '_arm_', '_orm_'
)

# main class
class FCSFixColorSpace:
    bl_options = {'REGISTER', 'UNDO'}

    # replace these with the color space names you want to use
    col_color_space:str
    env_color_space:str

    # assign color space based on image texture name
    def set_color_space(self, image:Image):
        """Set the color space of an image based on its name."""
        image.colorspace_settings.name = self.col_color_space
        for keyword in KEYWORDS:
            if keyword in image.name.lower():
                image.colorspace_settings.is_data = True
                break
                   
    # recursively search for image textures
    def find_image_nodes(self, node_tree: ShaderNodeTree):
        """Find all image nodes in a node tree and set their color space. If a group node is found explore its node tree recursively."""
        for node in node_tree.nodes:
            if node.type == 'TEX_IMAGE' and node.image:
                self.set_color_space(node.image)
            elif node.type == 'TEX_ENVIRONMENT':
                node.image.colorspace_settings.name = self.env_color_space
            elif node.type == 'GROUP':
                self.find_image_nodes(node.node_tree)

    def execute(self, _context):
        # set color space for images in all materials
        for material in bpy.data.materials:
            if material.node_tree:
                self.find_image_nodes(material.node_tree)
        
        # set color space for images in all worlds
        for world in bpy.data.worlds:
            if world.node_tree:
                self.find_image_nodes(world.node_tree)
        
        return {'FINISHED'}
        
# button functionality for defualt color spaces
class FCSFixColorSpace_OT_Filmic(FCSFixColorSpace, Operator):
    bl_idname = "scene.apply_filmic_colorspace"
    bl_label = "Filmic"

    col_color_space = 'sRGB'
    if bpy.app.version_string.split('.')[0] < '4':
        env_color_space = 'Linear'
    else:
        env_color_space = 'Linear Rec.709'

# button functionality for OCIO v1 ACES config
class FCSFixColorSpace_OT_ACES(FCSFixColorSpace, Operator):
    bl_idname = "scene.apply_aces_colorspace"
    bl_label = "ACES"

    col_color_space = 'Utility - sRGB - Texture'
    env_color_space = 'Utility - Linear - Rec.709'

# button functionality for OCIO v2 ACES config
class FCSFixColorSpace_OT_ACESTWO(FCSFixColorSpace, Operator):
    bl_idname = "scene.apply_aces_colorspace_two"
    bl_label = "ACES 2"

    # auto select the correct color space for sRGB files
    try:
        ocio_config = OCIO.GetCurrentConfig()
    except:
        print('Unable to load ICIO config file')
    else:
        col_color_space = ocio_config.getColorSpace(OCIO.ROLE_COLOR_PICKING).getName()
        env_color_space = 'Linear Rec.709 (sRGB)'


classes = (
    FCSFixColorSpace_OT_Filmic,
    FCSFixColorSpace_OT_ACES,
    FCSFixColorSpace_OT_ACESTWO,
)

def register():
    #Scene.my_property = BoolProperty(default=True)
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #del Scene.my_property
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
