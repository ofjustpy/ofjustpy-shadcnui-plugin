import ofjustpy as oj
from shadcnui_components.components import Checkbox, Label
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *


checkbox = Checkbox(key="terms")
label = Label(for_="/terms", text="Accept terms and conditions",
              classes="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70")


label_box = oj.PD.Div(classes="flex items-center space-x-2",
          childs = [checkbox, label

              ]
          )
          
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="alert",
                                 childs = [
                                     label_box
                                           ],
                                 
                                 title="Alert"
                                 )
oj.add_jproute("/", wp_endpoint)
                
