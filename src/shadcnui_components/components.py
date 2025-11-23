
from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR
from addict_tracking_changes import Dict
from ofjustpy.htmlcomponents_impl import assign_id

# class BindValueMixin:
#     def __init__(self, attrs=attrs, **kwargs):
        
def gen_Div_type_by_tag(tag,
                        prefix="",
                        #bind_value = False,
                        addon_mixins=None,
                        html_tag=None,
                        attrs=None,
                        runtime_behaviour_type=HCType.passive
                        ):
    """
    bind_value: implies that component is tied to a value e.g.
    <Menubar.RadioGroup bind:value={profileRadioValue}>
    """

    class Mixin:
        def __init__(self, attrs=attrs, **kwargs):
            self.domDict.vue_type = "shadcnui_component"
            self.domDict.html_tag = f"{prefix}{tag}".lower()
            self.domDict.js_eval_map = kwargs.get('js_eval_map', {})
            
            if attrs:
                for attr in attrs:
                    if attr in kwargs:
                        self.attrs[attr] = kwargs.get(attr)

        # @property
        # def html_tag(self):
        #     return self.domDict.html_tag

        # @html_tag.setter
        # def html_tag(self, value):
        #     self.domDict.html_tag = value
        
    class_def = gen_Div_type(runtime_behaviour_type,
                                 f"{prefix}{tag}",
                                 Mixin,
                                 stytags_getter_func=lambda m=ui_styles: getattr(m.sty,
                                                                                 f"shadcnui_{prefix.lower()}{tag.lower()}"),
                             static_addon_mixins=addon_mixins,
                             html_tag = html_tag
                             )
    
    return class_def

# ============================= accordion ============================

class AccordionMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "accordion"
        for key in ['multiple', 'disabled', 'value', 'onValueChange', 'asChild', 'el']:
            if key in kwargs:
                self.attrs[key] = kwargs[key]

        pass
    Root = gen_Div_type_by_tag("Root", prefix="Accordion_")
    Item = gen_Div_type_by_tag("Item", prefix="Accordion_", attrs=['value', 'disabled', 'asChild', 'el'])
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Accordion_")
    Content = gen_Div_type_by_tag("Content", prefix="Accordion_")
    
Accordion = gen_Div_type(
    HCType.passive,
    "Accordion",
    AccordionMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_accordion,
)

class AlertMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "alert"
        

    Root = gen_Div_type_by_tag("Root", prefix="Alert_")        
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


    Root = gen_Div_type_by_tag("Root", prefix="AlertDialog_")        
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

    Root = gen_Div_type_by_tag("Root", prefix="Avatar_")        
    Image = gen_Div_type_by_tag("Image", prefix="Avatar_",
                                addon_mixins=[TR.ImgMixin],
                                html_tag="avatar_image")
    Fallback = gen_Div_type_by_tag("Fallback",
                                   addon_mixins=[TR.HCTextMixin],
                                   prefix="Avatar_"


                                   )

class AspectRatioMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "aspectratio"

        if 'ratio' in kwargs:
            self.attrs['ratio']= kwargs.get('ratio')

AspectRatio = gen_Div_type(HCType.passive,
                     "AspectRatio",
                     AspectRatioMixin,
                     static_addon_mixins=[TR.HCTextMixin],
                     stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_aspectratio,
                     )


Avatar = gen_Div_type(
    HCType.passive,
    "Avatar",
    AvatarMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_avatar,
)



class BadgeMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "badge"

        if 'variant' in kwargs:
            self.attrs['variant']= kwargs.get('variant')

Badge = gen_Div_type(HCType.passive,
                     "Badge",
                     BadgeMixin,
                     static_addon_mixins=[TR.HCTextMixin],
                     stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_badge,
                     )

        
    
Avatar = gen_Div_type(
    HCType.passive,
    "Avatar",
    AvatarMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_avatar,
)




class BreadcrumbMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "breadcrumb"

    Root = gen_Div_type_by_tag("Root", prefix="Breadcrumb_")                
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

        if "variant" in kwargs:
            self.attrs["variant"] = kwargs.get('variant')
        if "value" in kwargs:
            self.domDict["value"] = kwargs.get("value")

    @property
    def value(self):
        """
        The 'value' attribute of the <data> element specifies the machine-readable value associated with the element.
        """
        return self.domDict.get("value", None)

    
