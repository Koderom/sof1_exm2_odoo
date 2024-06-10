{
    'name': "Gestion academica",
    'depends':[
        'hr'
    ],
    'data' : [
        'security/ir.model.access.csv',
        
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
    'application': True
}