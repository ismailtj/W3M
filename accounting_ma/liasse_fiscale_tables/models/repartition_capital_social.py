# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RepartitionCapitalSocial(models.Model):
    _name = 'repartition.capital.social'
    _description = 'ETAT DE REPARTITION DU CAPITAL SOCIAL'

    name = fields.Char(string=u"Nom",default="ETAT DE REPARTITION DU CAPITAL SOCIAL",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    repartition_capital_social_line_ids = fields.One2many(comodel_name="repartition.capital.social.line",
                                                          inverse_name="repartition_capital_social_id", string="Lignes",
                                                          required=False, copy=True)
    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class RepartitionCapitalSocialLine(models.Model):
    _name = 'repartition.capital.social.line'
    _description = 'LIGNES ETAT DE REPARTITION DU CAPITAL SOCIAL'

    name = fields.Char(string=u"Nom, prénoms ou raison sociale des principaux associés",required=True,)
    code = fields.Char(string=u"Code", required=True, )
    adresse = fields.Char(string=u"Adresse",required=False,)
    n_cin = fields.Char(string=u"CIN",required=False,)
    n_if = fields.Char(string=u"IF",required=False,)
    nbre_titre_exe_prec = fields.Integer(string=u"Nbre de titre de l'exercice précedent",  required=False, )
    nbre_titre_exe_actuel = fields.Integer(string=u"Nbre de titre de l'exercice actuel",  required=False, )
    valeur_nominal = fields.Float(string=u"valeur nominal de chaque action ou part sociale",  required=False, )
    montant_capital_souscrit = fields.Float(string=u"Montant du capital souscrit",  required=False, )
    montant_capital_appele = fields.Float(string=u"Montant du capital appelé",  required=False, )
    montant_capital_libere = fields.Float(string=u"Montant du capital Libéré",  required=False, )
    repartition_capital_social_id = fields.Many2one(comodel_name="repartition.capital.social", string="REPARTITION DU CAPITAL SOCIAL", required=False, )