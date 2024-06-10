from odoo import fields, models
class Materia(models.Model):
    _name = "ga.materia"
    _description = "GA materia"
    codigo = fields.Char(required=True, string="Codigo")
    descripcion = fields.Text(required=True, string="Nombre")