from py_tailwind_utils import *
from macropy.core.macros import Macros
import ast
import astor


macros = Macros()

    
@macros.block
def writer_ctx(tree, *args, **kw):
    """
    a macro that patches the ast-tree
    : in our use-case -- tree is a list of With nodes
    """
    for node in tree:
        print (astor.dump_tree(node))
    with_blocks = [node for node in tree if isinstance(node, ast.Call)]
    print (astor.dump_tree(with_blocks))
    x_assign = ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Constant(value=1)
    )

    return [x_assign]

