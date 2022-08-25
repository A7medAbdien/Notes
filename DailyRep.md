# My Daily Training Notes

## Thu, 25 Aug

1. odoo slides 2h
2. odoo dev. video 2h

### slides

topics:

__Using Odoo__:

1. calender
2. activity
3. discussion
4. contacts and importing data
    * she uses v14, the [importing](https://www.odoo.com/documentation/15.0/applications/general/export_import_data.html) differ

### Business Flow

__consumable product__:

1. Marketing (website): generate leads
2. Sales (CRM): handel the lead
   1. lead, create a quotation
   2. verity the quotations via email or signature
3. Purchases (inventory & purchase): sets when do we purchase items
    * Replenishment, order are not in the stuck
      * odoo will generate a request for the quotations, whenever there are not enough in the stuck
4. Inventory (inventory): validate or send requests
    * vender (receive) and delivery (send) requests
5. Accounting (purchase & account): create Bills, and Pay
   1. they check what they received form the vender and what in the bill
   2. Invoicing, in sales create invoices->confirm->send or print->payment

__service product__:

1. sales
2. project
3. time sheets
4. expenses
5. ?account?
