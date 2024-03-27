import ofjustpy as oj
from shadcnui_components.components import Card, Button,Label, Input, Select
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *


select = Select(key="select")
item1 = select.Item(value="sveltekit", label="Sveltekit", text="Sveltekit")
item2  = select.Item(value="next", label="Next.js", text="Next.js")
item3 = select.Item(value="nuxt", label="Nuxt.js", text="Nuxt.js")

select.set_slot_content(item1, item2, item3)


card = Card()
card.set_slot_title(text="Create Project", classes="variant-filled")

card.set_slot_description(text="Deploy your new project in one-click.", classes="variant-filled-primary"

                           )

content  = oj.PD.Div(classes="grid w-full items-center gap-4",
                     childs = [oj.PD.Div(classes="flex flex-col space-y-1.5",
                               childs= [Label(for_="/terms", text="Name",
                                              classes=""),
                                        Input(key="name", placeholder="Name of your project")
                               ]
                               

                               ),
                     oj.PD.Div(classes="flex flex-col space-y-2",
                               childs = [Label(for_="/framework", text="Framework",
                                               classes=""),
                                         select
                                   

                                   ]
                               )
                               ]
                     )
card.set_slot_content(content
    )

card.set_slot_footer(Button(key="button1", text="Cancel", variant="outline", href="#", ),
                     Button(key="button2", text="Deploy", variant="link", href="#", ),
                     classes="flex justify-between",

    )

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="cards",
                                 childs = [
                                     card
                                           ],
                                 
                                 title="Cards"
                                 )
oj.add_jproute("/", wp_endpoint)
                



