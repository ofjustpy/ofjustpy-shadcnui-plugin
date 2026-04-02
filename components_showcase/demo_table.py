import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")



invoices = [
    {
      "invoice": "INV001",
      "paymentStatus": "Paid",
      "totalAmount": "$250.00",
      "paymentMethod": "Credit Card"
    },
    {
      "invoice": "INV002",
      "paymentStatus": "Pending",
      "totalAmount": "$150.00",
      "paymentMethod": "PayPal"
    },
    {
      "invoice": "INV003",
      "paymentStatus": "Unpaid",
      "totalAmount": "$350.00",
      "paymentMethod": "Bank Transfer"
    },
    {
      "invoice": "INV004",
      "paymentStatus": "Paid",
      "totalAmount": "$450.00",
      "paymentMethod": "Credit Card"
    },
    {
      "invoice": "INV005",
      "paymentStatus": "Paid",
      "totalAmount": "$550.00",
      "paymentMethod": "PayPal"
    },
    {
      "invoice": "INV006",
      "paymentStatus": "Pending",
      "totalAmount": "$200.00",
      "paymentMethod": "Bank Transfer"
    },
    {
      "invoice": "INV007",
      "paymentStatus": "Unpaid",
      "totalAmount": "$300.00",
      "paymentMethod": "Credit Card"
    }
  ]

def create_row(invoice):
    # Python equivalent for the HTML snippet
    with writer_ctx:
        with SCUI.Table.Row() as row_box:
            with SCUI.Table.Cell(classes="font-medium"):
                with oj.PD.Prose(text=invoice["invoice"]):
                    pass
            with SCUI.Table.Cell():
                with oj.PD.Prose(text=invoice["paymentStatus"]):
                    pass
            with SCUI.Table.Cell():
                with oj.PD.Prose(text=invoice["paymentMethod"]):
                    pass
            with SCUI.Table.Cell(classes="text-right"):
                with oj.PD.Prose(text=invoice["totalAmount"]):
                    pass

    return row_box

rows = [create_row(invoice) for invoice in invoices
    ]

with writer_ctx:
    with SCUI.Table.Root() as table_box:
        with SCUI.Table.Caption():
            with oj.PD.Prose(text="A list of your recent invoices."):
                pass
        with SCUI.Table.Header():
            with SCUI.Table.Row():
                with SCUI.Table.Head(extra_classes="w-[100px]"):
                    with oj.PD.Prose(text="Invoice"):
                        pass
                with SCUI.Table.Head():
                    with oj.PD.Prose(text="Status"):
                        pass
                with SCUI.Table.Head():
                    with oj.PD.Prose(text="Method"):
                        pass
                with SCUI.Table.Head(classes="text-right"):
                    with oj.PD.Prose(text="Amount"):
                        pass
        with SCUI.Table.Body() as body_div:
            pass
        with SCUI.Table.Footer():
            with SCUI.Table.Row():
                with SCUI.Table.Cell(colspan=3):
                    with oj.PD.Prose(text="Total"):
                        pass
                with SCUI.Table.Cell(classes="text-right"):
                    with oj.PD.Prose(text="$2,500.00"):
                        pass

                    
body_div.components = rows
