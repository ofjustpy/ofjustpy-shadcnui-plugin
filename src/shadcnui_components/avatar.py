from kavya.themes import ui_styles
from kavya.type_factory.static_type_factory import (
    ActiveDiv_StubWrappedTypeGen,
    PassiveDiv_StubWrappedTypeGen,
)
from .shadcn_type_factory import (
    CSR_comp_generator,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
)
from kavya.htmlcomponents import html_tag_mixins as HTM
from kavya.type_factory.common_mixins import HCTextMixin

scui_comp_label = "avatar"


class AvatarMixin:

    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "avatar_root"


# Base generation pipeline wrapper
_Avatar = ActiveDiv_StubWrappedTypeGen(
    "Avatar",
    AvatarMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_avatar,
)

# Module-level component definitions
Root = CSR_comp_generator(_Avatar)

Image = gen_PassiveDiv_type_by_tag(
    "Image", 
    prefix="Avatar_", 
    addon_mixins=[HTM.ImgMixin], 
)

Fallback = gen_PassiveDiv_type_by_tag(
    "Fallback", 
    prefix="Avatar_", 

)


# 3. Module-level registry mapping using the Avatar namespace container
kv_label_to_shadcn_comp_map = """
    'avatar_root': Avatar.Root,
    'avatar_image': Avatar.Image,
    'avatar_fallback': Avatar.Fallback,
"""
import_stmt = """import * as Avatar from "$lib/components/ui/alert-dialog/index.js";
"""
