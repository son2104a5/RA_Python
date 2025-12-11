from odoo import models, fields

class Demo(models.Model):
    _name = 'demo_hello'
    _description = 'Demo Model for Hello World Addon'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')