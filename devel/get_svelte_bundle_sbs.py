import sys
#from svelte_bundler import list_jsvars_in_module
from svelte_bundler import build_bundle
target_module = "runner"
dep_modules = [
    "devel_jsexpr_bundler",
    ]

twsty_str=["bg-green-100"]
build_bundle(target_module,
             dep_modules,
             output_dir="static/svelte_bundler")

