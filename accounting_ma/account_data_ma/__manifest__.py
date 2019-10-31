# -*- encoding: utf-8 -*-


{
    'name': u'Données de base de la comptabilité Marocaine',
    'version': '1.0',
    'summary': u'Plan comptable, Types de comptes, Taxes',
    'author': 'Andema',
    'website': 'http://www.andemaconsulting.com',
    "depends": [
        'account','account_tax_code',
    ],
    'data': [
        'data/account_chart_data.xml',
        "data/account.account.type.csv",
        "data/account.account.template.csv",
        "data/account.tax.template.csv",
        'data/account_chart_data_final.xml',
        'data/account_chart_template_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
