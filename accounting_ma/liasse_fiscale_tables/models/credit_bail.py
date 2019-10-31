# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CreditBail(models.Model):
    _name = 'credit.bail'
    _description = 'TABLEAU DES BIENS EN CREDIT BAIL'

    name = fields.Char(string=u"Nom",default="TABLEAU DES BIENS EN CREDIT BAIL", required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal', copy=False)
    credit_bail_line_ids = fields.One2many(comodel_name="credit.bail.line", inverse_name="credit_bail_id",
                                           string="Lignes", required=False, copy=True)

    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class CreditBailLine(models.Model):
    _name = 'credit.bail.line'
    _description = 'LIGNES TABLEAU DES BIENS EN CREDIT BAIL'

    name = fields.Char(string=u"Rubrique",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    date_premiere_echeance = fields.Date(string=u"Date de la 1ère échéance",required=False, )
    duuree_contrat = fields.Integer(string=u"Durée du contrat en mois", required=False, )
    valeur_estimee = fields.Float(string=u"Valeur estimée du bien à la date du contrat",  required=False, )
    duuree_theorique = fields.Integer(string=u"Durée théorique d'amortissement du bien", required=False, )
    cumul_redevance = fields.Float(string=u"Cumul des exercices précedents des redevances", required=False, )
    montant_redevance = fields.Float(string=u"Montant de l'exercice des redevances", required=False, )
    redevance_restant_moins = fields.Float(string=u"Redevances restant à payer A moins d'un an", required=False, )
    redevance_restant_plus = fields.Float(string=u"Redevances restant à payer A plus d'un an", required=False, )
    prix_achat_fin_contrat = fields.Float(string=u"Prix d'achat résiduel en fin de contrat",  required=False, )
    observations = fields.Text(string=u"Observations", required=False, )
    credit_bail_id = fields.Many2one(comodel_name="credit.bail", string="Credit bail", required=False, )