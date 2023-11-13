# FixColorSpace
Blender addon that changes the color space of material image nodes based on specific image keywords. Designed to be used with the default color spaces or ACES. Compatible with ACES config files for [OCIO v1](https://github.com/colour-science/OpenColorIO-Configs/tree/feature/aces-1.2-config) or [OCIO v2](https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES). **Not** tested with custom config files, e.g. Blender default merged with an Aces v1 file. Tested with Blender 2.8 to 4.0. 

Extended from the original file posted by **Blender Bob** [Free Color space addon for Blender](https://www.youtube.com/watch?v=73Y_5LrDZQc&t=1s&ab_channel=BlenderBob)

## Conversion defaults
  
|  | Color Images | Non-Color Images | Environment Images |
| :---|  :---:  |  :---:  |  :---:  |
| Filmic/AgX | sRGB | Non-Color | Linear (Blender <= 3.6) / Linear Rec.709 (Blender 4.0+) |
| ACES (OCIO v1) | Utility - sRGB - Texture | Utility - Raw | Utility - Linear - Rec.709 |
| ACES 2 (OCIO v2) | sRGB - Texture | Raw | Linear Rec.709 (sRGB) |

## Installation
Download the latest version from the Releases section. Open Blender -> _Edit -> Preferences -> Add-ons -> Install..._
Navigate to the location of the .zip that was downoaded. Makes sure the enable checkbox is ticked. In the 3D viewport press N and select the Tool tab. Scroll down untill you find **Fix Color Space**. Alternatively, you can find the Tool tab in the Properties panel (above the Render tab).

![Addon in side panel](/resources/SidePanel.png)
![Addon in properties panel](/resources/PropertiesPanel.png)

## FAQ
**Q: Why do I only see this button:**
![](/resources/To%20Filmic.png)  
  
A: The addon automatically checks the properties panel -> Render -> Color Management -> Display Device (Aces config v1 - will only display "ACES")  
![](/resources/Aces1.png) ![](/resources/To%20Aces.png)  
  
or View Transform (Aces config v2 - will have a list of 4 names, 2 starting with "ACES 1.0")  
![](/resources/Aces2.png) ![](/resources/To%20Aces2.png)  

If you don't see either of these options, you are most likely using default Blender and won't see the Aces buttons.  

**Q: How do I get the Aces options to show up?**  

A: One option would be to start Blender with a OCIO config file. The following will work on for Windows. Create a text file and name it anything you like. Paste one of the following examples into the file and change the paths to the appropriate locations. Change the file extension from .txt to .bat. Double-click the batch file when you need to run Blender in Aces mode.

```
REM ACES v1
set OCIO=C:\OpenColorIO-Configs\aces_1.2\config.ocio
start "BLENDER 4.0" "C:\BlenderBuilds\bl_symlink\blender.exe"
```

```
REM ACES v2
set "OCIO=G:\OpenColorIO-Configs\aces_2\v2\studio-config-v2.0.0_aces-v1.3_ocio-v2.2.ocio"
start "BLENDER 4.0" "C:\BlenderBuilds\bl_symlink\blender.exe"
```

**Q: Why is the color space of the image texture not converting correctly?**  

A: The addon looks for the following keywords in the image file name:  
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

If a keyword is found, the color space will be changed to a raw/non-color variant. If none are found, the color space will be changed to a variant of sRGB. For variations, refer to Conversion defaults above. Textures from sites such as [Polyhaven](https://polyhaven.com/), or generated with Substance 3D Painter, have the keywords in the file names and should work as expected. If you are naming files manually, be sure to add the appropriate keyword to the file. E.g. Bronze_damaged_normal.png

  
