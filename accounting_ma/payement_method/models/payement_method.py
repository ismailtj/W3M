# -*- encoding: utf-8 -*-

from odoo import models,fields, api

class PayementMethod(models.Model):
    _name = 'payement.method'

    name = fields.Char(string=u'Nom')
    code = fields.Char(string=u'Code')

class account_move_line(models.Model):
    _inherit = "account.move.line"

    payement_method_id = fields.Many2one(comodel_name='payement.method',
                                  string=u'Methode de paiement',readonly=True)

class account_payment(models.Model):
    _inherit = "account.payment"

    payement_method_id = fields.Many2one(comodel_name='payement.method',
                                  string=u'Methode de paiement')

    def _create_payment_entry(self, amount):
        res = super(account_payment,self)._create_payment_entry(amount)
        for mv in res.line_ids:
            mv.payement_method_id = self.payement_method_id
        return res
