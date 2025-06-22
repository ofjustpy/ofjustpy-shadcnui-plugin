import macropy.activate
from svelte_safelist_builder import get_svelte_safelist

#target_module = "ofjustpy_webworks_website.skeletonui_component_library_showcase"

import sys
target_module = "runner"
dep_modules = [
    #"td_alertdialog",
    #"td_alert",
    #"td_avatar",
    #"td_breadcrumb",
    #"td_badge",
    #"td_button",
    #"td_cards",
    "td_carousel"
    
]


twtags, fontawesome_icons = get_svelte_safelist(target_module)


# # which font families to include
font_families = ["Geist", "Roboto"]

from  svelte_bundler import  all_in_one_bundle_builder, list_shadcn_components_in_module


shadcn_components, shadcn_components_parts  = list_shadcn_components_in_module(target_module, dep_modules) 

print("shadcn_components = ", shadcn_components, shadcn_components_parts)
all_in_one_bundle_builder(twtags,

                          font_families=font_families,
                          fontawesome_icons = fontawesome_icons,
                          output_dir="static/skeleton_shadcn_uibundle",
                          shadcn_components = list(shadcn_components),
                          shadcn_components_parts = list(shadcn_components_parts)
                          )


