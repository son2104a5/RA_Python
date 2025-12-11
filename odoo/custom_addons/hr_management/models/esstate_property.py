from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Property Name', required=True)
    price = fields.Float(string='Price', default=0.0)

    customer_id = fields.Many2one(
        comodel_name='estate.customer',
        string='Customer',
        ondelete='cascade'
    )
