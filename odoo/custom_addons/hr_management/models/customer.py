from odoo import models, fields

class Customer(models.Model):
    _name = 'estate.customer'
    _description = 'Customer'

    name = fields.Char(string='Customer Name', required=True)

    property_ids = fields.One2many(
        comodel_name='estate.property',
        inverse_name='customer_id',
        string='Properties'
    )