Button = gen_Div_type(
        HCType.active,
        "Button",
        ButtonMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_button,
    static_addon_mixins = [TR.HCTextMixin]  
        )
Button = assign_id(Button)



class CardMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "card"
        pass
    Root = gen_Div_type_by_tag("Root", prefix="Card_")
    Header = gen_Div_type_by_tag("Header", prefix="Card_")
    #Header = gen_Div_type_by_tag("Header", prefix="Card_")
    Title = gen_Div_type_by_tag("Title", prefix="Card_")
    Description = gen_Div_type_by_tag("Description", prefix="Card_")
    Content = gen_Div_type_by_tag("Content", prefix="Card_")
    Footer = gen_Div_type_by_tag("Footer", prefix="Card_")
    Action = gen_Div_type_by_tag("Action", prefix="Card_")


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

    Root  = gen_Div_type_by_tag("Root", prefix="Carousel_")        
    Content = gen_Div_type_by_tag("Content", prefix="Carousel_")
    Item = gen_Div_type_by_tag("Item", prefix="Carousel_")
    Previous = gen_Div_type_by_tag("Previous", prefix="Carousel_")
    Next = gen_Div_type_by_tag("Next", prefix="Carousel_")

Carousel = gen_Div_type(
    HCType.passive,
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
Checkbox = assign_id(Checkbox)

class CollapsibleMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "collapsible"
        pass
    Root = gen_Div_type_by_tag("Root", prefix="Collapsible_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Collapsible_")
    Content = gen_Div_type_by_tag("Content", prefix="Collapsible_")

Collapsible = gen_Div_type(
    HCType.passive,
    "Collapsible",
    CollapsibleMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_collapsible,
)


class ContextMenuMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "context-menu"
        pass
    Root = gen_Div_type_by_tag("Root", prefix="ContextMenu_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="ContextMenu_")
    Content = gen_Div_type_by_tag("Content", prefix="ContextMenu_")
    Item = gen_Div_type_by_tag("Item", prefix="ContextMenu_")

ContextMenu = gen_Div_type(
    HCType.passive,
    "ContextMenu",
    ContextMenuMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_context_menu,
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

    Root = gen_Div_type_by_tag("Root", prefix="Dialog_")        
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Dialog_")
    Content = gen_Div_type_by_tag("Content", prefix="Dialog_")
    Header = gen_Div_type_by_tag("Header", prefix="Dialog_")
    Title = gen_Div_type_by_tag("Title", prefix="Dialog_")
    Description = gen_Div_type_by_tag("Description", prefix="Dialog_")
    Footer = gen_Div_type_by_tag("Footer", prefix="Dialog_")

Dialog = gen_Div_type(HCType.passive,
                      "Dialog",
                      DialogMixin,
                      stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_dialog,
                      )


class DrawerMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "drawer"

        pass

    Root = gen_Div_type_by_tag("Root", prefix="Drawer_")
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
        pass

    Root = gen_Div_type_by_tag("Root", prefix="DropdownMenu_")
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
        pass

    Root = gen_Div_type_by_tag("Root", prefix="HoverCard_")
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
            
        if "value" in kwargs:
            self.domDict["value"] = kwargs.get("value")
            
    @property
    def value(self):
        """
        The 'value' attribute of the <data> element specifies the machine-readable value associated with the element.
        """
        return self.domDict.get("value", None)
    

Input = gen_Div_type(
        HCType.active,
        "Input",
        InputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_input,
    static_addon_mixins = [TR.HCTextMixin]  
        )

Input = assign_id(Input)

class LabelMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "label"

        

Label = gen_Div_type(
    HCType.passive,
        "Label",
        LabelMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_label,
    static_addon_mixins = [TR.HCTextMixin]  
        )

class MenubarMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "menubar"

    Root = gen_Div_type_by_tag("Root", prefix="Menubar_")        
    Menu = gen_Div_type_by_tag("Menu", prefix="Menubar_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Menubar_")
    Content = gen_Div_type_by_tag("Content", prefix="Menubar_")
    Item = gen_Div_type_by_tag("Item", prefix="Menubar_")
    Shortcut = gen_Div_type_by_tag("Shortcut", prefix="Menubar_")
    Separator = gen_Div_type_by_tag("Separator", prefix="Menubar_")
    RadioGroup = gen_Div_type_by_tag("RadioGroup",
                                     prefix="Menubar_",
                                     #bind_value = True
                                     )

Menubar = gen_Div_type(
    HCType.passive,
    "Menubar",
    MenubarMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_menubar,
)

class NavigationMenuMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "navigation-menu"
        pass
    Root = gen_Div_type_by_tag("Root", prefix="NavigationMenu_")
    List = gen_Div_type_by_tag("List", prefix="NavigationMenu_")
    Item = gen_Div_type_by_tag("Item", prefix="NavigationMenu_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="NavigationMenu_")
    Content = gen_Div_type_by_tag("Content", prefix="NavigationMenu_")
    Link = gen_Div_type_by_tag("Link", prefix="NavigationMenu_")

NavigationMenu = gen_Div_type(
    HCType.passive,
    "NavigationMenu",
    NavigationMenuMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_navigation_menu,
)

class PopoverMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "popover"
        pass
    Root = gen_Div_type_by_tag("Root", prefix="Popover_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Popover_")
    Content = gen_Div_type_by_tag("Content", prefix="Popover_")

Popover = gen_Div_type(
    HCType.passive,
    "Popover",
    PopoverMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_popover,
)





# ============================ pagination ============================

class PaginationMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "pagination"
        self.attrs["count"] = 100

    Root = gen_Div_type_by_tag("Root", prefix="Pagination_")
    Content = gen_Div_type_by_tag("Content", prefix="Pagination_")
    Item = gen_Div_type_by_tag("Item", prefix="Pagination_")
    PrevButton = gen_Div_type_by_tag("PrevButton", prefix="Pagination_")
    Ellipsis = gen_Div_type_by_tag("Ellipsis", prefix="Pagination_")
    Link = gen_Div_type_by_tag("Link", prefix="Pagination_")
    NextButton = gen_Div_type_by_tag("NextButton", prefix="Pagination_")

Pagination = gen_Div_type(
    HCType.passive,
    "Pagination",
    PaginationMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_pagination,
)


# ============================= Progress =============================
class ProgressMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "progress"
        if 'value' in kwargs:
            self.attrs['value'] = kwargs.get('value')

        if 'max_' in kwargs:
            self.attrs['max'] = kwargs.get('max_')

Progress = gen_Div_type(
    HCType.passive,
    "Progress",
    ProgressMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_progress,
)

# ============================ Radio Group ===========================
class RadioGroupMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "radiogroup"
        pass

    Root = gen_Div_type_by_tag("Root", prefix="RadioGroup_")
    Item = gen_Div_type_by_tag("Item", prefix="RadioGroup_")
    Input = gen_Div_type_by_tag("Input", prefix="RadioGroup_")

RadioGroup = gen_Div_type(
    HCType.passive,
    "RadioGroup",
    RadioGroupMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_radiogroup,
)

# ============================= resizable ============================
class ResizableMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "resizable"

    PaneGroup = gen_Div_type_by_tag("PaneGroup", prefix="Resizable_", attrs=["direction"])
    Pane = gen_Div_type_by_tag("Pane", prefix="Resizable_", attrs=["defaultSize"])
    Handle = gen_Div_type_by_tag("Handle", prefix="Resizable_", attrs=["withHandle"])

Resizable = gen_Div_type(HCType.passive,
    "Resizable",
    ResizableMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_resizable,
)

# ============================ scroll area ===========================

class ScrollAreaMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "scrollarea"

        if "orientation" in kwargs:
            self.attrs["orientation"] = kwargs.get("orientation")
            
ScrollArea = gen_Div_type(
    HCType.passive,
    "ScrollArea",
    ScrollAreaMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_scrollarea,
)

# ============================= separator ============================

class SeparatorMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "separator"
        if 'orientation' in kwargs:
            self.attrs['orientation'] = kwargs.get('orientation')
            
        
Separator = gen_Div_type(
    HCType.passive,
    "Separator",
    SeparatorMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_separator,
)


# =============================== sheet ==============================
class SheetMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "sheet"
        pass
    
    Root = gen_Div_type_by_tag("Root", prefix="Sheet_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Sheet_")
    Content = gen_Div_type_by_tag("Content", prefix="Sheet_")
    Header = gen_Div_type_by_tag("Header", prefix="Sheet_")
    Title = gen_Div_type_by_tag("Title", prefix="Sheet_")
    Description = gen_Div_type_by_tag("Description", prefix="Sheet_")
    Footer = gen_Div_type_by_tag("Footer", prefix="Sheet_")
    Close = gen_Div_type_by_tag("Close", prefix="Sheet_")

Sheet = gen_Div_type(
    HCType.passive,
    "Sheet",
    SheetMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_sheet,
)

# ============================= skeleton =============================
class SkeletonMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "skeleton"

Skeleton = gen_Div_type(
    HCType.passive,
    "Skeleton",
    SkeletonMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_skeleton,
)



# ============================== slider ==============================
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
                self.attrs[attr] = kwargs.get("value")
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

# ============================== switch ==============================

class SwitchMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "switch"

        for attr in ["checked" ]:
            if attr in kwargs:
                self.attrs[attr] = kwargs.get("value")

        

Switch = gen_Div_type(
    HCType.passive,
    "Switch",
    SwitchMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_switch,
)

# =============================== table ==============================
class TableMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "table"

    Root = gen_Div_type_by_tag("Root", prefix="Table_")
    Caption = gen_Div_type_by_tag("Caption", prefix="Table_")
    Header = gen_Div_type_by_tag("Header", prefix="Table_")

    Footer = gen_Div_type_by_tag("Footer", prefix="Table_")
    
    Body = gen_Div_type_by_tag("Body", prefix="Table_")
    Row = gen_Div_type_by_tag("Row", prefix="Table_")
    Head = gen_Div_type_by_tag("Head", prefix="Table_")
    Cell = gen_Div_type_by_tag("Cell", prefix="Table_")

Table = gen_Div_type(
    HCType.passive,
    "Table",
    TableMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_table,
)


# =============================== tabs ===============================
class TabsMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "tabs"

        if 'value' in kwargs:
            self.attrs['value']= kwargs.get('value')
    Root = gen_Div_type_by_tag("Root", prefix="Tabs_", attrs=['value'])
    List = gen_Div_type_by_tag("List", prefix="Tabs_", attrs=['value'])
    Trigger = gen_Div_type_by_tag("Trigger",
                                  prefix="Tabs_",
                                  attrs=['value']
                                  )
    Content = gen_Div_type_by_tag("Content", prefix="Tabs_", attrs=['value'])

Tabs = gen_Div_type(
    HCType.passive,
    "Tabs",
    TabsMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_tabs,
)

# ============================= Textarea =============================
class TextareaMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "textarea"

        for attr in ["placeholder" ]:
            if attr in kwargs:
                self.attrs[attr] = kwargs.get("placeholder")

        

Textarea = gen_Div_type(
    HCType.passive,
    "Textarea",
    TextareaMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_textarea,
    static_addon_mixins = [TR.HCTextMixin]  
)

# ============================= Tooltip =============================

# Class definition for Tooltip
class TooltipMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "tooltip"
        pass
    Provider = gen_Div_type_by_tag("Provider", prefix="Tooltip_")
    Root = gen_Div_type_by_tag("Root", prefix="Tooltip_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Tooltip_")
    Content = gen_Div_type_by_tag("Content", prefix="Tooltip_")

Tooltip = gen_Div_type(
    HCType.passive,
    "Tooltip",
    TooltipMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_tooltip,
)







# ============================== select ==============================
class SelectMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "select"
        pass

    Root = gen_Div_type_by_tag("Root", prefix="Select_")
    Trigger = gen_Div_type_by_tag("Trigger", prefix="Select_")
    Value = gen_Div_type_by_tag("Value", prefix="Select_", attrs=["placeholder"])        
    Group = gen_Div_type_by_tag("Group", prefix="Select_")
    Item = gen_Div_type_by_tag("Item", prefix="Select_", addon_mixins= [TR.HCTextMixin],
                               attrs=["value", "label", "disabled"])

    Label = gen_Div_type_by_tag("Label", prefix="Select_", addon_mixins= [TR.HCTextMixin],
                                
                                )
    Content = gen_Div_type_by_tag("Content", prefix="Select_")
Select = gen_Div_type(
        HCType.passive,
        "Select",
        SelectMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_select,
    
        )


#Select = assign_id(Select)    
