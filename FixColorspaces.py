# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Fix ColorSpace",
    "author": "ChatGPT / Blender Bob / True-VFX / NicSJ",
    "description": "Changes the color space of image nodes based on specific image names.",
    "blender": (2, 80, 0),
    "version": (1, 0, 3),
    "location": "View3D > Sidebar > Tool",
    "category": "Material",
}

import bpy
from bpy.types import Image, Operator, Panel, ShaderNodeTree

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
    'curvature', 'curv'
)


class FixColorSpaceBase:
    bl_options = {'REGISTER', 'UNDO'}

    # Must replace these with the color space names you want to use
    color_space:str
    non_color_space:str

    def set_color_space(self, image:Image):
        """Set the color space of an image based on its name."""
        image.colorspace_settings.name = self.color_space
        for keyword in KEYWORDS:
            if keyword in image.name.lower():
                image.colorspace_settings.name = self.non_color_space
                break
                
    
    def find_image_nodes(self, node_tree: ShaderNodeTree):
        """Find all image nodes in a node tree and set their color space. If a group node is found explore its node tree recursively."""
        for node in node_tree.nodes:
            if node.type == 'TEX_IMAGE' and node.image:
                self.set_color_space(node.image)
            elif node.type == 'GROUP':
                self.find_image_nodes(node.node_tree)

    def execute(self, _context):
        # Set color space for images in all materials
        for material in bpy.data.materials:
            if material.node_tree:
                self.find_image_nodes(material.node_tree)
        
        # Set color space for images in all worlds
        for world in bpy.data.worlds:
            if world.node_tree:
                self.find_image_nodes(world.node_tree)
        
        return {'FINISHED'}


class FixColorSpace_OT_Filmic(FixColorSpaceBase, Operator):
    bl_idname = "scene.apply_filmic_colorspace"
    bl_label = "Filmic"

    color_space = 'sRGB'
    non_color_space = 'Non-Color' # old 'Raw'

class FixColorSpace_OT_ACES(FixColorSpaceBase, Operator):
    bl_idname = "scene.apply_aces_colorspace"
    bl_label = "ACES"

    color_space = 'Utility - sRGB - Texture'
    non_color_space = 'Utility - Raw'

class FixColorSpace_OT_ACESTWO(FixColorSpaceBase, Operator):
    bl_idname = "scene.apply_aces_colorspace_new"
    bl_label = "ACES 2"

    color_space = 'sRGB - Texture'
    non_color_space = 'Raw'

class FixColorSpace_PT_Panel(Panel):
    bl_idname = "FIXCOLORSPACE_PT_Panel"
    bl_label = "Fix Color Space"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"  # change Tool to any custom name if you want a new tab
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        
        # Only display the relevant buttons, based on the current Color Management
        # ACES 1 config files - up to 1.3
        if bpy.context.scene.display_settings.display_device == 'ACES':
            layout.operator("scene.apply_aces_colorspace", text="To ACES")
        # ACES 2 config files - no longer need luts (OCIO 2+)
        elif bpy.context.scene.view_settings.view_transform.startswith('ACES'):
            layout.operator("scene.apply_aces_colorspace_new", text="To ACES 2")
        else:
            layout.operator("scene.apply_filmic_colorspace", text="To Filmic/AgX")

classes = (
    FixColorSpace_OT_Filmic,
    FixColorSpace_OT_ACES,
    FixColorSpace_OT_ACESTWO,
    FixColorSpace_PT_Panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

# Only needed if running from text editor. Remove if installing as an addon.
# if __name__ == "__main__":
    # register()