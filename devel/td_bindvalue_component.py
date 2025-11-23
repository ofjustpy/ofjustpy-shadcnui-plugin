import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from shadcnui_components.bind_value_components import Slider
from py_tailwind_utils import *
oj.set_style("un")

slider_box = SCUI.Slider(key="slider",
                         extra_classes="w-[400px]", value=50,
                         
                         max_=100,
                         step=1)

def valuechange_eh(dbref, msg, to_ms):
    print("yey we are at valuechange: ", msg.value)
    pass
calendar_box = SCUI.Calendar(key="cal1", on_change=valuechange_eh,
              value=oj.JSExpr("today(getLocalTimeZone())",
                                                           import_stmts = [""" import { getLocalTimeZone, today } from "@internationalized/date";"""]
                                                           ),
         
              )

centered_box = oj.PD.Valign(oj.PD.Halign(oj.PD.StackV(childs=[slider_box,
                                                              calendar_box
                                                              ]
                                                      ),
                                         twsty_tags= [W/full]),
                            twsty_tags=[twmin/H/screen])

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Slider",
                                 childs = [
                                     centered_box
                                           ],
                                 
                                 title="Slider",
                                 csr_bundle_dir="svelte_bundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
