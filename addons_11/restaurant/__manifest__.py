# -*- coding: utf-8 -*-

{
    'name': 'Gestion des restaurants',
    'version': '1.0',
    'author': 'Gharib & salah',
    'website': 'https://www.emsi.ma',
    'support': 'elhasnaoui.soukaina@gmail.com',
    'license': "AGPL-3",
    'complexity': 'easy',
    'sequence': 1,
    'category': 'category',
    'description': """
        ce module permet la gestion de la restauration:
           
    """,
    'depends': ['mail','base'],
    'summary': 'plat, Restau, ',
    'data': [
        #'security/ModuleName.xml',
        #'security/ir.model.access.csv',
        #'data/ModuleName_data.xml',
        '/home/emsi/Desktop/eclipse/workspace/exam_addons/addons_11/restaurant/views/restaurant_views.xml',
        '/home/emsi/Desktop/eclipse/workspace/exam_addons/addons_11/restaurant/menu.xml',
    ],
    'demo': [
        #'demo/ModuleName_demo.xml'
    ],
    'css': [
        #'static/src/css/ModuleName_style.css'
    ],
    
    'price': 100.00,
    'currency': 'EUR',
    'installable': True,
    'application': True,
}
