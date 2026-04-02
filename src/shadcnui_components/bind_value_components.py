
from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR
from addict_tracking_changes import Dict
from ofjustpy.htmlcomponents_impl import assign_id


class BindValueMixin:
    def __init__(self, **kwargs):
        self.has_bind_value = True
        pass
    
        
class SliderMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_bind_value_component"
        self.domDict["html_tag"] = "slider"

        for attr in ["value", "step" ]:
            if attr in kwargs:
                self.attrs[attr] = kwargs.get("attr")
        if "max_" in kwargs:
            self.attrs["max"] = kwargs.get("max_")
        

_Slider = gen_Div_type(
    HCType.active,
    "Slider",
    SliderMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_slider,
    static_addon_mixins = [BindValueMixin]  
)
Slider=assign_id(_Slider)

class CalendarMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_bind_value_component"
        self.domDict.html_tag = "calendar"

        

Calendar = gen_Div_type(
        HCType.active,
        "Calendar",
        CalendarMixin,
        static_addon_mixins = [BindValueMixin] ,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_calendar,
        )
Calendar = assign_id(Calendar)


class RangeCalendarMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_bind_value_component"
        self.domDict.html_tag = "range-calendar"

        

_RangeCalendar = gen_Div_type(
        HCType.active,
     "RangeCalendar",
    RangeCalendarMixin,
        static_addon_mixins = [BindValueMixin] ,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_range_calendar,
        )
RangeCalendar = assign_id(_RangeCalendar)


