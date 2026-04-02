import kavya as kv
import shadcnui_components as SCUI
from kavya.dsl import macros, MuCtx

kv.set_style("un")

alert = kv.AD.SCUI.divactive.Alert(key="alert_1")
alert.Title(childs = [kv.PC.Span(text="Heads up!")])
alert.Description(childs = [kv.PC.Span(text="You can add components to your app using the cli.")

                            ]
                            
                  )
