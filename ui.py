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
from bpy.types import Panel

from . import operators

# main panel that the user interacts with
class FCSFixColorSpace_PT_Panel(Panel):
    bl_idname = "FCSFIXCOLORSPACE_PT_Panel"
    bl_label = "Fix Color Space"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"  # change Tool to any custom name if you want a new tab
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # only display the relevant button, based on the current Color Management (ACES/Filmic/AgX)
        # ACES 1 config files - up to 1.3 (OCIO 1)
        if scene.display_settings.display_device == 'ACES':
            layout.operator("scene.apply_aces_colorspace", text="To ACES")
        # ACES 2 config files - no longer need luts (OCIO 2)
        elif scene.view_settings.view_transform.startswith('ACES'):
            layout.operator("scene.apply_aces_colorspace_two", text="To ACES 2")
        else:
            layout.operator("scene.apply_filmic_colorspace", text="To Filmic/AgX")


def register():
    bpy.utils.register_class(FCSFixColorSpace_PT_Panel)

def unregister():
    bpy.utils.unregister_class(FCSFixColorSpace_PT_Panel)
