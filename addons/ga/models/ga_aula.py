from odoo import fields, models
class Aula(models.Model):
    _name="ga.aula"
    _description="Aula"
    _order = 'descripcion'

    codigo=fields.Char(required=True)
    descripcion=fields.Text()
    capacidad=fields.Integer()