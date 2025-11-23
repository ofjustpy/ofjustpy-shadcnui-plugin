import ofjustpy as oj
eyeoff_icon = oj.PC.LucideIcon(label="eyeoff")

oj.set_style("un")

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Slider",
                                 childs = [
                                     eyeoff_icon
                                           ],
                                 
                                 title="Slider",
                                 csr_bundle_dir="svelte_bundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
