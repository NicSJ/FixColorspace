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

bl_info = {
        "name": "Fix ColorSpace",
        "description": "Changes the color space of image nodes based on specific image names.",
        "author": "ChatGPT / Blender Bob / True-VFX / NicSJ",
        "version": (2, 0, 0),
        "blender": (2, 80, 0),
        "location": "View3D > Sidebar > Tool",
        "warning": "", # used for warning icon and text in addons panel
        "doc_url": "https://github.com/NicSJ/FixColorspace",
        "support": "COMMUNITY",
        "category": "Material",
        }

import bpy
from . import operators, ui
#from . import operators, preferences, interface

def register():
    operators.register()
    ui.register()
    #preferences.register()

def unregister():
    operators.unregister()
    ui.unregister()
    #preferences.unregister()
