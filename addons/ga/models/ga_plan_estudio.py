from odoo import fields, models
class PlanEstudio(models.Model):
    _name = "ga.plan.estudio"
    _description = "GA plan estudio"
    horas = fields.Integer()
    materia_id = fields.Many2one("ga.materia", string="Materia", required=True)
    gestion_id = fields.Many2one("ga.gestion", string="Gestion", required=True)
    grado_id = fields.Many2one("ga.grado", string="Grado academico",required=True)
    paralelo_profesor_ids = fields.One2many("ga.paralelo.profesor","plan_estudio_id", string="Asignacion profesor")