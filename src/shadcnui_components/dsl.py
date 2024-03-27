from py_tailwind_utils import *
from macropy.core.macros import Macros
import ast
import astor


macros = Macros()

def translater(comp_type,
               comp_label,
               kwargs_nodes,
               target_ast_node=None, 
               child_comp_call_trees=[]
               ):

    """
    comp_type: None
    comp_label ast: Attribute(value=Name(id='bc'), attr='List')
                     or
                    Attribute(value=Attribute(value=Name(id='oj'), attr='PD'), attr='Prose')
    """
    num_childs = len(child_comp_call_trees)

    childs_keyword = ast.keyword(arg='childs',
                                 value=ast.List(elts=child_comp_call_trees, ctx=ast.Load())

                                 )
    # div_func = ast.Attribute(value=ast.Name(id="Breadcrumb", ctx=ast.Load()),

    #                          )

    #div_func = ast.Name(id="Breadcrumb", ctx=ast.Load()),

    #print("comp_label = ", comp_label)
    #div_func = ast.Name(id=comp_label, ctx=ast.Load())
    call_ast = ast.Call(comp_label,
                        args=[],
                        keywords=[ *kwargs_nodes, childs_keyword]
                        )

    if target_ast_node:
        assign_statement = ast.Assign(targets=[target_ast_node], value=call_ast)
        return assign_statement, ast.Name(id=target_ast_node.id, ctx=ast.Load())
    else:
        return None, call_ast

    
def deal_with_inner_with_block(block_tree):
    assert isinstance(block_tree, ast.With)
    child_with_blocks = [node for node in block_tree.body if isinstance(node, ast.With)]
    child_comp_call_trees = []
    assign_stmts = []
    for child_with_block in child_with_blocks:
        child_assign_stmts, ref = deal_with_inner_with_block(child_with_block)
        assign_stmts.extend(child_assign_stmts)
        assert ref != None
        child_comp_call_trees.append(ref)

    withitem = block_tree.items[0]

    # capture the target varible of the with clause expression
    
    target_ast_node = None
    if withitem.optional_vars:
        target_ast_node = withitem.optional_vars
        pass

    context_expr = withitem.context_expr
    # TODO: about comp_type
    comp_type = None

    if isinstance(context_expr, ast.Call):
        # assume func_node is an attribute
        # Attribute(value=Attribute(value=Name(id='oj'), attr='PD'), attr='Prose')
        func_node = context_expr.func
        assign_stmt, ref = translater(comp_type,
                                      func_node,
                                      context_expr.keywords,
                                      target_ast_node=target_ast_node,
                                      child_comp_call_trees = child_comp_call_trees
                                      )
        if assign_stmt:
            assign_stmts.append(assign_stmt)
        return (assign_stmts, ref)
    elif isinstance(context_expr, ast.Name):
        assert False
        comp_id = context_expr.id
        comp_type = 'Passive'
        assign_stmt, ref = translater(comp_type, comp_id, [], child_comp_call_trees = child_comp_call_trees)
        
        if assign_stmt:
            assert False
            assign_stmts.append(assign_stmt)

        assert False
        return assign_stmts, ref
    else:
        assert False
        
    assert False
    
@macros.block
def writer_ctx(tree, *args, **kw):
    """
    a macro that patches the ast-tree
    : in our use-case -- tree is a list of With nodes
    """
    with_blocks = [node for node in tree if isinstance(node, ast.With)]
    assign_stmts, ref = deal_with_inner_with_block(with_blocks[0])

    return [*assign_stmts]

