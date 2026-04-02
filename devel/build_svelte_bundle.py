import sys
#from svelte_bundler import list_jsvars_in_module
from svelte_bundler import build_bundle
target_module = "runner"
dep_modules = [
    "td_bindvalue_component",
    "runner",
    
    ]


build_bundle(target_module,
             dep_modules,
             output_dir="static/svelte_bundle")

