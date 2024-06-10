from odoo import http
from odoo.http import request, route
import json

class GestionController(http.Controller):
    @http.route('/api/gestion', auth='public', type='http', methods=['GET'], csrf=False, website=True)
    def get_gestiones(self, **kw):
        gestiones = request.env['ga.gestion'].sudo().search([])
        gestiones_data = [{
            'codigo': gestion.codigo,
        } for gestion in gestiones]
        return json.dumps(gestiones_data)