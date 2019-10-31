# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InteretsEmprunts(models.Model):
    _name = 'interets.emprunts'
    _description = 'ETAT DES INTERETS DES EMPRUNTS'

    name = fields.Char(string=u"Nom",default="ETAT DES INTERETS DES EMPRUNTS CONTRACTES AUPRES DES ASSOCIES ET DES TIERS",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    interets_emprunts_line_ids = fields.One2many(comodel_name="interets.emprunts.line",
                                                 inverse_name="interets_emprunts_id", string="Lignes", required=False,
                                                 copy=True, )
    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class InteretsEmpruntsLine(models.Model):
    _name = 'interets.emprunts.line'
    _description = 'LIGNES ETAT DES INTERETS DES EMPRUNTS'

    type = fields.Selection([
        ('a', u'Associés'),
        ('b', u'Tiers'),
    ],
        string="Type", required = True)
    name = fields.Char(string=u"Nom prénoms ou raison sociale",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    adresse = fields.Char(string=u"Adresse",required=True,)
    cin = fields.Char(string=u"N° C.I.N.ou Article I.S.",required=True,)
    montant_pret = fields.Float(string=u"Montant du prêt",  required=False, )
    date_pret = fields.Date(string=u"Date du prêt",required=False, )
    duree_pret = fields.Integer(string=u"Durée du prêt(en mois)", required=False, )
    taux_interet = fields.Float(string=u"Taux d'intérêts",  required=False, )
    charge_financiere = fields.Float(string=u"Charge financière globlale",  required=False, )
    remboursement_exercice_ant_principal = fields.Float(string=u"Remboursement Exercice antérieurs principal",  required=False, )
    remboursement_exercice_ant_intertet = fields.Float(string=u"Remboursement Exercice antérieurs Interêt",  required=False, )
    remboursement_exercice_actuel_principal = fields.Float(string=u"Remboursement Exercice actuel principal",  required=False, )
    remboursement_exercice_actuel_intertet = fields.Float(string=u"Remboursement Exercice actuel Interêt",  required=False, )
    remboursement_exercice_ant = fields.Float(string=u"Remboursement Exercice antérieurs",  required=False, )
    observations = fields.Text(string=u"Observations", required=False, )
    interets_emprunts_id = fields.Many2one(comodel_name="interets.emprunts", string="Interets Emprunts", required=False, )