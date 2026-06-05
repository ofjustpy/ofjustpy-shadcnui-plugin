from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.themes import ui_styles

vue_type = "shadcnui_component"
scui_comp_label = "context-menu"


class ContextMenuMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "contextmenu_root"


# Base generation pipeline wrapper
_ContextMenu = ActiveDiv_StubWrappedTypeGen(
    "ContextMenu",
    ContextMenuMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_contextmenu_root,
)

# Module-level component definitions
Root = CSR_comp_generator(_ContextMenu)

Trigger = gen_PassiveDiv_type_by_tag("Trigger", prefix="ContextMenu_")
Content = gen_PassiveDiv_type_by_tag("Content", prefix="ContextMenu_")
Sub = gen_PassiveDiv_type_by_tag("Sub", prefix="ContextMenu_")
SubTrigger = gen_PassiveDiv_type_by_tag("SubTrigger", prefix="ContextMenu_")
SubContent = gen_PassiveDiv_type_by_tag("SubContent", prefix="ContextMenu_")
Separator = gen_PassiveDiv_type_by_tag("Separator", prefix="ContextMenu_")
Group = gen_PassiveDiv_type_by_tag("Group", prefix="ContextMenu_")
Shortcut = gen_PassiveDiv_type_by_tag("Shortcut", prefix="ContextMenu_")

# Sub-component mixins to catch custom primitive attributes
class ContextMenuItemMixin:

    def __init__(self, **kwargs):
        if "inset" in kwargs:
            self.attrs["inset"] = kwargs.get("inset")
        if "disabled" in kwargs:
            self.attrs["disabled"] = kwargs.get("disabled")


class ContextMenuCheckboxItemMixin:

    def __init__(self, **kwargs):
        if "checked" in kwargs:
            self.attrs["checked"] = kwargs.get("checked")


class ContextMenuRadioGroupMixin:

    def __init__(self, **kwargs):
        if "value" in kwargs:
            self.attrs["value"] = kwargs.get("value")


class ContextMenuRadioItemMixin:

    def __init__(self, **kwargs):
        if "value" in kwargs:
            self.attrs["value"] = kwargs.get("value")


class ContextMenuGroupHeadingMixin:

    def __init__(self, **kwargs):
        if "inset" in kwargs:
            self.attrs["inset"] = kwargs.get("inset")


# Specialized Sub-Components using Mixins
Item = gen_PassiveDiv_type_by_tag("Item",
                                  prefix="ContextMenu_",
                                  addon_mixins=[ContextMenuItemMixin]
                                  )
CheckboxItem = gen_PassiveDiv_type_by_tag("CheckboxItem",
                                          prefix="ContextMenu_",
                                          addon_mixins=[ContextMenuCheckboxItemMixin],
                                          )
RadioGroup = gen_PassiveDiv_type_by_tag("RadioGroup",
                                        prefix="ContextMenu_",
                                        addon_mixins=[ContextMenuRadioGroupMixin],
                                        )
RadioItem = gen_PassiveDiv_type_by_tag("RadioItem",
                                       prefix="ContextMenu_",
                                       addon_mixins=[ContextMenuRadioItemMixin],
                                       )
GroupHeading = gen_PassiveDiv_type_by_tag("GroupHeading",
                                          prefix="ContextMenu_",
                                          addon_mixins=[ContextMenuGroupHeadingMixin],
                                          )




import_stmt = """import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
"""

# Module-level registry mapping
kv_label_to_shadcn_comp_map = """
    'contextmenu_root': ContextMenu.Root,
    'contextmenu_trigger': ContextMenu.Trigger,
    'contextmenu_content': ContextMenu.Content,
    'contextmenu_item': ContextMenu.Item,
    'contextmenu_sub': ContextMenu.Sub,
    'contextmenu_subtrigger': ContextMenu.SubTrigger,
    'contextmenu_subcontent': ContextMenu.SubContent,
    'contextmenu_separator': ContextMenu.Separator,
    'contextmenu_checkboxitem': ContextMenu.CheckboxItem,
    'contextmenu_radiogroup': ContextMenu.RadioGroup,
    'contextmenu_group': ContextMenu.Group,
    'contextmenu_groupheading': ContextMenu.GroupHeading,
    'contextmenu_radioitem': ContextMenu.RadioItem,
    'contextmenu_separator': ContextMenu.Separator
"""
