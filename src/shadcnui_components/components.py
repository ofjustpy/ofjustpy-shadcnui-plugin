from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR
from addict_tracking_changes import Dict
from ofjustpy.htmlcomponents_impl import assign_id

def gen_Div_type_by_tag(tag, prefix="", addon_mixins=[], html_tag=None):

    class Mixin:
        def __init__(self, **kwargs):
            self.domDict.vue_type = "shadcnui_component"
            self.domDict.html_tag = f"{prefix}{tag}".lower()

    class_def = gen_Div_type(HCType.passive,
                                 f"{prefix}{tag}",
                                 Mixin,
                                 stytags_getter_func=lambda m=ui_styles: getattr(m.sty,
                                                                                 f"shadcnui_{prefix.lower()}{tag.lower()}"),
                             static_addon_mixins=addon_mixins,
                             html_tag = html_tag
                             )
    
    return class_def


class AlertMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "alert"
        

    Title = gen_Div_type_by_tag("Title", prefix="Alert_")
    Description = gen_Div_type_by_tag("Description", prefix="Alert_")
        
        
Alert = gen_Div_type(
        HCType.passive,
        "Alert",
        AlertMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_alert,
        )


class AlertDialogMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "alertdialog"


    Trigger = gen_Div_type_by_tag("Trigger", prefix="AlertDialog_")
    Content = gen_Div_type_by_tag("Content", prefix="AlertDialog_")
    Header = gen_Div_type_by_tag("Header", prefix="AlertDialog_")
    Title = gen_Div_type_by_tag("Title", prefix="AlertDialog_")
    Description = gen_Div_type_by_tag("Description", prefix="AlertDialog_")
    Footer = gen_Div_type_by_tag("Footer", prefix="AlertDialog_")
    Cancel = gen_Div_type_by_tag("Cancel", prefix="AlertDialog_")
    Action = gen_Div_type_by_tag("Action", prefix="AlertDialog_")

AlertDialog = gen_Div_type(
    HCType.passive,
    "AlertDialog",
    AlertDialogMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_alertdialog,

)
    

class AvatarMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "avatar"

    Image = gen_Div_type_by_tag("Image", prefix="Avatar_",
                                addon_mixins=[TR.ImgMixin],
                                html_tag="avatar_image")
    Fallback = gen_Div_type_by_tag("Fallback",
                                   addon_mixins=[TR.HCTextMixin],
                                   prefix="Avatar_"
                                   )
Avatar = gen_Div_type(
    HCType.passive,
    "Avatar",
    AvatarMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_avatar,
)

shadcnui_avatar = []

shadcnui_avatar_image = []

shadcnui_avatar_fallback = []

class BreadcrumbMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "breadcrumb"

    List = gen_Div_type_by_tag("List", prefix="Breadcrumb_")
    Item = gen_Div_type_by_tag("Item", prefix="Breadcrumb_")
    Link = gen_Div_type_by_tag("Link", prefix="Breadcrumb_", addon_mixins=[TR.AMixin], html_tag="breadcrumb_link")
    Separator = gen_Div_type_by_tag("Separator", prefix="Breadcrumb_")
    Page = gen_Div_type_by_tag("Page", prefix="Breadcrumb_")

Breadcrumb = gen_Div_type(
    HCType.passive,
    "Breadcrumb",
    BreadcrumbMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_breadcrumb
)

class ButtonMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "button"
        for attr in ["variant", "disabled", "href", "size"]:
            if attr in kwargs:
                self.attrs[attr] = kwargs.get(attr)

        if "type_" in kwargs:
            self.attrs["type"] = kwargs.get("type_")
            
Button = gen_Div_type(
        HCType.active,
        "Button",
        ButtonMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_button,
    static_addon_mixins = [TR.HCTextMixin]  
        )
Button = assign_id(Button)

class CalendarMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "calendar"

        

Calendar = gen_Div_type(
        HCType.passive,
        "Calendar",
        CalendarMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_calendar,
        )

class CardMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "card"
    Header = gen_Div_type_by_tag("Header", prefix="Card_")
    Title = gen_Div_type_by_tag("Title", prefix="Card_")
    Description = gen_Div_type_by_tag("Description", prefix="Card_")
    Content = gen_Div_type_by_tag("Content", prefix="Card_")
    Footer = gen_Div_type_by_tag("Footer", prefix="Card_")


Card = gen_Div_type(
        HCType.passive,
        "Card",
        CardMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_calendar,
        )        


class CarouselMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "carousel"

    Content = gen_Div_type_by_tag("Content", prefix="Carousel_")
    Item = gen_Div_type_by_tag("Item", prefix="Carousel_")
    Previous = gen_Div_type_by_tag("Previous", prefix="Carousel_")
    Next = gen_Div_type_by_tag("Next", prefix="Carousel_")

