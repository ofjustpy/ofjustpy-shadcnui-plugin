from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.themes import ui_styles
vue_type = "shadcnui_component"
scui_comp_label = "command"


class CommandMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "command_root"


# Base generation pipeline wrapper
_Command = ActiveDiv_StubWrappedTypeGen(
    "Command",
    CommandMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_command,
)

# Module-level component definitions
Root = CSR_comp_generator(_Command)

Input = gen_PassiveDiv_type_by_tag("Input", prefix="Command_")
List = gen_PassiveDiv_type_by_tag("List", prefix="Command_")
Empty = gen_PassiveDiv_type_by_tag("Empty", prefix="Command_")
Item = gen_PassiveDiv_type_by_tag("Item", prefix="Command_")
Shortcut = gen_PassiveDiv_type_by_tag("Shortcut", prefix="Command_")

Separator = gen_PassiveDiv_type_by_tag("Separator", prefix="Command_")


# Sub-component mixin to explicitly capture header attributes
class CommandGroupMixin:

    def __init__(self, **kwargs):
        if "heading" in kwargs:
            self.attrs["heading"] = kwargs.get("heading")


Group = gen_PassiveDiv_type_by_tag("Group",
                                   prefix="Command_",
                                   addon_mixins=[CommandGroupMixin]
                                   )



import_stmt = """import * as Command from "$lib/components/ui/command/index.js";
"""

# Module-level registry mapping using the Command namespace container
kv_label_to_shadcn_comp_map = """
    'command_root': Command.Root,
    'command_input': Command.Input,
    'command_list': Command.List,
    'command_empty': Command.Empty,
    'command_group': Command.Group,
    'command_item': Command.Item,
    'command_separator': Command.Separator
"""
