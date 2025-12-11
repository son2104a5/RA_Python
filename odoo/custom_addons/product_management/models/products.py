from odoo import models, fields

class Product(models.Model):
    _name = 'product.management'
    _description = 'Product Management'

    product_name = fields.Char(
        string='Product Name',
        required=True
    )

    product_price = fields.Float(
        string='Price',
        required=True,
        default=0.0
    )

    product_quantity = fields.Integer(
        string='Quantity',
        required=True,
        default=0
    )
