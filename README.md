# FixColorSpace
Blender addon that changes the color space of material image nodes based on specific image keywords. Designed to be used with the default color spaces or ACES. Tested with Blender 2.8 to 4.0. Compatible with ACES config files for [OCIO v1](https://github.com/colour-science/OpenColorIO-Configs/tree/feature/aces-1.2-config) or [OCIO v2](https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES). 

Extended from the original file posted by **Blender Bob** [Free Color space addon for Blender](https://www.youtube.com/watch?v=73Y_5LrDZQc&t=1s&ab_channel=BlenderBob)

## Conversion defaults
**Non-color image types:**
- Filmic/AgX = Non-Color  
- Aces = "Utility - Raw"
- Aces2 = "Raw"

**Color images:**  
- Filmic/AgX = "sRGB"  
- Aces = "Utility - sRGB - Texture"
- Aces2 = "sRGB - Texture"  

## Installation
Download the latest version from the Releases section. Open Blender -> _Edit -> Preferences -> Add-ons -> Install..._
Navigate to the location of the .zip that was downoaded. Makes sure the enable checkbox is ticked. In the 3D viewport press N and select the Tool tab. Scroll down untill you find **Fix Color Space**. Alternatively, you can find the Tool tab in the Properties panel (above the Render tab).

![Addon in side panel](/resources/SidePanel.png)
![Addon in properties panel](/resources/PropertiesPanel.png)
