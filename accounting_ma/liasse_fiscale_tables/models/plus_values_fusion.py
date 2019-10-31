# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PlusValuesFusion(models.Model):
    _name = 'plus.values.fusion'
    _description = 'PLUS VALUES CONSTATEES EN CAS DE FUSION'

    name = fields.Char(string=u"Nom", default="ETAT DES PLUS-VALUES CONSTATEES EN CAS DE FUSION", required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    plus_values_fusion_line_ids = fields.One2many(comodel_name="plus.values.fusion.line",
                                                  inverse_name="plus_values_fusion_id", string="Lignes", required=False,
                                                  copy=True, )
    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class PlusValuesFusionLine(models.Model):
    _name = 'plus.values.fusion.line'
    _description = 'LIGNES PLUS VALUES CONSTATEES EN CAS DE FUSION'

    name = fields.Char(string=u"Eléments",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    valeur_apport = fields.Float(string=u"Valeur d'apport", required=False, )
    valeur_nette_comptable = fields.Float(string=u"Valeur nette comptable",  required=False, )
    plus_value_constatee = fields.Float(string=u"Plus-value constatée et différée",  required=False, )
    fraction_exercice_ant = fields.Float(string=u"Fraction de la plus-value rapportée aux exercices antérieurs(cumul)",  required=False, )
    fraction_exercice_actuel = fields.Float(string=u"Fraction de la plus-value rapportée à l'exercice actuel",  required=False, )
    cumul_plus_value_rapportee = fields.Float(string=u"Cumul des plus-value rapportées",  required=False, )
    solde_plus_value_non_rapportee = fields.Float(string=u"Solde des plus-values non-imputées",  required=False, )
    observations = fields.Text(string="Observations", required=False, )
    plus_values_fusion_id = fields.Many2one(comodel_name="plus.values.fusion", string="PLUS-VALUES CONSTATEES EN CAS DE FUSION", required=False, )