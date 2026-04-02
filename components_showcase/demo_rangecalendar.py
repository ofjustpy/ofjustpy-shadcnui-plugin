import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
import jsexprs.macro_module as mm
from jsexprs.macro_module import macros, writer_ctx as jsexpr_writer_ctx
oj.set_style("un")

def valuechange_eh(dbref, msg, to_ms):
    print("yey we are at valuechange: ", msg.value)
    pass

# Python equivalent for the HTML snippet
with writer_ctx:
    with SCUI.RangeCalendar(key="cal1",
                            value=oj.JSExpr("{   start: new CalendarDate(2025, 2, 10),   end:new CalendarDate(2025, 2, 17)    }",
                                            import_stmts = [""" import { CalendarDate } from '@internationalized/date';"""]
                                                           ),
                            
                            # value=oj.JSExpr("(() => { const start = today(getLocalTimeZone()); return { start, end: start.add({ days: 7 }) } })()",
                            #                 import_stmts = [""" import { getLocalTimeZone, today } from "@internationalized/date";"""]
                            #                                ),
                            on_change=valuechange_eh) as range_calendar_box:
        pass
