# Odoo

The videos:

1. [installation](https://youtu.be/eD12tbz6BC4)
2. [setup the environment](https://youtu.be/LS8tdWoiOQQ)

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
2. create the "__init__.py" file
3. create a file "patient.py"
4. in the main "__init__.py" add `from . import models`
5. in the models/__init__.py add `from . import patient`

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
2. `\c odoo15` the database name
3. `select * from hospital_patient` the model name

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
