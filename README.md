# FixColorSpace
Blender addon that changes the color space of material image nodes based on specific image keywords. Designed to be used with the default color spaces or ACES. Tested with Blender 2.8 to 4.0. 

Extended from the original file posted by **Blender Bob** [Free Color space addon for Blender](https://www.youtube.com/watch?v=73Y_5LrDZQc&t=1s&ab_channel=BlenderBob)

## Conversion defaults
**Non-color image types:**
- Filmic/AgX = Non-Color  
- Aces = "Utility - Raw"

**Rest:**  
- Filmic/AgX = "sRGB"  
- Aces = "Utility - sRGB - Texture"  

## Installation
Download the latest version from the Releases section. Open Blender -> _Edit -> Preferences -> Add-ons -> Install..._
Navigate to the location of the .zip that was downoaded. Makes sure the enable checkbox is ticked. In the 3D viewport press N and select the Tool tab. Scroll down untill you find **Fix Color Space**.
