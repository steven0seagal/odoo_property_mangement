
{
    'name': 'Property Management',
    'version': '15.0.1.0.0',
    'summary': 'Property Management',
    'sequence': -99,
    'description': 'Property Management',
    'category': 'Project',
    'website': 'www.example.com',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/property.xml',
        'views/document.xml',
        'views/tenant.xml',
        'views/contract.xml',
        'views/cleaning.xml',
        'views/contractor.xml',
        'views/mainten.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}