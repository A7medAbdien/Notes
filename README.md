# Odoo

The videos:

1. [installation](https://youtu.be/eD12tbz6BC4)
2. [setup the environment](https://youtu.be/LS8tdWoiOQQ)

* could to try [it](https://youtu.be/XBR_hcwY0HE)

## Usefully commands

`python odoo-bin -d odoo -r odoo -w odoo`

`python odoo-bin scaffold om_hospital addons\`

`git commit -am "git commit -a --allow-empty-message -m ''"`

## Notes from the [playlist](https://youtube.com/playlist?list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU)

### 1. `__manifest__.py` file

```py
"application": True,
"sequence": -100,
```

### 2. Adding the icon

1. create a directory "static"
2. create a directory "description"
3. add the image with name "icon" *the image will automatically added*

### 3. Creating Database Tables

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

## 39. Widget List Activity

1. activity is in the models when we inherited the mail model
2. just add it to the tree and activate the widget, in

   ```xml
   <field name="activity_ids" widget='list_activity' />
   ```

## 40. Optional Field Visibility In List View

1. in tree view fields

   ```xml
   <field name="appointment_time" optional="show" />
   ```

## 41. many2one_avatar_user and many2one_avatar

the one with user open the chat, the other not

1. create field based on users of odoo domain
2. add it to the view with `widget='many2one_avatar_user'`

## 42+43. make field 'collaborative':true && 'resizable': true

in html field in the appointment model, add `options="{'collaborative': true, 'resizable': true}"`

## 44. Default Focus

select the field that you want to be focused when the user start edit the record and add `default_focus='1'`, underscore

```xml
<field name="booking_date" default_focus="1" />
```

## 45. show sample data in the background when there is no data

in tree field add `sample='1'`

```xml
<tree decoration-success="state =='done'" decoration-info="state =='draft'" decoration-danger="state=='in_consultation'" sample='1'>
```

---

## 46. enable editing form tree view

add to the tree view `multi_edit='1'`

```xml
<tree decoration-success="state =='done'" decoration-info="state =='draft'" decoration-danger="state=='in_consultation'" sample='1' multi_edit='1'>
```

## 47. change the state in the statusbar via a button

* u could search in odoo for, action_done, action_cancel... etc

1. add buttons in the view with type object
2. create their object actions/methods
3. set their states attribute, when they will be shown

## 48. add hot keys for buttons

add `data-hotkey='z'`, any letter available

## 49. add One2Many field

One2many in One from many

One2many in appointment from pharmacy

One -> appointment

Many -> Pharmacy

0. create the model, we want its many
1. in pharmacy, add a Many2one field with the appointment
2. in appointment, add One2many field and pass field from step 1
3. add the pharmacy One2many field to the view
4. create the tree and form view from one2 many field
5. in this case the product model have been used so we need to add it to the depends in the manifest file

### pharmacy model at the end of custom_addons\hospital\models\appointment.py

```py
class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one(
        'hospital.appointment', string='Appointment')
```

### appointment model in custom_addons\hospital\models\appointment.py

```py
pharmacy_lines_id = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
```

### in custom_addons\hospital\views\appointment_view.xml

```xml
<notebook>
  <page string="Prescription">
    <field name='prescription' placeholder='Enter prescription' options="{'collaborative': true, 'resizable': true}" />
  </page>
  <page string='Pharmacy'>
    <field name="pharmacy_lines_id">
      <tree editable='bottom'>
        <field name="product_id" />
        <field name="price_unit" />
        <field name="qty" />
      </tree>
      <form>
        <group>
          <field name="product_id" />
          <field name="price_unit" />
          <field name="qty" />
        </group>
      </form>
    </field>
  </page>
</notebook>
```

### in custom_addons\hospital\_*manifest*_.py

```py
'depends': ['mail', 'product'],
```

---

## 50. editable attribute in the tree tag

1. without the editable, when adding a new line will show a pop up of the form
2. top, will fill the data at the top of the list/tree
3. bottom, will fill the data at the bottom of the list/tree

## 51. colum inviable based on value in the model, all xml

1. add boolean field
2. add attrs attribute to the field will be hidden
3. add the condition of hide

```xml
</page>
  <page string='Pharmacy'>
    <field name="pharmacy_lines_id">
      <tree editable='bottom'>
        <field name="product_id" />
        <field name="price_unit" attrs="{ 'column_invisible':[('parent.hide_sales_price','=',True)] }" />
        <field name="qty" />
      </tree>
      <form>
        <group>
          <field name="product_id" />
          <field name="price_unit" attrs="{ 'column_invisible':[('parent.hide_sales_price','=',True)] }" />
          <field name="qty" />
        </group>
      </form>
    </field>
  </page>
```

## 52. show only in the developer mode

add `groups="base.group_no_one"` to the field u wanna hide

## 53. image field

in custom_addons\hospital\models\patient.py

```py
image = fields.Image(string='Image')
```

in custom_addons\hospital\views\patient_view.xml

```xml
<sheet>
  <field name="image" widget='image' class="oe_avatar" />
  <group>
    <group>
      <field name="name" />
      <field name="dob" />
      <field name="age" />
    </group>
```

## 54. create tags model and use boolean_toggle widget

to create a model, will deal with 6 files:

1. MyModel.py, patient_tag.py

   ```py
   from email.policy import default

    from odoo import api, fields, models

    class PatientTag(models.Model):
        _name = 'patient.tag'
        _description = 'Patient Tag'

        name = fields.Char(
            string='Name',
            required=True
        )
        active = fields.Boolean(
            string='Active',
            default=True
        )

   ```

2. my_view.xml, patient_tag_view.xml

   ```xml
    <?xml version='1.0' encoding='utf-8'?>
    <odoo>
      <record model="ir.ui.view" id="view_patient_tag_tree">
        <field name="name">Patient Tags</field>
        <field name="model">patient.tag</field>
        <field name="arch" type="xml">
          <tree sample='1'>
            <field name="name" string="Tag Name" />
          </tree>
        </field>
      </record>

      <record model="ir.ui.view" id="view_patient_tag_form">
        <field name="name">Patient Tags</field>
        <field name="model">patient.tag</field>
        <field name="arch" type="xml">
          <form>
            <sheet>
              <group>
                <group>
                  <field name="name" />
                </group>
                <group>
                  <field name="active" widget="boolean_toggle" />
                </group>
              </group>
            </sheet>
          </form>
        </field>
      </record>

      <record id="action_patient_tag" model="ir.actions.act_window">
        <field name="name">Tags</field>
        <field name="type">ir.actions.act_window</field>
        <field name="res_model">patient.tag</field>
        <field name="view_mode">tree,form</field>
        <field name="context"></field>
        <field name="help" type='html'>
          <p class='o_view_nocontent_smiling_face'>
                Create your first tag!
          </p>
        </field>
      </record>

      <menuitem id="menu_patient_tag" name="Tags" action="action_patient_tag" parent="menu_configuration_main" />

    </odoo>
   ```

3. menu.py

   ```xml
     <menuitem id="menu_configuration_main" name="Configuration" sequence="20" parent="menu_hospital_main" />
   ```

4. __init\__.py

   ```py
   from . import models
   from . import patient
   from . import appointment
   from . import patient_tag
   ```

5. __manifest\__.py

   ```py
   'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/female_patient_view.xml',
        'views/patient_tag_view.xml',
    ],
   ```

6. ..access.csv

   ```py
   hospital.access_patient_tag,access_patient_tag,hospital.model_patient_tag,base.group_user,1,1,1,1
   ```

## 55->58 adding Many2many colored field

1. create color field, two types:
   1. char: more options
   2. integer: some given colors
2. add the fields to the view
3. in patient.py add many2many field, will crete a separate table
4. in patient view add many2many field, with options attribute and many2many_tag widget

in custom_addons\hospital\models\patient_tag.py

```py
color = fields.Integer(
    string='Color',
)

color2 = fields.Char(
    string='Color2',
)
```

in custom_addons\hospital\views\patient_tag_view.xml

```xml
<field name="color" widget="color" />
<field name="color2" widget="color_picker" groups="base.group_no_one" />
```

in custom_addons\hospital\models\patient.py

```py
tag_ids = fields.Many2many(
    string='Tag',
    comodel_name='patient.tag'
)
```

in tree and form view custom_addons\hospital\views\patient_view.xml

```xml
<field name="tag_ids" widget="many2many_tags" options="{'color_field': 'color'}" />
```

## 59. add activity view to the appointment

1. create the view
2. don't for get to add it to the `view_mode`

```xml
<record model="ir.ui.view" id="view_hospital_appointment_activity">
  <field name="name">hospital.appointment.activity</field>
  <field name="model">hospital.appointment</field>
  <field name="arch" type="xml">
    <activity string='Appointment'>
      <field name="patient_id" />
      <field name="ref" />
      <templates>
        <div t-name="activity-box">
          <img t-att-src="activity_image('hospital.patient','image',record.patient_id.raw_value)" t-att-title="record.patient_id.value" t-att-alt="record.patient_id.value" />
          <div>
            <field name="ref" />
          </div>
        </div>
      </templates>
    </activity>
  </field>
</record>
```

```xml
<record id="action_hospital_appointment" model="ir.actions.act_window">
    <field name="name">Appointments</field>
    <field name="type">ir.actions.act_window</field>
    <field name="res_model">hospital.appointment</field>
    <field name="view_mode">tree,form,activity</field>
    <field name="context">{}</field>
    <field name="help" type='html'>
      <p class='o_view_nocontent_smiling_face'>
            Create your first appointment!
      </p>
    </field>
</record>
```

## 60. enable the html code

suppose passing `codeview':true` in options attribute will make it work but for me it did not work

in prescription field in custom_addons\hospital\views\appointment_view.xml

```xml
<field name='prescription' placeholder='Enter prescription' options="{'collaborative': true, 'resizable': true,'codeview':true}" />
```

## 61+62. transient model

* for temporarily data usage

1. create dir. wizard
2. import wizard in main __init\__.py file
3. create its own __init\__.py file
4. create the my_model.py/cancel_appointment.py
5. define it in the ..access.csv
6. create my_model_wizard.xml/cancel_appointment_wizard.xml, will keep
7. create the the menu window action, and keep it in menu.xml, because step 8
8. add the relative path to __manifest\__.py, wizards added before the views and after security
9. make the form as a pop up, `target`
10. editing the default footer

### init files

custom_addons\hospital\wizard\_*init*_.py

```py
from . import cancel_appointment
```

custom_addons\hospital\_*init*_.py

```py
from . import controllers
from . import models
from . import wizard
```

### manifest file, they loaded by their order

```py
'data': [
    'security/ir.model.access.csv',
    'wizard/cancel_appointment_wizard.xml',
    'views/menu.xml',
    'views/patient_view.xml',
    'views/appointment_view.xml',
    'views/female_patient_view.xml',
    'views/patient_tag_view.xml',
]
```

### menu.py, custom_addons\hospital\views\menu.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <menuitem id="menu_hospital_main" name="Hospital" sequence="0" web_icon="hospital,static\description\icon.png" />
  <menuitem id="menu_patient_main" name="Patient Details" sequence="0" parent="menu_hospital_main" />
  <menuitem id="menu_appointment_main" name="Appointment Details" sequence="20" parent="menu_hospital_main" />
  <menuitem id="menu_configuration_main" name="Configuration" sequence="20" parent="menu_hospital_main" />
  <menuitem id="menu_cancel_appointment" action='action_cancel_appointment_wizard' name="Cancellation" sequence="10" parent="menu_appointment_main" />
</odoo> 
```

### Security

```py
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
hospital.access_hospital_patient,access_hospital_patient,hospital.model_hospital_patient,base.group_user,1,1,1,1
hospital.access_hospital_appointment,access_hospital_appointment,hospital.model_hospital_appointment,base.group_user,1,1,1,1
hospital.access_appointment_pharmacy_lines,access_appointment_pharmacy_lines,hospital.model_appointment_pharmacy_lines,base.group_user,1,1,1,1
hospital.access_patient_tag,access_patient_tag,hospital.model_patient_tag,base.group_user,1,1,1,1
hospital.access_cancel_appointment_wizard,access_cancel_appointment_wizard,hospital.model_cancel_appointment_wizard,base.group_user,1,1,1,1
```

### the model, custom_addons\hospital\wizard\cancel_appointment.py

```py
from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one(
        string='Appointment',
        comodel_name='hospital.appointment'
    )

    def action_cancel(self):
        return
```

### the view, custom_addons\hospital\wizard\cancel_appointment_wizard.xml

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <record model="ir.ui.view" id="view_cancel_appointment_form">
    <field name="name">cancel.appointment.wizard.form</field>
    <field name="model">cancel.appointment.wizard</field>
    <field name="arch" type="xml">
      <form>
        <group>
          <group>
            <field name="appointment_id" />
          </group>
          <group></group>
        </group>
        <footer>
          <button string="Cancel Appointment" type="object" class="btn-primary" name="action_cancel" data-hotkey="q" />
          <button string="Discard" spacial="cancel" class="btn-secondary" data-hotkey="z" />
        </footer>
      </form>
    </field>
  </record>

  <record id="action_cancel_appointment_wizard" model="ir.actions.act_window">
    <field name="name">Cancel Appointment</field>
    <field name="type">ir.actions.act_window</field>
    <field name="res_model">cancel.appointment.wizard</field>
    <field name="view_mode">form</field>
    <field name="context"></field>
    <field name="target">new</field>
  </record>

</odoo>
```

## 63. text field

in custom_addons\hospital\wizard\cancel_appointment.py

```py
    reason = fields.Text(
        string='Reason',
    )
```

in custom_addons\hospital\wizard\cancel_appointment_wizard.xml

```xml
<group>
  <field name="appointment_id" />
  <field name="reason" />
</group>
```

## 64. use buttons to get an affect form anther model/ lunch wizard form a button

in custom_addons\hospital\views\appointment_view.xml

```xml
<!-- button type action -->
<!-- <button type='action' data-hotkey='n' name="%(action_cancel_appointment_wizard)d" string='Cancel' states='in_consultation,draft' /> -->
<!-- button type object -->
<button type='object' data-hotkey='n' name="action_cancel" string='Cancel' states='in_consultation,draft' />
```

in custom_addons\hospital\models\appointment.py

```py
# def action_cancel(self):
#     for rec in self:
#         rec.state = 'cancel'

def action_cancel(self):
    action = self.env.ref(
        'hospital.action_cancel_appointment_wizard').read()[0]
    return action
```

## 65+66. load data from xml file

1. create 'data' dir.
2. create my_model_data.xml/patient_tag_data file
3. create my.model.csv/patient.tag.csv file
4. add it to manifest file after security

__notice__: the naming is important, patient_tag.csv causes an error, it can not find the model, while patient.tag.csv not

in custom_addons\hospital\_*manifest*_.py

```py
'data': [
    'security/ir.model.access.csv',
    'data/patient_tag_data.xml',
    'wizard/cancel_appointment_wizard.xml',
    'views/menu.xml',
```

in custom_addons\hospital\data\patient_tag_data.xml

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>

  <record id="patient_tag_vip" model="patient.tag">
    <field name="name">VIP</field>
  </record>

  <record id="patient_tag_kid" model="patient.tag">
    <field name="name">KID</field>
  </record>

  <record id="patient_tag_kid" model="patient.tag">
    <field name="name">Master</field>
    <field name="active" eval="False" />
  </record>

</odoo>
```

in custom_addons\hospital\data\patient.tag.csv

```csv
id,name,active
patient_tag_ASAP,ASAP,True
patient_tag_NASAP,NASAP,False
```

## 67. scaffold command

to create odoo model using command line

where u can find the odoo-bin file use this command `python odoo-bin scaffold :my_model :my_path`

`python odoo-bin scaffold om_inheritance C:\Users\bashr\odoo\odoo\custom_addons\`

## 68+69. inheritance, adding field

1. my_inherited_model.py
2. init file
3. manifest file
4. add a field to an inherited view

__my_inherited_model.py__, in custom_addons\om_inheritance\models\sale_order.py:

```py
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one(
    string='Confirmed User',
    comodel_name='res.users',
    )
```

__init file__,  custom_addons\om_inheritance\models\_*init*_.py

```py
from . import sale_order
```

__manifest file__, custom_addons\om_inheritance\_*manifest*_.py

```py
# any module necessary for this one to work correctly
'depends': ['sale'],

# always loaded
'data': [
    # 'security/ir.model.access.csv',
    'views/sale_order_view.xml',
    'views/templates.xml',
],
```

__my_inherited_view__, custom_addons\om_inheritance\views\sale_order_view.xml

```xml
<odoo>
  <data>

    <record id="view_order_form_inherit" model="ir.ui.view">
      <field name="name">sale.order.inherit</field>
      <field name="model">sale.order</field>
      <field name="inherit_id" ref="sale.view_order_form" />
      <field name="arch" type="xml">

        <xpath expr="//field[@name='payment_term_id']" position="after">

          <field name="confirmed_user_id" />

        </xpath>

      </field>
    </record>


  </data>
</odoo>
```

## 70. inherit a function

1. add inherited function to my_inherited_model.py,
    * __REMEMBER__ where u place the super will be affected by the execution sequence of python

inherit function __syntax__:

```py
def action_inherit(self,arg1,arg2):
  # to_do before the execution of the inherited function
  super(MyModel,self).action_inherit(arg1,arg2)
  # to_do after the execution of the inherited function
  # if u dint place the super line, this function (action_inherit) will get executed not the inherited one!!!!
```

in custom_addons\om_inheritance\models\sale_order.py

```py
def action_confirm(self):
    super(SaleOrder, self).action_confirm()
    print('Hi, I am working!! ..................')
    self.confirmed_user_id = self.env.user.id
```
