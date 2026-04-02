from svelte_bundler.csr import  build_csr_svelte_bundle
from twtags_safelist import (get_csr_components, 
                             get_twtags_safelist
                             )

# res  = get_twtags_safelist("td")
#page_csr_components = get_csr_components("td")
# print(res)
# print(page_csr_components)
#print(page_csr_components)
build_csr_svelte_bundle("td")
