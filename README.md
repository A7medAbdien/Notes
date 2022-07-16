# Odoo

The videos:

1. [installation](https://youtu.be/eD12tbz6BC4)
2. [setup the environment](https://youtu.be/LS8tdWoiOQQ)

## Usefully commands

`python odoo-bin -d odoo15 -r odoo -w odoo`

`python odoo-bin scaffold myFirstModule addons\`

`git commit -am "git commit -a --allow-empty-message -m ''"`

## Notes from the [playlist](https://youtube.com/playlist?list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU)

### `__manifest__.py` file

* "application": True
* "sequence": -100

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
import string
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
