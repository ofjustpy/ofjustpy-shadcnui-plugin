import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
import jsexprs.macro_module as mm
from jsexprs.macro_module import macros, writer_ctx as jsexpr_writer_ctx
oj.set_style("un")

with jsexpr_writer_ctx:
    with ImportVar(module="@internationalized/date", var_label="getLocalTimeZone"):
        pass

    with ImportVar(module="@internationalized/date", var_label="today") as today_var:
        pass

    with SetValueVar():
        with Runes():
            with FuncInvoke(method=today_var):
                with Args():
                    with FuncInvoke(method=getLocalTimeZone_var):
                        with Args():
                            pass
                        pass
                    pass
                pass
            pass
        pass
    
                
                
Calender_SCT= DeriveShadcnComponent()    
def valuechange_eh(dbref, msg, to_ms):
    print("yey we are at valuechange: ", msg.value)
    pass

# Python equivalent for the HTML snippet
with writer_ctx:
    with SCUI.Calendar(key="cal1", on_change=valuechange_eh) as calendar_box:
        pass
