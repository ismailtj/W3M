# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Provisions(models.Model):
    _name = 'provisions'
    _description = 'TABLEAU DES PROVISIONS'

    name = fields.Char(string=u"Nom",default="TABLEAU DES PROVISIONS",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    provisions_line_ids = fields.One2many(comodel_name="provisions.line", inverse_name="provisions_id", string="Lignes",
                                          required=False, copy=True)
    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class ProvisionsLine(models.Model):
    _name = 'provisions.line'
    _description = 'LIGNES TABLEAU DES PROVISIONS'

    code = fields.Char(string=u"Code",required=True,)
    name = fields.Char(string=u"Nature",required=True,)
    montant_debut = fields.Float(string=u"Montant début exercice",  required=False, )
    dotation_exploitation = fields.Float(string=u"Dotation d'exploitation",  required=False, )
    dotation_financiere = fields.Float(string=u"Dotation financières",  required=False, )
    dotation_non_courante = fields.Float(string=u"Dotation Non courantes",  required=False, )
    reprises_exploitation = fields.Float(string=u"Reprises d'exploitation",  required=False, )
    reprises_financiere = fields.Float(string=u"Reprises financières",  required=False, )
    reprises_non_courante = fields.Float(string=u"Reprises Non courantes",  required=False, )
    provisions_id = fields.Many2one(comodel_name="provisions", string="Provisions", required=False, )