# showInReceipt view

will create an inherited view

## Steps

1. `python odoo-bin scaffold showInReceipt C:\Users\bashr\odoo\odoo\custom_addons\`

## 68+69. inheritance, adding field

will add a filed form res.users to sale.order

1. my_inherited_model.py
2. init file
3. manifest file
4. add a field to an inherited view

__my_inherited_model.py__, custom_addons\show_in_receipt\models\product_template.py:

```py
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    showInReceipt = fields.Boolean(
        string='showInReceipt',
    )
```

__init file__,  custom_addons\show_in_receipt\models\\_\_init__.py

```py
from . import product_template
```

__manifest file__, custom_addons\show_in_receipt\\_\_manifest__.py

```py
    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_template_view.xml',
```

__my_inherited_view__, custom_addons\show_in_receipt\views\product_template_view.xml

```xml
<odoo>
    <data>

        <record id="view_product_template_inherit" model="ir.ui.view">
            <field name="name">product.template.inherit</field>
            <field name="model">product.template</field>
            <!-- get ref from External ID of the view you wanna add to it  -->
            <field name="inherit_id" ref="product.product_template_only_form_view" />
            <field name="arch" type="xml">

                <xpath expr="//field[@name='detailed_type']" position="after">

                    <field name="showInReceipt" />

                </xpath>

            </field>
        </record>


    </data>
</odoo>
```
