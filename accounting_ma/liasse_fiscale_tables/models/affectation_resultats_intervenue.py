# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AffectationResultatsIntervenue(models.Model):
    _name = 'affectation.resultats.intervenue'
    _description = 'AFFECTATION DES RESULTATS INTERVENUE'

    name = fields.Char(string=u"Nom",default="ETAT D'AFFECTATION DES RESULTATS INTERVENUE AU COURS DE L'EXERCICE",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    affectation_resultats_intervenue_line1_ids = fields.One2many(comodel_name="affectation.resultats.intervenue.line1",
                                                                 inverse_name="affectation_resultats_intervenue_id",
                                                                 string="Lignes1", required=False, copy=True)
    affectation_resultats_intervenue_line2_ids = fields.One2many(comodel_name="affectation.resultats.intervenue.line2",
                                                                 inverse_name="affectation_resultats_intervenue_id",
                                                                 string="Lignes2", required=False, copy=True)

    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class AffectationResultatsIntervenueLine1(models.Model):
    _name = 'affectation.resultats.intervenue.line1'
    _description = 'LIGNES AFFECTATION DES RESULTATS INTERVENUE 1'

    name = fields.Char(string=u"Nom, prénoms ou raison sociale des principaux associés",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    montant = fields.Float(string=u"Montant",  required=False, )
    affectation_resultats_intervenue_id = fields.Many2one(comodel_name="affectation.resultats.intervenue", string="AFFECTATION DES RESULTATS INTERVENUE", required=False, )

class AffectationResultatsIntervenueLine2(models.Model):
    _name = 'affectation.resultats.intervenue.line2'
    _description = 'LIGNES AFFECTATION DES RESULTATS INTERVENUE 2'

    name = fields.Char(string=u"Nom, prénoms ou raison sociale des principaux associés",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    montant = fields.Float(string=u"Montant",  required=False, )
    affectation_resultats_intervenue_id = fields.Many2one(comodel_name="affectation.resultats.intervenue", string="AFFECTATION DES RESULTATS INTERVENUE", required=False, )