import macropy.activate
import kavya as kv
kv.set_style("un")
from py_tailwind_utils import *
from demo_accordion import accordion_box
#from demo_alertdialog import alertdialog_box
#from demo_alert import alert_box
#from demo_aspectratio import aspectratio_box
#from demo_aspectratio import aspectratio_box
#from demo_avatar import avatar_box
#from demo_badge import badge_box
#from demo_breadcrumb import breadcrumb_box
#from demo_button import button_box
#from demo_calendar import calendar_box

#from demo_card import card_box
#from demo_carousel import carousel_box
#from demo_context_menu import context_menu_box
#from demo_dialog import dialog_box
#from demo_drawer import drawer_box
#from demo_dropdown_menu import dropdown_menu_box
#from demo_tabs import tabs_box
#from demo_table import table_box
#from demo_rangecalendar import range_calendar_box
app = kv.load_app()
# centered_box = oj.PD.Valign(oj.PD.Halign(#carousel_box,
#     #context_menu_box,
#     #dialog_box,
#     #drawer_box,
#     #dropdown_menu_box,
#     #tabs_box,
#     #table_box,
#     range_calendar_box,
    
#     twsty_tags=[W/screen]
# ), twsty_tags=[H/screen]
#                             )

wp_endpoint = kv.create_endpoint(key="components_showcase",
                                 childs = [                                           
                                     accordion_box
                                     #alertdialog_box
                                     #alert_box
                                     #aspectratio_box
                                     #avatar_box
                                     #badge_box
                                     #breadcrumb_box
                                     #button_box
                                     #calendar_box
                                     #card_box
                                     #carousel_box
                                     #centered_box
                                     
 ],
                                 
                                 title="Components Showcase",
                                 svelte_bundle_dir="svelte_bundle",
                                 )
kv.add_route("/", wp_endpoint)
                
