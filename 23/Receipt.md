# solutions

if there is a description will be printed, if there is not it will not

## edit the models.js

\addons\point_of_sale\static\src\js\models.js Orderline export_for_printing

just search for "product_name_wrapped"

then under id add:

```js
id: this.id,
NotPrinted: this.product.description_sale,
quantity: this.get_quantity(),
```

## edit receipt xml

\addons\point_of_sale\static\src\xml\Screens\ReceiptScreen\OrderReceipt.xml OrderLinesReceipt

just search for "product_name_wrapped"

then add, follow under the loop :

```xml
<t t-foreach="receipt.orderlines" t-as="line" t-key="line.id">
  <t t-if="!line.NotPrinted">
```

## notes

to see if there is a description or not

in \addons\point_of_sale\static\src\js\models.js Orderline:

```js
this.product = options.product;
console.log(this.product);
```

## additional problems

* the conflict in the total and the price per unit
  * solution: let the price of the bag equal to 0

## front end

the filed of description_sales edited to be: (addons\product\models\product_template.py)

```py
description_sale = fields.Boolean('Not Printed', default=False, help="If checked, it will print the product in the receipt.")
```

and its xml to be : (addons\product\views\product_views.xml)

```xml
<group>
  <group string="NOT Printed in the Receipt" name="description">
    <field name="description_sale" placeholder="If checked, it will not ptint this product in the receipt." />
  </group>
</group>
```

xml view can be edited also form the debugging icon.
