from odoo import models, fields
from datetime import date

class Employee(models.Model):
    _name = 'employee.management'
    _description = 'Employee Management'

    name = fields.Char(
        string='Name',
        required=True
    )

    position = fields.Selection(
        selection=[
            ('manager', 'Manager'),
            ('developer', 'Developer'),
            ('hr', 'HR'),
        ],
        string='Position',
        required=True
    )

    salary = fields.Float(
        string='Salary',
        default=1000.0,
        required=True
    )

    start_date = fields.Date(
        string='Start Date',
        default=date.today
    )
