# My Daily Training Notes

## 23 Jul

1. cache flow
2. Hosting
3. show item in recept or not
4. payment method

### solution (cache flow)

it is enabled automatically. Only the admin how can close a session.

#### to control it

1. enable the Authorized Employees in the setting of session
2. add another user, make sure in HR Setting, Employee Type is Employee
3. go to the admin HR Setting and add PIN code, it will work as a Password in POS.

## 24 Jul

1. Azure
2. Order reports

## 25 jul

1. improve development environment (run the server form VScode)
2. Offers management
3. wire to connect tab with receipt printer

## 26 jul

1. dev videos
2. Restart everything cuz using the advanced uninstaller to uninstall Unity 2017

## wed, July 27

1. Present the receipt printer options (DONE)
2. Start working on CRM module (DONE)
3. Set a plan to adapting POS for the fish shop (STILL)
4. Development playlist,form 12 to 16 (STILL)

## Thu, July 27 (HOME)

1. try to test the printer (DONE)
2. more about CRM

## Mun, August 1

1. more about CRM (DONE)
2. Development playlist,form 12 to 18 (DONE)

## Tue, 2 Aug

1. Development playlist,form 18 to 28

## Wed, 3 Aug

1. CRM use case
   * users access rights, let the team shear the leads (Failed)

## Thu, 4 Aug

* understand the pipeline/company work
* let the follower see access the lead(50%)
* let only manager can crate a Quotation(90%)

## Sat, 6 Aug

* set some activities for the scenario and testing them

### problems - in case the manager wanna do the employees work

* manager can not assign an activity to an employee that is not have an access to that lead
* followers can not see the sheared lead:
  1. manager cant invite employees
  2. employee cant invite employee
  3. employee can invite the manager

## Sun, 7 Aug

1. followers can not see the sheared lead: (the company will take as it is)
   1. manager cant invite employees (not that important)
   2. employee cant invite employee (might effect if the team leader need to see others work)
   3. employee can invite the manager (anyway he can see all leads :))
2. finish the odoo tutorial 1 course
3. dev videos 24->34
4. send the quotation to the customer

## Mon, 8 Aug (Holyday)

1. solve the follower issue (DONE)
2. solve the team leader issue (DONE)

## Thu, 11 Aug

1. email server (DONE)
2. Group access rights (DONE)
3. handel notification [Odoo, email]
4. Integrate Outlook calender (UNNECESSARILY)
5. Disable filtering (STILL)

## Sat, 13 Aug

1. Disable filtering (DONE)
2. Manager sees the Dashboard as a default rather than Kanban view (UNAPPLICABLE)

## Mon, 22 Aug

1. Developing my programming skills plane
2. 71->81 odoo dev. video
3. work on training report

## Wed, 24 Aug

1. dev video x10 (NOT DONE)
2. some explanation with the sales manager
    * this discussion toke two hours. I could not understand what he was asking about for the whole two hours, it seemed to me that he did not have a clear issue or problem. I asked him to explain it, then I asked him to write it, eventually, I asked him clearly, "what is the problem? I can not get what you asking about." He responds, "There is no problem, I just need an explanation." Here I realized that my brain had structured to understand each conversation as a problem trying to solve. So, I started to explain each field and what it does, my explanation was awful, so I played a video form the formal odoo website, and it worked, he finally got what he wants from 5 minutes video, which I still do not know what it was.
    * Lessons:
      1. when I talk to people have no background in programming or they are new to a system, start with a simple explanation for the purpose of the whole system moving to the purpose of each field.
      2. separate a normal conversation or question, than problem solving

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

## Mon, 29 Aug

1. Odoo slides
   1. business use case x1
   2. studio x5
   3. CRM (without lead)
2. adjust employee model
3. why salesperson is shown all users not a sales team members (wishes/NOT DONE)

### salesperson

asked in help form, and tried to work on it. we will need to access the hr.employee from crm.lead, where user_id is the same and display all his child_id
