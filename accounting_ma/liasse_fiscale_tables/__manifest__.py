# -*- encoding: utf-8 -*-

{
    'name': u'Tableaux à saisie manuelle de la liasse fiscale Marocaine',
    'version': '1.0',
    'author': 'Andema',
    'website': 'http://www.andemaconsulting.com',
    "depends": [
        'date_range','odoo_excel_engin'
    ],
    'data': [
        "views/credit_bail_view.xml",
        "views/provisions_view.xml",
        "views/titre_participation_view.xml",
        "views/repartition_capital_social_view.xml",
        "views/affectation_resultats_intervenue_view.xml",
        "views/plus_values_fusion_view.xml",
        "views/interets_emprunts_view.xml",
        "views/locations_baux_view.xml",
        "views/detail_stock_view.xml",
        "views/calcul_impot.xml",
        "views/passage.xml",
        "security/liasse_fiscale_tables.xml",
        "security/ir.model.access.csv",
        ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
