from odoo import models, fields, api

class Student(models.Model):
    _name = 'school.management.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    school_id = fields.Many2one(
        comodel_name='school.management.school',
        string='School',
        ondelete='cascade'
    )
    score = fields.Float(string='Score', default=0.0)

    # CRUD helpers (optional)
    @api.model
    def create_student(self, vals):
        """Tạo học viên mới và liên kết với school_id (nếu có)."""
        return self.create(vals)

    def update_student(self, vals):
        """Cập nhật thông tin học viên."""
        return self.write(vals)
