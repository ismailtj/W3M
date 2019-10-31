# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.onchange('date_invoice', 'partner_id', 'amount_total')
    def onchange_invoices_doubles_warning(self):
        if not self.partner_id and not self.date_invoice and not self.amount_total:
            return
        warning = {}

        invoices = self.search([['date_invoice', '=', self.date_invoice],
                                ['partner_id', '=', self.partner_id.id],
                                ['amount_total', '=', self.amount_total],
                                ['type', '=', self.type],
                                ])

        if invoices:
            title = "Avertissement"
            message = u"Il semblerai qu'une facture identique existe déjà. Êtes vous sur de vouloir continuer?"
            warning['title'] = title
            warning['message'] = message
            return {'warning': warning}
        return {}
