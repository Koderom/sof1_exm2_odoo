from odoo import fields, models
class Gestion(models.Model):
    _name = "ga.gestion"
    _description = "GA gestion"
    codigo = fields.Char(required=True)
    descripcion = fields.Text()
    fecha_inicio = fields.Date(string="Fecha inicio")
    fecha_fin = fields.Date(string="Fecha finalizacion")
    ciclo_adacemico_ids = fields.One2many('ga.ciclo.academico', 'gestion_id', string="Ciclos Academicos" )
    plan_estudio_ids = fields.One2many('ga.plan.estudio', 'gestion_id', string="Plan Estudio")