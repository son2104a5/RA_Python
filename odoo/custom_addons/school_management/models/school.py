from odoo import models, fields, api

class School(models.Model):
    _name = 'school.management.school'
    _description = 'School'

    name = fields.Char(string='School Name', required=True)
    location = fields.Char(string='Location')
    start_date = fields.Date(string='Start Date')

    # One2many to students and exams
    student_ids = fields.One2many(
        comodel_name='school.management.student',
        inverse_name='school_id',
        string='Students'
    )
    exam_ids = fields.One2many(
        comodel_name='school.management.exam',
        inverse_name='school_id',
        string='Exams'
    )

    # Convenience create/update wrappers (optional)
    @api.model
    def create_school(self, vals):
        """Tạo mới trường học (wrapper)."""
        return self.create(vals)

    def update_school(self, vals):
        """Cập nhật thông tin trường học (wrapper)."""
        return self.write(vals)
