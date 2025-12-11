from odoo import models, fields

class Book(models.Model):
    _name = 'book'
    _description = 'Book'

    title = fields.Char(
        string='Title',
        required=True
    )

    author = fields.Char(
        string='Author',
        required=True
    )

    price = fields.Float(
        string='Price',
        required=True,
        default=0.0
    )

    publish_date = fields.Date(
        string='Publish Date'
    )
