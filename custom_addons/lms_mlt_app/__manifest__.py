# -*- coding: utf-8 -*-
{
    'name': "LMS - MLTr",
    'summary': """
        Logistics Management System for MLTrucking LLC""",
    'description': """
        Manage freight services
    """,
    'author': "Battseren - MLH",
    'website': "http://www.mlholding.mn",
    'category': 'Sales',
    'license': 'LGPL-3',
    'version': "15.0.1.0.0",
    'depends': ['base','fleet','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/lms_menu.xml',
        'views/lms_view.xml',
        'views/lms_form.xml',
        'views/lms_sequence.xml',
    ],
    "installable": True,
    "application": True,
}
