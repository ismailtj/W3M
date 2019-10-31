# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CalculImpot(models.Model):
    _name = 'calcul.impot'
    _description = 'TABLEAU DE CALCUL DES IMPOTS'

    name = fields.Char(string=u"Nom",default="TABLEAU DE CALCUL DES IMPOTS",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    calcul_impot_line_ids = fields.One2many(comodel_name="calcul.impot.line", inverse_name="calcul_impot_id",
                                            string="Lignes", required=False, copy=True, )
    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class CalculImpotLine(models.Model):
    _name = 'calcul.impot.line'
    _description = 'LIGNES TABLEAU DE CALCUL DES IMPOTS'

    name = fields.Char(string=u"Rubrique",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    ens_produit = fields.Float(string=u"Ensemble des produits")
    ens_produit_base_imposable = fields.Float(string=u"Ensemble des produits base imposable")
    ens_produit_numerateur_taxable = fields.Float(string=u"Ensemble des produits numerateur taxable")
    calcul_impot_id = fields.Many2one(comodel_name="calcul.impot", string="Impot", required=False, )