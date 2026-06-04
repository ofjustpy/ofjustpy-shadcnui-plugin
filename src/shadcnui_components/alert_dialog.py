from .shadcn_type_factory import (gen_ActiveDiv_type_by_tag, gen_PassiveDiv_type_by_tag,
                                  CSR_comp_generator
                                  )

from kavya.type_factory.static_type_factory import ActiveDiv_StubWrappedTypeGen, PassiveDiv_StubWrappedTypeGen
from kavya.themes import ui_styles

kv_label_to_shadcn_comp_map = """
    'alertdialog_root': AlertDialog.Root,
    'alertdialog_trigger': AlertDialog.Trigger,
    'alertdialog_content': AlertDialog.Content,
    'alertdialog_header': AlertDialog.Header,
    'alertdialog_title': AlertDialog.Title,
    'alertdialog_description': AlertDialog.Description,
    'alertdialog_footer': AlertDialog.Footer,
    'alertdialog_cancel': AlertDialog.Cancel,
    'alertdialog_action': AlertDialog.Action,
    """

scui_comp_label = "alert-dialog"
    
class AlertDialogMixin:

    
    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "alertdialog_root"


# Base generation pipeline wrapper
_AlertDialog = ActiveDiv_StubWrappedTypeGen(
    "AlertDialog",
    AlertDialogMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_alertdialog,
)

Root = CSR_comp_generator(_AlertDialog)

Trigger = gen_PassiveDiv_type_by_tag("Trigger", prefix="AlertDialog_")
Content = gen_PassiveDiv_type_by_tag("Content", prefix="AlertDialog_")
Header = gen_PassiveDiv_type_by_tag("Header", prefix="AlertDialog_")
Title = gen_PassiveDiv_type_by_tag("Title", prefix="AlertDialog_")
Description = gen_PassiveDiv_type_by_tag("Description", prefix="AlertDialog_")
Footer = gen_PassiveDiv_type_by_tag("Footer", prefix="AlertDialog_")
Cancel = gen_PassiveDiv_type_by_tag("Cancel", prefix="AlertDialog_")
Action = gen_PassiveDiv_type_by_tag("Action", prefix="AlertDialog_")

    

import_stmt = """import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
"""
