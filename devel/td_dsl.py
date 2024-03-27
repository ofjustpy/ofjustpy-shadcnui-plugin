import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
from shadcnui_components.components  import Breadcrumb


app = oj.load_app()

with writer_ctx:
    with Breadcrumb(classes="bg-green-100") as bc:
        with Breadcrumb.List(classes="bg-blue-100"):

            pass
        pass

wp_endpoint = oj.create_endpoint(key="select",
                                 childs = [
                                     bc
                                           ],
                                 
                                 title="Select"
                                 )
oj.add_jproute("/", wp_endpoint)

# from starlette.testclient import TestClient

# client = TestClient(app)    
# response = client.get('/')
# print(response.text)