Carousel = gen_Div_type(
    "Carousel",
    CarouselMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_carousel,
)



class CheckboxMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "checkbox"

        

Checkbox = gen_Div_type(
    HCType.active,
        "Checkbox",
        CheckboxMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_checkbox,
    
        )

class CollapsibleMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "collapsible"

    Trigger = gen_Div_type_by_tag("Trigger", prefix="Collapsible_")
    Content = gen_Div_type_by_tag("Content", prefix="Collapsible_")

Collapsible = gen_Div_type(
    HCType.passive,
    "Collapsible",
    CollapsibleMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_collapsible,
)


class CommandMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "command"

    Input = gen_Div_type_by_tag("Input", prefix="Command_") #TODO: use Input mixin
    List = gen_Div_type_by_tag("List", prefix="Command_")
    Empty = gen_Div_type_by_tag("Empty", prefix="Command_")
    Group = gen_Div_type_by_tag("Group", prefix="Command_", ) # TODO: attrs=["heading"]
    Item = gen_Div_type_by_tag("Item", prefix="Command_")
    Separator = gen_Div_type_by_tag("Separator", prefix="Command_")

Command = gen_Div_type(
        HCType.passive,
    "Command",
    CommandMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_command,
)

class DialogMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "dialog"

    Trigger = gen_Div_type_by_tag("Trigger", prefix="Dialog_")
    Content = gen_Div_type_by_tag("Content", prefix="Dialog_")
    Header = gen_Div_type_by_tag("Header", prefix="Dialog_")
    Title = gen_Div_type_by_tag("Title", prefix="Dialog_")
    Description = gen_Div_type_by_tag("Description", prefix="Dialog_")

Dialog = gen_Div_type(
    HCType.passive,
    "Dialog",
    DialogMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_dialog,
)


class DrawerMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "drawer"

    Trigger = gen_Div_type_by_tag("Trigger", prefix="Drawer_")
    Content = gen_Div_type_by_tag("Content", prefix="Drawer_")
    Header = gen_Div_type_by_tag("Header", prefix="Drawer_")
    Title = gen_Div_type_by_tag("Title", prefix="Drawer_")
    Description = gen_Div_type_by_tag("Description", prefix="Drawer_")
    Footer = gen_Div_type_by_tag("Footer", prefix="Drawer_")
    Button = gen_Div_type_by_tag("Button", prefix="Drawer_")
    Close = gen_Div_type_by_tag("Close", prefix="Drawer_")

Drawer = gen_Div_type(
    HCType.passive,
    "Drawer",
    DrawerMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_drawer,
)


class DropdownMenuMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "dropdownmenu"

    Trigger = gen_Div_type_by_tag("Trigger", prefix="DropdownMenu_")
    Content = gen_Div_type_by_tag("Content", prefix="DropdownMenu_")
    Group = gen_Div_type_by_tag("Group", prefix="DropdownMenu_")
    Label = gen_Div_type_by_tag("Label", prefix="DropdownMenu_")
    Separator = gen_Div_type_by_tag("Separator", prefix="DropdownMenu_")
    Item = gen_Div_type_by_tag("Item", prefix="DropdownMenu_")

DropdownMenu = gen_Div_type(
    HCType.passive,
    "DropdownMenu",
    DropdownMenuMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_dropdownmenu,
)

class HoverCardMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "hovercard"

    Trigger = gen_Div_type_by_tag("Trigger", prefix="HoverCard_")
    Content = gen_Div_type_by_tag("Content", prefix="HoverCard_")

HoverCard = gen_Div_type(
    HCType.passive,
    "HoverCard",
    HoverCardMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_hovercard,
)


class InputMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "input"

        if "type_" in kwargs:
            self.attrs["type"] = kwargs.get("type_")
        for attr in ["placeholder", "disabled"]:
            self.attrs[attr] = kwargs.get(attr)
            
            

Input = gen_Div_type(
        HCType.active,
        "input",
        InputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_input,
    static_addon_mixins = [TR.HCTextMixin]  
        )

class LabelMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "label"

        

Label = gen_Div_type(
    HCType.passive,
        "label",
        LabelMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_label,
    static_addon_mixins = [TR.HCTextMixin]  
        )

class MenubarMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "menubar"

    Menu = gen_Div_type_by_tag("Menu", prefix="Menubar_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Menubar_")
    Content = gen_Div_type_by_tag("Content", prefix="Menubar_")
    Item = gen_Div_type_by_tag("Item", prefix="Menubar_")
    Shortcut = gen_Div_type_by_tag("Shortcut", prefix="Menubar_")
    Separator = gen_Div_type_by_tag("Separator", prefix="Menubar_")

Menubar = gen_Div_type(
    HCType.passive,
    "Menubar",
    MenubarMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_menubar,
)
