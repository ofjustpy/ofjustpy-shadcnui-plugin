import macropy.activate
from svelte_safelist_builder import get_svelte_safelist

#target_module = "ofjustpy_webworks_website.skeletonui_component_library_showcase"

import sys
target_module = "runner"
dep_modules = [
    #"td_accordion"
    #"td_alertdialog",
    #"td_alert",
    #"td_avatar",
    #"td_breadcrumb",
    #"td_badge",
    #"td_button",
    #"td_cards",
    "td_chart",
    #"td_carousel"
    #"td_calender", 
    #"td_label_checkbox",
    #"td_collapsible"
    #"td_context_menu"
    #"td_dialog",
    #"td_drawer",
    #"td_dropdownmenu"
    #"td_hovercard",
    #"td_input"
    #"td_menubar"
    #"td_navigationmenu",
    #"td_pagination",
    #"td_popover",
    #"td_progress",
    #"td_radiogroup",
    #"td_resizable",
    #"td_scrollarea",
    #"td_select",
    #"td_separator",
    #"td_sheet"
    #"td_skeleton",
    #"td_slider"
    #"td_switch",
    #"td_table",
    #"td_tabs",
    #"td_textarea",
    #"td_tooltip"
]


twtags, fontawesome_icons = get_svelte_safelist(target_module)


# # which font families to include
font_families = ["Geist", "Roboto"]

from  svelte_bundler import  all_in_one_bundle_builder, list_shadcn_components_in_module, list_layerchart_components_in_module



shadcn_components, shadcn_components_parts  = list_shadcn_components_in_module(target_module, dep_modules) 

layerchart_components, all_d3_assests = list_layerchart_components_in_module(target_module, dep_modules)

#print("shadcn_components = ", shadcn_components, shadcn_components_parts)
print("layerchart_components = ", layerchart_components)
print("d3_components = ", all_d3_assests)


all_in_one_bundle_builder(twtags,

                          font_families=font_families,
                          fontawesome_icons = fontawesome_icons,
                          output_dir="static/skeleton_shadcn_uibundle",
                          shadcn_components = list(shadcn_components),
                          shadcn_components_parts = list(shadcn_components_parts),
                          layerchart_components = layerchart_components,
                          layerchart_d3_assests = all_d3_assests
                          )


