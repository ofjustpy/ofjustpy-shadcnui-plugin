from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR
from addict_tracking_changes import Dict
from ofjustpy.htmlcomponents_impl import assign_id


class SliderMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "slider"
        for attr in ["value", "step" ]:
            if attr in kwargs:
                self.attrs[attr] = kwargs.get("value")
        if "max_" in kwargs:
            self.attrs["max"] = kwargs.get("max_")
        

Slider = assign_id(gen_Div_type(
    HCType.active,
    "Slider",
    SliderMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_slider,
))
