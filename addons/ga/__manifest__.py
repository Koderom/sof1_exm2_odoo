{
    'name': 'Gestion Academica',
    'version': '1.0',
    'category': 'CRM',
    'license': 'AGPL-3',
    'description': """
        Este es un modulo para la gestion de diferentes academia de enseñanza
    """,
    'author': 'Gestion Academica',
    'website': 'ga',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/ga_inscripcion_views.xml',
        'data/ga.gestion.csv',
        'data/ga.nivel.csv',
        'data/ga.grado.csv',
        'data/ga.materia.csv',
        'data/ga.aula.csv',
        'data/ga.paralelo.csv',

        'views/ga_gestion_views.xml',
        'views/ga_unidad_educativa_views.xml',
        'views/ga_materia_views.xml',
        'views/ga_plan_estudio_views.xml',
        'views/ga_menu_views.xml'
       
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}