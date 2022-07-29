{
    'name': "LMS (MLTrucking)",
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
        'views/assets/sequence.xml',
        'views/datas/freight_type.xml',
        'views/datas/operation_type.xml',
        'views/datas/operation_status.xml',
        'views/datas/services_type.xml',
        'views/layouts/menu.xml',
        'views/models/general.xml',
        'views/models/order.xml',
        'views/models/package.xml'
    ],
    'demo': [
        'demo/general_status.xml',
        'demo/freight_ types.xml',
        'demo/operation_types.xml'
    ],
    "installable": True,
    "application": True,
}
