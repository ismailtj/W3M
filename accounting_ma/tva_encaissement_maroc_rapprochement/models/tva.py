# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TvaDeclaration(models.Model):
    _inherit = "tva.declaration"

    statement_ids = fields.Many2many('account.bank.statement', string=u'Relevés')

    @api.multi
    def get_payment_moves(self):
        move_obj = self.env['account.move']
        move_line_obj = self.env['account.move.line']
        move_line_domain = [
            ('statement_id', 'in', self.statement_ids.ids),
            ('journal_id.type', '=', 'bank')]
        move_line_ids = move_line_obj.search(move_line_domain)

        move_bank_ids = move_line_ids.mapped('move_id')
        domain = [('date', '>=', self.period_id.date_start),
                  ('date', '<=', self.period_id.date_end),
                  ('journal_id.type', '=', 'cash')]
        move_ids = move_obj.search(domain)
        move_ids = move_ids | move_bank_ids
        return move_ids