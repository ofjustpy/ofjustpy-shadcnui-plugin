import sys
#from svelte_bundler import list_jsvars_in_module
from svelte_bundler import publish_tailwind_svelte_safelist
target_module = "runner"
dep_modules = [
    "demo_alert",
    "demo_alertdialog",
    "demo_accordion",
    "demo_aspectratio",
    "demo_avatar",
    "demo_badge",
    "demo_breadcrumb",
    "demo_button",
    "demo_calendar",
    "demo_card",
    "demo_carousel"
    "landing_page",
    
    ]


publish_tailwind_svelte_safelist(target_module,
             dep_modules,
                                  )

