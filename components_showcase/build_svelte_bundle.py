import sys
#from svelte_bundler import list_jsvars_in_module
from svelte_bundler import build_bundle
target_module = "runner"
dep_modules = [
    # "demo_alert",
    # "demo_alertdialog",
    # "demo_accordion",
    # "demo_aspectratio",
    # "demo_avatar",
    # "demo_badge",
    # "demo_breadcrumb",
    # "demo_button",
    # "demo_calendar",
    # "demo_card",
    # "demo_carousel",
    # "demo_context_menu",
    # "demo_dialog",
    # "demo_drawer",
    # "demo_dropdown_menu",
    #"demo_tabs",
    #"demo_table",
    "demo_rangecalendar",
    "landing_page",
    
    ]


build_bundle(target_module,
             dep_modules,
             output_dir="static/svelte_bundle")

