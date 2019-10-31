# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TitreParticipation(models.Model):
    _name = 'titre.participation'
    _description = 'TITRE DE PARTICIPATION'

    name = fields.Char(string=u"Nom",default="TABLEAU DES TITRES DE PARTICIPATION",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    titre_participation_line_ids = fields.One2many(comodel_name="titre.participation.line",
                                                   inverse_name="titre_participation_id", string="Lignes",
                                                   required=False, copy=True)
    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class TitreParticipationLine(models.Model):
    _name = 'titre.participation.line'
    _description = 'LIGNES DES TITRES DE PARTICIPATION'

    name = fields.Char(string=u"Raison sociale de la Société émettrice",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    secteur_activite = fields.Char(string=u"Secteur d'activité",required=False,)
    capital_social = fields.Float(string=u"Capital social",  required=False, )
    participation_capital = fields.Float(string=u"Participation au capital en %",  required=False, )
    prix_acquisition = fields.Float(string=u"Prix d'acquisition global",  required=False, )
    valeur_comptable_nette = fields.Float(string=u"Valeur comptable nette",  required=False, )
    date_cloture = fields.Date(string=u"Date de cloture" ,required=False, )
    situation_nette = fields.Float(string=u"Situation nette",  required=False, )
    resultat_net = fields.Float(string=u"Résultat net",  required=False, )
    produits_inscrits = fields.Float(string=u"Produits inscrits au C.P.C de l'exercice",  required=False, )
    titre_participation_id = fields.Many2one(comodel_name="titre.participation", string="Titre Participation", required=False, )