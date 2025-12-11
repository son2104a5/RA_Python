from odoo import models, fields, api
from odoo.exceptions import UserError

class Exam(models.Model):
    _name = 'school.management.exam'
    _description = 'Exam'

    exam_date = fields.Date(string='Exam Date', required=True)
    subject = fields.Char(string='Subject', required=True)
    school_id = fields.Many2one(
        comodel_name='school.management.school',
        string='School',
        ondelete='cascade'
    )
    student_ids = fields.Many2many(
        comodel_name='school.management.student',
        relation='exam_student_rel',
        column1='exam_id',
        column2='student_id',
        string='Students'
    )

    average_score = fields.Float(
        string='Average Score',
        compute='_compute_average_score',
        store=True
    )

    @api.depends('student_ids', 'student_ids.score')
    def _compute_average_score(self):
        for rec in self:
            scores = rec.student_ids.mapped('score') or []
            if scores:
                rec.average_score = sum(scores) / len(scores)
            else:
                rec.average_score = 0.0

    # Convenience CRUD and business logic
    @api.model
    def create_exam(self, vals):
        """Tạo exam và trả về record."""
        return self.create(vals)

    def update_exam(self, vals):
        """Cập nhật exam."""
        return self.write(vals)

    def compute_average_between_dates(self, start_date, end_date):
        """
        Trả về dict {exam_id: average_score} cho các kỳ thi của trường
        trong khoảng ngày (filter by exam_date).
        """
        exams = self.search([('exam_date', '>=', start_date), ('exam_date', '<=', end_date)])
        return {e.id: e.average_score for e in exams}
