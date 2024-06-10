from odoo import fields, models
class ParaleloProfesor(models.Model):
    _name="ga.paralelo.profesor"
    _description="ParaleloProfesor"

    profesor_id = fields.Many2one("hr.employee", string="Profesor", required=True)
    aula_id = fields.Many2one("ga.aula", string="Aula", required=True)
    aula_codigo = fields.Char(related='aula_id.codigo')
    paralelo_id = fields.Many2one("ga.paralelo", string="Paralelo", required=True)
    plan_estudio_id=fields.Many2one("ga.plan.estudio", string="Plan Estudio", required=True)
    paralelo_profesor_dias_ids=fields.One2many("ga.paralelo.profesor.dias", "paralelo_profesor_id", string="Dias de clase")
