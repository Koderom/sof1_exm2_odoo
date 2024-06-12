from odoo import fields, models
class Profesor(models.Model):
    _inherit="hr.employee"
    codigo = fields.Char(string="Codigo profesor")
    unidad_educativa_id = fields.Many2one("ga.unidad.educativa", string="Profesor", required=False)
    paralelo_profesor_ids = fields.One2many("ga.paralelo.profesor", "profesor_id", string="Asignacion profesor")