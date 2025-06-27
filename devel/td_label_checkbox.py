import ofjustpy as oj
from shadcnui_components.components import Checkbox, Label
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *
import shadcnui_components as SCUI

# checkbox = Checkbox(key="terms")
# label = Label(for_="/terms", text="Accept terms and conditions",
#               classes="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70")


# label_box = oj.PD.Div(classes="flex items-center space-x-2",
#           childs = [checkbox, label

#               ]
#           )
checkbox = SCUI.Checkbox(key="terms")
label = SCUI.Label(for_="/terms", text="Accept terms and conditions",
              classes="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70")


label_box = oj.PD.Div(classes="flex items-center space-x-2",
          childs = [checkbox, label

              ]
          )

checkbox_box = oj.HCCStatic.Div(key="Checkbox",
                                childs = [label_box],
                                )


app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="checkbox",
                                 childs = [
                                     label_box
                                           ],
                                 
                                 title="Checkbox",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)
                
