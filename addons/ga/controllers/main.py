from odoo import http
from odoo.http import request, route
import json, marshal

class GestionController(http.Controller):
    @http.route('/api/gestion', auth='public', type='http', methods=['GET'], csrf=False, website=True)
    def get_gestiones(self, **kw):
        gestiones = request.env['ga.gestion'].sudo().search([])
        gestiones_data = [{
            'codigo': gestion.codigo,
        } for gestion in gestiones]
        return json.dumps(gestiones_data)
    
class ProfesorController(http.Controller):
    @http.route('/ga/profesor/lista-curso-materias',csrf=False,  type='http', auth='public', website=True, methods=['GET'])
    def get_lista_curso_materias(self, **post):
        response_data = {}
        
        body = request.httprequest.data
        data = json.loads(body)
        codigo_profesor = data.get('codigoPersona')
        profesor = request.env['hr.employee'].sudo().search([('id', '=', codigo_profesor)])
        
        response_data["profesor"] = {}
        if len(profesor) > 0:
            paralelo_profesores = request.env['ga.paralelo.profesor'].sudo().search([('profesor_id', '=', profesor.id)])
            grados = request.env['ga.grado'].sudo().search([])
            cursos_data = []
            for grado in grados:
                if not grado.exists(): continue
                for p_profesor in paralelo_profesores:
                    if not p_profesor.exists(): continue
                    plan_estudios = request.env['ga.plan.estudio'].sudo().search(
                        [('id', '=', p_profesor.plan_estudio_id.id),('grado_id', '=', grado.id)]
                    )
                    if not plan_estudios.exists(): continue
                    materias_data = []
                    for p_estudio in plan_estudios:
                        if not p_estudio.exists(): continue
                        materia = request.env['ga.materia'].sudo().search([('id', '=', p_estudio.materia_id.id)])
                        materias_data.append({
                            'materiaId': materia.id,
                            'nombreMateria':materia.descripcion
                        })

                    nivel = request.env['ga.nivel'].sudo().search([('id', '=', grado.nivel_id.id)])
                    paralelo = request.env['ga.paralelo'].sudo().search([('id', '=', p_profesor.paralelo_id.id)])
                    
                    cursos_data.append({
                        'cursoId': grado.id,
                        'nombreCurso': '{} {} de {}'.format(grado.descripcion, paralelo.descripcion, nivel.descripcion),
                        'materias': materias_data
                    })

            # datos del profesor
            response_data["profesor"] = {
                'id':profesor[0].id,
                'nombre':profesor[0].name,
                'cursos' : cursos_data
            }
        return json.dumps(response_data)
        
    