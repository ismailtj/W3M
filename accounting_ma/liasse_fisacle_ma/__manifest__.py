# -*- encoding: utf-8 -*-
{
    'name': u'Données de la liasse fiscale Marocaine',
    'version': '1.0',
    'author': 'Andema',
    'website': 'http://www.andemaconsulting.com',
    "depends": [
        'odoo_excel_engin','liasse_fiscale_tables',
    ],
    'data': [
        'data/init_data.xml',
        "data/formulas.engine.csv",
        "data/report.list.formulas.csv",
        "data/report.pyhton.edi.csv",
        "data/report.engin.csv",
        "data/report.group.csv",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
