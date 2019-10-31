# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    is_acompte = fields.Boolean(string=u"Facture acompte?")