from odoo import fields, models
class UnidadEducativa(models.Model):
    _name="ga.unidad.educativa"
    _description="UnidadEducativa"
    codigo = fields.Char(required=True)
    descripcion = fields.Text(string="Nombre")
    latitud = fields.Float()
    longitud = fields.Float()