# MY Problem

C:\Users\bashr\odoo\odoo\addons\product\models\product_template.py 131

C:\Users\bashr\odoo\odoo\addons\point_of_sale\static\src\xml\Screens\ReceiptScreen\OrderReceipt.xml


C:\Users\bashr\odoo\odoo\addons\point_of_sale\models\pos_order.py 1274

product = self.env['product.product'].browse(line[2]['product_id'])

C:\Users\bashr\odoo\odoo\addons\point_of_sale\static\src\js\models.js

I want to allow the user to decide either to print this product in the receipt or not on odoo15.

So, I added a boolean field to product.template, let us call it "inReceipt". Then I have to check if this field is True or false in the receipt xml, and here is where I stocked.

What I found so far:

1. where I have to add the condition, \addons\point_of_sale\static\src\xml\Screens\ReceiptScreen\OrderReceipt.xml t-name="OrderLinesReceipt"
2. so the inReceipt needs to be in "receipt.orderlines" so I can access it
3. "receipt.orderlines" coming from \addons\point_of_sale\static\src\js\models.js Orderline
4. Orderline uses Backbone to get its values

I think the next step that I have to understand is how Backbone works to add inReceipt value to it.

Any recommendation, advice, or evaluation is appreciated.

Small note: this is my first training month as a programmer or odoo developer.
