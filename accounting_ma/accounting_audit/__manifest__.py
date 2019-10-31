# -*- coding: utf-8 -*-

{
    'name': u'Tests de Cohérence',
    'version': '1.0',
    'author': 'Andema',
    'website': 'http://www.andemaconsulting.com',
    "depends": [
         'odoo_excel_engin'
    ],
    'data': [
        'security/accounting_audit.xml',
        'security/ir.model.access.csv',
        "views/audit.xml",
        "wizard/print_report.xml",
        ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
