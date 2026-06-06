from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
    BindValueMixin
)
from kavya.themes import ui_styles

scui_comp_label = "calendar"
vue_type = "shadcnui_bindvalue_component"

class CalendarMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_bindvalue_component"
        self.domDict.html_tag = "calendar"

        # Capture custom structural primitive properties if specified
        if "captionLayout" in kwargs:
            self.attrs["captionLayout"] = kwargs.get("captionLayout")


# Base generation pipeline wrapper using ActiveDiv for active input bindings
_Calendar = ActiveDiv_StubWrappedTypeGen(
    "Calendar",
    CalendarMixin,
    addon_mixins=[BindValueMixin],
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_calendar,
)

Root = CSR_comp_generator(_Calendar)


import_stmt = """import { Calendar } from "$lib/components/ui/calendar/index.js";
"""

# Module-level registry mapping (Flat component style layout)
kv_label_to_shadcn_comp_map = """
    'calendar': Calendar,
"""
