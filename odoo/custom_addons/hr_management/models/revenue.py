from odoo import models, fields, api
from datetime import date

class Revenue(models.Model):
    _name = 'revenue.management'
    _description = 'Revenue Management'

    date = fields.Date(
        string='Revenue Date',
        required=True,
        default=date.today
    )

    amount = fields.Float(
        string='Amount',
        required=True,
        default=0.0
    )

    description = fields.Text(
        string='Description'
    )

    # ============================
    # Tính tổng doanh thu
    # ============================
    @api.model
    def total_revenue(self, start_date, end_date):
        """Tính tổng doanh thu giữa 2 ngày."""
        records = self.search([
            ('date', '>=', start_date),
            ('date', '<=', end_date)
        ])
        return sum(records.mapped('amount'))
