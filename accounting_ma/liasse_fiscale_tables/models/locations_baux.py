# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LocationsBaux(models.Model):
    _name = 'locations.baux'
    _description = 'Locations Baux'

    name = fields.Char(string=u"Nom",default="TABLEAU DES LOCATIONS ET BAUX AUTRES QUE LE CREDIT-BAIL",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    locations_baux_line_ids = fields.One2many(comodel_name="locations.baux.line", inverse_name="locations_baux_id",
                                              string="Lignes", required=False, copy=True, )
    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class LocationsBauxLine(models.Model):
    _name = 'locations.baux.line'
    _description = 'LIGNES Locations Baux'

    name = fields.Char(string=u"Nature du bien loué",required=True,)
    code = fields.Char(string=u"Code",required=True,)
    lieu_situation = fields.Char(string=u"Lieu de Situation",required=False,)
    nom_prenom = fields.Char(string=u"Nom et prénoms ou Raison sociale et adresse du propriétaire",  required=False, )
    date_conclusion = fields.Date(string="Date de conclusion de l'acte de location",required=False, )
    montant_annuel = fields.Float(string="Montant annuel de location",  required=False, )
    montant_loyer = fields.Float(string="Montant du loyer compris dans les charges de l'exercice",  required=False, )
    nature_contrat_bail = fields.Char(string=u"Nature du contrat-Bail-ordinaire", required=False, )
    nature_contrat_period = fields.Char(string=u"(Nème période)", required=False, )
    locations_baux_id = fields.Many2one(comodel_name="locations.baux", string="Locations Baux", required=False, )