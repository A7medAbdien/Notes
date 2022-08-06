# CRM ep.1

## Wed, 27 june

## feature it provides

1. profile the customers, analyze their interest or actions
2. show the progress of each deal or opportunity
3. manage seals teams
4. automate activities
5. lead management:
   1. lead generation
   2. lead enrichment, if u have one information about the customer and you want to get the rest. Ex: by knowing the email, the system can get the name, phone... etc.
   3. lead mining

## things should to clarify for the adaption

1. important information about the customer
   * how the business will evaluate the customer priority.
2. nature of my pipeline, steps, or steps
3. structure of sales team
   * based on what they spited
4. Activity and their order.
   * like Call, Create Quote.. etc.
5. how the business get its customers (for lead management)
   * Ex: tack IP address of a visitor for the business website

## Mon, 1 Aug

following this [playlist](https://youtube.com/playlist?list=PLeJtXzTubzj8dSeQ6dVDOU4Rlh5AQbTFO)

1. salespersons management
2. *create and group leads*
3. moving leads to opportunities
4. Opportunities management
   * Schedule an activity from the pipeline by clicking on the "clock icon"
   * color in the pipeline, means status of activities assigned each opp. and they can be grouped by it.
5. Sales Team
   * Rather than just wining, it can send a Quotation
      1. 'NEW RENTAL' option, it require Rental model
      2. Quotation, require Sales model
6. lost opp. management
7. Commission plane
   * gives a discount based on customer partner level
     1. install the model, resellers commission for..
     2. set the commission plan
     3. set the partner levels, link it with commission plan
     4. In the customer profile set the customer partner level
     5. continue the process of selling, **the tex will be added on the discount** and the purchase model used in this process!
8. Activity management
9. *lead Generation*
10. pipeline customization
11. *lead mining*
12. Tags management, custom group by, show them in the forecast report
13. forecast report (different views of report)
14. *lead enrichment*
15. pipeline report
    * in table view after setting it to fit the need it can be inserted in a spreadsheet
16. Assignment of opportunities for a salesperson based on a rule exist in the sales team
    * require an activation form the setting
    * it can be skipped form in the sales team profile
17. summary all
18. using spreadsheet
    1. install model Spreadsheet
    2. can be accessed via Document

### Representation

1. add a sales person, will require to add a user
2. access the DB via incognito browser
3. test it assign some opp. to the new user

### auto assign feature

* any opp that is not assigned to anyone is shown for the admin by default
* the assigning from who to whom is saved in chatter

## Wed, 3 Aug

I am trying to set a use case for the sales team, I have to..

1. set employee structure, this [link](https://www.odoo.com/forum/help-1/how-to-define-user-groups-186064) was useful.
2. each team see its own opp.
3. test the employee roles of on some leads

### Components of CRM model

knowing the components will help to set the access right for each group

1. leads (see wt u own, or all)
2. customers (all can see, create, edit)
3. acclivities
   1. all can assign to any
   2. only administration can create a newly activity type
4. Reports, based on what u see in the pipeline
5. losing reasons (all can see, create, edit)
6. tags (all can see, create, edit)
7. members-employees, only officer can edit
8. pipeline structure, only administration

## Thu, 4 Aug

* understand the pipeline/company work
* let the follower see access the lead(50%)
* let only manager can crate a Quotation(90%)

### solutions

1. send email to the new follower
2. they can see the button and fill the data but they can not crete a quotation

### domain notes

```py
['|',('team_id','=',False),('team_id', 'in', [user.team_id.id])]
['&', ('user_id','=',user.id), ('section_id.member_ids', 'in', [user.team_id])]
['&', ('user_id','=',user.id), ('section_id.member_ids', 'in', [(user.team_id.crm_team_member_ids[1])])]
```

### need to know about the scenario

* quotation duration to send to client
* lead time

## Sat, 6 Aug

* set some activities for the scenario and testing them

### problems - in case the manager wanna do the employees work

* manager can not assign an activity to an employee that is not have an access to that lead
* followers can not see the sheared lead:
  1. manager cant invite employees
  2. employee cant invite employee
  3. employee can invite the manager

### solution

* edit the access right of leads(Failed)
* ask the community
