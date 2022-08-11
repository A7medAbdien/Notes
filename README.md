# Odoo

The videos:

1. [installation](https://youtu.be/eD12tbz6BC4)
2. [setup the environment](https://youtu.be/LS8tdWoiOQQ)

* could to try [it](https://youtu.be/XBR_hcwY0HE)

## Usefully commands

`python odoo-bin -d odoo15 -r odoo -w odoo`

`python odoo-bin scaffold om_hospital addons\`

`git commit -am "git commit -a --allow-empty-message -m ''"`

## Notes from the [playlist](https://youtube.com/playlist?list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU)

### `__manifest__.py` file

```py
"application": True,
"sequence": -100,
```

### Adding the icon

1. create a directory "static"
2. create a directory "description"
3. add the image with name "icon" *the image will automatically added*

### Creating Database Tables

each model is a table in the database contain whatever data, customer, sales history...etc

1. create a directory "models"
2. create the "_\_init__.py" file
3. create a file "patient.py"
4. in the main "_\_init__.py" add `from . import models`
5. in the models/_\_init__.py add `from . import patient`

In the patient.py:

```py

from odoo import api, fields, models

class HospitalPatient(models.Model):
  # that will create a table with name "hospital_patient"
  _name = "hospital.patient"
  _description = "Hospital Patient"

  name = fields.Char(string="Name")
  age = fields.Integer(string="Age")
  # list with tubules (key,value)
  gender = fields.Selection([('male','Male'),('female', 'Female')], string="Gender")
```

Too see the changes:

1. in Apps, install/upgrade the model
2. in settings -> technical -> database structure -> modules
3. search for the table name

Another way

1. `psql –U postgres`
2. `\c odoo` the database name
3. `select * from hospital_patient` the model name

Note: add a space at the begging of select statement

---

### 4.Create Menu

1. create dir. views
2. inside views dir. create menu.xml file

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <odoo>
      <menuitem id="menu_hospital_main" name="Hospital" action="" />
      <menuitem id="menu_patient_main" name="Patient Details" action="" parent="menu_hospital_main" />
      <menuitem id="menu_patient_details" name="Patients" action="" parent="menu_patient_main" />
    </odoo>
    ```

3. import the menu file in the manifest file by

    ```py
    'data' :['views/menu.xml']
    ```

Too see the changes:

1. upgrade the model
2. more info about the model
3. installed features/ created menus

---

### 5.Create Window Action

1. create a patient.xml file

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <odoo>

      <record id="action_hospital_patient" model="ir.actions.act_window">
        <field name="name">Patients</field>
        <field name="type">ir.actions.act_window</field>
        <field name="res_model">hospital.patient</field>
        <field name="view_mode">tree,form</field>
        <field name="context" eval="{}" />
        <field name="help" type='html'>
          <p class='o_view_nocontent_smiling_face'>
            Create your first patient!
          </p>
        </field>
      </record>

    </odoo>
    ```

2. import it in the manifest file

    ```py
    'data' :['views/menu.xml','views/patient.xml']
    ```

Too see the changes:

1. upgrade the model
2. settings>technical>Window Actions
3. search for Name of your action

---

### 6. Link Menu And Actions

1. edit the menu to be :

    ```py
    <menuitem id="menu_patient_details" name="Patients" action="action_hospital_patient" parent="menu_patient_main" />
    ```

2. from the debugging icon, became a superuser
3. now u can see the hospital in the main menu

__NOTE:__ to get an existing action go for it works and from the debugging icon, edit action

__Important:__ must create any menuitem that uses an action, after their action. So we the `Patients` menuitem will be moved to `patient.xml`, because the execution start in manifest in the data object executing them one by one, so when it executes the `menu.xml` will find a menuitem that has an action that still didn't created, causing an error.

### 7. security rights

in custom_addons\hospital\security\ir.model.access.csv

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
hospital.access_hospital_patient,access_hospital_patient,hospital.model_hospital_patient,base.group_user,1,1,1,1
```

### 8. set menu icon

install web_responsive and add int to custom_addons

in custom_addons\hospital\views\menu.xml edited to be

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <menuitem id="menu_hospital_main" name="Hospital" sequence="0" web_icon="hospital,static\description\icon.png" />
  <menuitem id="menu_patient_main" name="Patient Details" sequence="0" parent="menu_hospital_main" />
</odoo>
```

then uninstall the model in the app list not the custom_addons

### 9+10. create tree and form view

__NOTICE__ that here we will add here a filed called ref in the patient model, copy name filed and change its name to ref with string value Reference. (in custom_addons\hospital\models\patient.py)

```py
ref = fields.Char(string="Recreance")
```

in custom_addons\hospital\views\patient_view.xml add this after `<odoo>`

```xml

  <record model="ir.ui.view" id="view_hospital_patient_tree">
    <field name="name">hospital patient</field>
    <field name="model">hospital.patient</field>
    <field name="arch" type="xml">
      <tree>
        <field name="name" string="Patient Name" />
        <field name="ref" />
        <field name="age" />
        <field name="gender" />
      </tree>
    </field>
  </record>


  <record model="ir.ui.view" id="view_hospital_patient_form">
    <field name="name">hospital patient</field>
    <field name="model">hospital.patient</field>
    <field name="arch" type="xml">
      <form>
        <sheet>
          <group>
            <group>
              <field name="name" />
              <field name="age" />
            </group>
            <group>
              <field name="gender" />
              <field name="ref" />
            </group>
          </group>
        </sheet>
      </form>
    </field>
  </record>

```

### 11. add search view

in custom_addons\hospital\views\patient_view.xml add this after form view

```xml
  <record model="ir.ui.view" id="view_hospital_patient_search">
    <field name="name">hospital patient</field>
    <field name="model">hospital.patient</field>
    <field name="arch" type="xml">
      <search string='test'>
        <field name="name" string="Patient Name" filter_domain="['|',('name', 'ilike', self),('ref', 'ilike', self)]" />
        <field name="age" />
        <field name="gender" />
      </search>
    </field>
  </record>
```

__NOTES__:

* in filter_domain to have more than oen or condition,'|', add another '|' and add the condition
  * filter_domain="['|','|',('name', 'ilike', self),('anotherValue', 'ilike', self),('ref', 'ilike', self)]"

### 12. add filter and search view

__NOTES__:

1. separator to not allow the or operation, when u select more than one filter
2. `&lt;` means less than,'<'.

```xml
  <record model="ir.ui.view" id="view_hospital_patient_search">
    <field name="name">hospital patient</field>
    <field name="model">hospital.patient</field>
    <field name="arch" type="xml">
      <search string='test'>
        <field name="name" string="Patient Name" filter_domain="['|',('name', 'ilike', self),('ref', 'ilike', self)]" />
        <field name="age" />
        <field name="gender" />
        <filter string="Male" name="filter_male" domain="[('gender','=','male')]" />
        <filter string="Female" name="filter_female" domain="[('gender','=','female')]" />
        <separator />
        <filter string="Kids" name="filter_kids" domain="[('age','&lt;=','5')]" />
        <group expand="0" string="Group By">
          <filter string="Gender" name="group_by_gender" context="{'group_by':'gender'}" />
        </group>
      </search>
    </field>
  </record>
```

### 13. archive and not

in custom_addons\hospital\models\patient.py add active filed

```py
    active = fields.Boolean(string="Active", default=True)
    age = fields.Integer(string="Age")
    # list with tubules (key,value)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender")
    name = fields.Char(string="Name")
```

in custom_addons\hospital\views\patient_view.xml add active filed

in form record

```xml
<group>
  <field name="gender" />
  <field name="ref" />
  <field name="active" invisible="1" />
</group>
```

in search record

```xml
<separator />
<filter string="Kids" name="filter_kids" domain="[('age','&lt;=','5')]" />
<separator />
<filter string="Archive" name="filter_archive" domain="[('active','=',False)]" />
```

## 14. Apply domain for a menu

1. model will be from patient.hospital
2. view:

   ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <odoo>

      <record id="action_hospital_female_patient" model="ir.actions.act_window">
        <field name="name">Female Patients</field>
        <field name="type">ir.actions.act_window</field>
        <field name="res_model">hospital.patient</field>
        <field name="view_mode">tree,form</field>
        <field name="context">{}</field>
        <field name="domain">[('gender','=','female')]</field>
        <field name="help" type='html'>
          <p class='o_view_nocontent_smiling_face'>
                Create your first patient!
          </p>
        </field>
      </record>

      <menuitem id="menu_female_patient_details" name="Female Patients" action="action_hospital_female_patient" parent="menu_patient_main" />
    </odoo>
   ```

3. add it to the custom_addons\hospital\_*manifest*_.py

  ```py
  'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ],
  ```

## 15. Set Default Value Using Context

in view, custom_addons\hospital\views\female_patient_view.xml

```xml
<field name="context">{"default_gender":"female","default_age":"20"}</field>
```

rather than keeping it empty

## 16. Set Default filter Using Context

in view, custom_addons\hospital\views\patient_view.xml

```xml
<field name="context">{'search_default_filter_male':1,'search_default_group_by_gender':1}</field>
```

## 17. Adding chatter

1. in custom_addons\hospital\_*manifest*_.py

   ```py
   'depends': ['mail'],
   ```

2. in custom_addons\hospital\models\patient.py

   ```py
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
   ```

3. in custom_addons\hospital\views\patient_view.xml

  ```xml
  <div class="oe_chatter">
    <field name="message_follower_ids" widget="mail_followers" />
    <field name="activity_ids" widget="mail_activity" />
    <field name="message_ids" widget="mail_thread" />
  </div>
  ```

## 18. Enable Tracking For Fields to show in the chatter

in custom_addons\hospital\models\patient.py add tracking attribute

```py
active = fields.Boolean(string="Active", default=True)
age = fields.Integer(string="Age", tracking=True)
# list with tubules (key,value)
gender = fields.Selection(
    [('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
name = fields.Char(string="Name", tracking=True)
```

## 19. Add searchpanel

in search tag in patient_view.xml

```xml
<searchpanel>
  <field name="gender" enable_conter="1" />
</searchpanel>
```

## 20. Add Many2one Field

1. create model file, custom_addons\hospital\models\appointment.py

   ```py
   from odoo import models, fields, api

    class HospitalAppointment(models.Model):
        # that will create a table with name "hospital_appointment"
        _name = "hospital.appointment"
        _inherit = ['mail.thread', 'mail.activity.mixin']
        _description = "Hospital Appointment"

        patient_id = fields.Many2one('hospital.patient', 'Patient')

   ```

2. add it to init in model dir, custom_addons\hospital\models\_*init*_.py

    ```py
    from . import models
    from . import patient
    from . import appointment
   ```

3. crete view (where we add the many2one field), custom_addons\hospital\views\appointment_view.xml

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <odoo>

      <record model="ir.ui.view" id="view_hospital_appointment_tree">
        <field name="name">hospital appointment</field>
        <field name="model">hospital.appointment</field>
        <field name="arch" type="xml">
          <tree></tree>
        </field>
      </record>


      <record model="ir.ui.view" id="view_hospital_appointment_form">
        <field name="name">hospital appointment</field>
        <field name="model">hospital.appointment</field>
        <field name="arch" type="xml">
          <form>
            <sheet>
              <group>
                <group>
                  <field name="patient_id" />
                </group>
                <group></group>
              </group>
            </sheet>

            <div class="oe_chatter">
              <field name="message_follower_ids" widget="mail_followers" />
              <field name="activity_ids" widget="mail_activity" />
              <field name="message_ids" widget="mail_thread" />
            </div>

          </form>
        </field>
      </record>


      <record id="action_hospital_appointment" model="ir.actions.act_window">
        <field name="name">appointments</field>
        <field name="type">ir.actions.act_window</field>
        <field name="res_model">hospital.appointment</field>
        <field name="view_mode">tree,form</field>
        <field name="context">{}</field>
        <field name="help" type='html'>
          <p class='o_view_nocontent_smiling_face'>
                Create your first appointment!
          </p>
        </field>
      </record>

      <menuitem id="menu_appointment_details" name="Appointments" action="action_hospital_appointment" parent="menu_patient_main" />
    </odoo>
    ```

4. add it to manifest, custom_addons\hospital\_*manifest*_.py

   ```py
      # -*- coding: utf-8 -*-

    {
      'name': "hospital",
      "application": True,
      "sequence": -101,
      'summary': """
          Short (1 phrase/line) summary of the module's purpose, used as
          subtitle on modules listing or apps.openerp.com""",

      'description': """
          Long description of module's purpose
      """,

      'author': "My Company",
      'website': "http://www.yourcompany.com",

      # Categories can be used to filter modules in modules listing
      # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
      # for the full list
      'category': 'Uncategorized',
      'version': '0.1',

      # any module necessary for this one to work correctly
      'depends': ['mail'],

      # always loaded
      'data': [
          'security/ir.model.access.csv',
          'views/menu.xml',
          'views/patient_view.xml',
          'views/appointment_view.xml',
          'views/female_patient_view.xml',
      ],
      # only loaded in demonstration mode
      'demo': [
          'demo/demo.xml',
      ],
    }
   ```

5. edit the security access

   ```py
    id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
    hospital.access_hospital_patient,access_hospital_patient,hospital.model_hospital_patient,base.group_user,1,1,1,1
    hospital.access_hospital_appointment,access_hospital_appointment,hospital.model_hospital_appointment,base.group_user,1,1,1,1
   ```

## 21+22. add date and datetime with default value

__carful:__ Date and Datetime not date and datetime

in custom_addons\hospital\models\appointment.py

```py
appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now)
booking_date = fields.Date(
    string="Booking Date", default=fields.Date.context_today)
```

in custom_addons\hospital\views\appointment_view.xml under the patient_id

```xml
<field name="appointment_time" />
<field name="booking_date" />
```

## 23. Add Related Field

in custom_addons\hospital\models\appointment.py

```py
gender = fields.Selection(related="patient_id.gender", readonly=True)
```

__notice:__ readonly if False will allow to make change to the value and it is by default True in the related field

## 24. Add Computed Field

1. edit the age field
2. add date of birth field(dob)
3. crete the compute function
4. comment the age filter, because the computed field does not store in the DB

### in custom_addons\hospital\models\patient.py

```py
dob = fields.Date(string="Date of Birth")
age = fields.Integer(string="Age", tracking=True, compute='_compute_age')
# age = fields.Integer(string="Age", tracking=True, compute='_compute_age', store=True)

@api.depends('dob')
    def _compute_age(self):
        print("self................", self)
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1
```

### in custom_addons\hospital\views\patient_view.xml

```xml
<!-- <separator /> -->
<!-- <filter string="Kids" name="filter_kids" domain="[('age','&lt;=','5')]" /> -->
```

## 25.onchange field

1. add field that will show the change, in model file
2. create the onchange function, in model file
3. add it in view

## 26. _rec_name

1. it is what we see in the navigation bar!!
2. what will be seen if we used this value in many2one field

## 27. notebook

under the sheet tag add `<notebook><page><group><field>`

## 28. HTML field

1. add it in the model
2. add it in the view
3. add placeholder attribute

## 29. Remove Create, Edit, Delete and Duplicate Options From Views

in from or tree tag add `crete='0'`

this what i needed after editing the access rights of the employee to deny him from creating a quotation

## 30. Priority Widget

1. add new selection field in model
2. add it to the view

## 31. Status bar

1. add new selection field in model
2. add it to the view

## 32+33+34. two types of buttons & confirmation massage & help massage

1. action: to do a window action
2. object: to run a python code

in custom_addons\hospital\views\appointment_view.xml

```xml
<button name="action_test" string="Object Button" type="object" class="oe_highlight" confirm='confirm massage' />
<button name="%(hospital.action_hospital_patient)d" string="Action Button" type="action" class="oe_highlight" help='this will redirect u to patient' />
```

in custom_addons\hospital\models\appointment.py

```py
def action_test(self):
  print('test!!!!!!!!!!!!!!!!!!!!')
```

## 35. add else in the computed fields

## 36. rainbow effect

in custom_addons\hospital\models\appointment.py

```py
def action_test(self):
  print('test!!!!!!!!!!!!!!!!!!!!')
  return {
    'effect': {
        'fadeout': 'slow',
        'message': 'Printed',
        'type': 'rainbow_man',
    }
  }
```

## 37+38. Badge Widget And Decorations & Color tree

in the tree view custom_addons\hospital\views\appointment_view.xml

```xml
<tree decoration-success="state =='done'" decoration-info="state =='draft'" decoration-danger="state=='in_consultation'">
  <field name="state" widget='badge' decoration-success="state == 'done'" decoration-info="state =='draft'" decoration-danger="state=='in_consultation'" />
```

1. decoration-muted, gray
2. decoration-info, blue
3. decoration-success, green
4. decoration-warning, yellow
5. decoration-danger, red
