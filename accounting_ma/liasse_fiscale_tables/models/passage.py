# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AffectationResultatsIntervenue(models.Model):
    _name = 'liasse.passage'
    _description = 'AFFECTATION DES RESULTATS INTERVENUE'

    name = fields.Char(string=u"Nom",default="PASSAGE DU RESULTAT NET COMPTABLE AU RESULTAT NET FISCAL",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)

    benifice_net_1 = fields.Float(u'Bénéfice net comptable')
    perte_nette_1 = fields.Float(u'Perte nette comptable')

    re_fy_courante_ids = fields.One2many(comodel_name="passage.line1", inverse_name="passage_id", string="II. REINTEGRATIONS FISCALES COURANTE", required=False,)
    re_fy_non_courante_ids = fields.One2many(comodel_name="passage.line2", inverse_name="passage_id", string="II. REINTEGRATIONS FISCALES NON COURANTE", required=False,)
    de_fy_courante_ids = fields.One2many(comodel_name="passage.line3", inverse_name="passage_id", string="III. DEDUCTIONS FISCALES COURANTE", required=False,)
    de_fy_non_courante_ids = fields.One2many(comodel_name="passage.line4", inverse_name="passage_id", string="III. DEDUCTIONS FISCALES NON COURANTE", required=False,)

    benifice_brut_1 = fields.Float(u'Bénéfice brut fiscal')
    deficit_brut_1 = fields.Float(u'Déficit brut fiscal')

    exercice_n_4 = fields.Float(u'Exercice (n-4)')
    exercice_n_3 = fields.Float(u'Exercice (n-3)')
    exercice_n_2 = fields.Float(u'Exercice (n-2)')
    exercice_n_1 = fields.Float(u'Exercice (n-1)')
    amortissement = fields.Float(u'Amortissement')

    benifice_net_a_c_1 = fields.Float(u'Bénéfice net fiscal (A-C)')
    deficit_net_b_1 = fields.Float(u'Déficit net fiscal (B)')

    amortissement_1 = fields.Float(u'Cumul des amortissements fiscalement différés')

    exercice_n_4_1_c = fields.Float(u'CUMUL Exercice (n-4)')
    exercice_n_3_1_c = fields.Float(u'CUMUL Exercice (n-3)')
    exercice_n_2_1_c = fields.Float(u'CUMUL Exercice (n-2)')
    exercice_n_1_1_c = fields.Float(u'CUMUL Exercice (n-1)')

    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class passageLine1(models.Model):
    _name = 'passage.line1'
    _description = 'Passage line 1'

    name = fields.Char(string=u"Description",required=True,)
    montant_1 = fields.Float(string=u"Montant",  required=False, )
    passage_id = fields.Many2one(comodel_name="liasse.passage", string="Passage", required=False, )

class passageLine2(models.Model):
    _name = 'passage.line2'
    _description = 'Passage line 2'

    name = fields.Char(string=u"Description",required=True,)
    montant_1 = fields.Float(string=u"Montant",  required=False, )
    passage_id = fields.Many2one(comodel_name="liasse.passage", string="Passage", required=False, )

class passageLine3(models.Model):
    _name = 'passage.line3'
    _description = 'Passage line 3'

    name = fields.Char(string=u"Description", required=True,)
    montant_1 = fields.Float(string=u"Montant",  required=False, )
    passage_id = fields.Many2one(comodel_name="liasse.passage", string="Passage", required=False, )

class passageLine4(models.Model):
    _name = 'passage.line4'
    _description = 'Passage line 4'

    name = fields.Char(string=u"Description", required=True,)
    montant_1 = fields.Float(string=u"Montant",  required=False, )
    passage_id = fields.Many2one(comodel_name="liasse.passage", string="Passage", required=False, )