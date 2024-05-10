
import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI

oj.set_style("un")

with writer_ctx:
    with oj.PD.Div(class_="grid w-full gap-2") as with_button_box:
        
        with SCUI.Textarea(placeholder="Type your message here."):
            pass
        
        with SCUI.Button(key="abtn"):
            with oj.PD.Prose(text="Send message"):
                pass


with writer_ctx:            
    with oj.PD.Div(class_="grid w-full gap-1.5") as with_text_box:
        
        with SCUI.Label():
            with oj.PD.Prose(text="Your Message"):
                pass
        
        with SCUI.Textarea(placeholder="Type your message here.", id="message-2"):
            pass
        
        with oj.PD.P(class_="text-sm text-muted-foreground"):
            with oj.PD.Prose(text="Your message will be copied to the support team."):
                pass


with writer_ctx:
    with oj.PD.Div(class_="grid w-full gap-1.5") as with_label_box:
        with SCUI.Label():
            with oj.PD.Prose(text="Your message"):
                pass
        
        with SCUI.Textarea(placeholder="Type your message here.", id="message"):
            pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     with_label_box,
                                     with_text_box,
                                     with_button_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                                        
