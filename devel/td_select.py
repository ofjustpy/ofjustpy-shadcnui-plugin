import ofjustpy as oj
from shadcnui_components.components import Select
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *


select = Select(key="select")

             
item1 = select.Item(value="light", text="Light")
item2 = select.Item(value="dark", text="Dark")
group = select.Group(childs=[item1, item2

    ]
             )
             
select.set_slot_content(group, classes="bg-pink-400")
print(select.domDict)

print(select.attrs)
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="select",
                                 childs = [
                                     select
                                           ],
                                 
                                 title="Select"
                                 )
oj.add_jproute("/", wp_endpoint)
                



