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

scui_comp_label = "breadcrumb"


class BreadcrumbMixin:

    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "breadcrumb_root"


# Base generation pipeline wrapper
_Breadcrumb = ActiveDiv_StubWrappedTypeGen(
    "Breadcrumb",
    BreadcrumbMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_breadcrumb,
)

# Module-level component definitions
Root = CSR_comp_generator(_Breadcrumb)

List = gen_PassiveDiv_type_by_tag("List", prefix="Breadcrumb_")
Item = gen_PassiveDiv_type_by_tag("Item", prefix="Breadcrumb_")

Link = gen_PassiveDiv_type_by_tag(
    "Link", 
    prefix="Breadcrumb_", 
    addon_mixins=[HTM.AMixin], 
)

Separator = gen_PassiveDiv_type_by_tag("Separator", prefix="Breadcrumb_")
Page = gen_PassiveDiv_type_by_tag("Page", prefix="Breadcrumb_")


# 3. Module-level registry mapping using the Breadcrumb namespace container
kv_label_to_shadcn_comp_map = """
    'breadcrumb_root': Breadcrumb.Root,
    'breadcrumb_list': Breadcrumb.List,
    'breadcrumb_item': Breadcrumb.Item,
    'breadcrumb_link': Breadcrumb.Link,
    'breadcrumb_separator': Breadcrumb.Separator,
    'breadcrumb_page': Breadcrumb.Page,
"""

import_stmt = """import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
"""
