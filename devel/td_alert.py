import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons



with writer_ctx:
    with SCUI.Alert() as alert_box:
        with SCUI.Alert.Title():
            with oj.PD.Prose(text="Heads up!"):
                pass
            pass

        with SCUI.Alert.Description():
            with oj.PD.Prose(text="You can add components to your app using the cli."):
                pass
                
        
# alert = Alert()

# alert.set_slot_title(oj.PD.Prose(text="Title goes here"),
#                      classes="bg-green-400"
#                      )

# alert.set_slot_content(oj.PD.Prose(text="Content goes here"),
#                      classes="bg-pink-400"
#                      )

# alertdialog = AlertDialog()    
# calendar = Calendar()

# card = Card()

# checkbox = Checkbox()

# label = Label()
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="alert",
                                 childs = [
                                     alert_box
                                           ],
                                 
                                 title="Alert"
                                 )
oj.add_jproute("/", wp_endpoint)

# request = Dict()
# request.session_id = "abc"
# oj.set_style("un")
# sm = oj.get_session_manager(request)
# class WP:
#     def add_component(self, x):
#         pass
#     pass
# wp = WP()
# with  oj.sessionctx(sm):
#     alert_box.stub()(wp)

#     alert_box.build_json()
#     print (alert_box.obj_json)
