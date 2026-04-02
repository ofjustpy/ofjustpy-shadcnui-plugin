import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")
print("importing Buttons")
# with writer_ctx:
#     with SCUI.Breadcrumb.Root() as breadcrumb_box:

button1 = SCUI.Button(key="button1", text="Button", variant="outline", href="#", )

button2 = SCUI.Button(key="button2", text="Button", variant="link", href="#", )

button3 = SCUI.Button(key="button3", text="Button", variant="ghost")

button4 = SCUI.Button(key="button3", text="Button", variant="destructive")


button_box = oj.PD.StackV(childs=[button1, button2, button3, button4], twsty_tags=[space/y/4])


