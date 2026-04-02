import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *


oj.set_style("un")

# Python equivalent for the HTML snippet with Badge
with writer_ctx:
    with oj.PD.Div(classes="flex flex-col items-center gap-2") as badge_box:
        with oj.PD.Div(classes="flex w-full flex-wrap gap-2"):
            with SCUI.Badge():
                with oj.PD.Prose(text="Badge"):
                    pass
            with SCUI.Badge(variant="secondary"):
                with oj.PD.Prose(text="Secondary"):
                    pass
            with SCUI.Badge(variant="destructive"):
                with oj.PD.Prose(text="Destructive"):
                    pass
            with SCUI.Badge(variant="outline"):
                with oj.PD.Prose(text="Outline"):
                    pass
        with oj.PD.Div(classes="flex w-full flex-wrap gap-2"):
            with SCUI.Badge(variant="secondary", classes="bg-blue-500 text-white dark:bg-blue-600"):
                # BadgeCheckIcon would be handled by an icon component if available,
                # here we just include the text.
                with oj.PD.Prose(text="Verified"):
                    pass
            with SCUI.Badge(classes="h-5 min-w-5 rounded-full px-1 font-mono "): #tabular-nums
                with oj.PD.Prose(text="8"):
                    pass
            with SCUI.Badge(variant="destructive", classes="h-5 min-w-5 rounded-full px-1 font-mono "): #tabular-nums
                with oj.PD.Prose(text="99"):
                    pass
            with SCUI.Badge(variant="outline", classes="h-5 min-w-5 rounded-full px-1 font-mono "): #tabular-nums
                with oj.PD.Prose(text="20+"):
                    pass
