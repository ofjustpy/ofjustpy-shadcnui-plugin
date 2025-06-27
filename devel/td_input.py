import ofjustpy as oj
from shadcnui_components import Checkbox, Label, Input, Button
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *


inp1 = Input(key="inp1", type="email", placeholder="email", classes="max-w-xs")
inp_with_label = oj.PD.Div(classes="flex w-full max-w-sm flex-col gap-1.5",
               childs=[Label(for_="email", text="Email"),
                       Input(key="inp1", type="email", placeholder="email", classes="max-w-xs")
                   ]
        )

inp_with_label_text = oj.PD.Div(classes="flex w-full max-w-sm flex-col gap-1.5",
               childs=[Label(for_="email", text="Email"),
                       Input(key="inp1", type="email", placeholder="email", classes="max-w-xs"),
                       oj.PC.Prose(text="Enter your email address.", extra_classes="text-muted-foreground")
                    
                   ]
        )

inp_with_button = oj.AD.Form(key="aform", classes="flex w-full max-w-sm items-center space-x-2",
                                 childs = [Input(key="inp1", type="email", placeholder="email", classes="max-w-xs"),
                                           Button(key="abtn", type_= "submit",text="Subscribe")
                                           

                                     ]
                                 )

                                 
tlc = oj.PD.StackV(childs=[inp1, inp_with_label, inp_with_label_text, inp_with_button],
             twsty_tags=[space/y/4]
             )
          
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Input",
                                 childs = [
                                     tlc
                                 ],
                                 
                                 title="Input",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)
                
