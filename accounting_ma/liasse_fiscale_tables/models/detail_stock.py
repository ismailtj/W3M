# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DetailStock(models.Model):
    _name = 'detail.stock'
    _description = 'Detail Stock'

    name = fields.Char(string=u"Nom",default="ETAT DETAIL DES STOCKS",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal',copy=False)
    detail_stock_line_ids = fields.One2many(comodel_name="detail.stock.line", inverse_name="detail_stock_id",
                                            string="Lignes", required=False, copy=True, )

    _sql_constraints = [
        ('unique_fy', 'UNIQUE(fy_n_id)', 'Un autre tableau existe pour le meme exercice!'),
    ]

class DetailStockLine(models.Model):
    _name = 'detail.stock.line'
    _description = 'LIGNES Detail Stock'

    name = fields.Char(string=u"Stock",required=True,)
    fy_n_id = fields.Many2one('date.range', 'Exercice fiscal')
    code = fields.Char(string=u"Code", required=True, )
    montant_brut_stock_final = fields.Float(string=u"Stock Final Stock Final",  required=False, )
    provisions_stock_final = fields.Float(string=u"Stock Final Provision pour dépréciation",  required=False, )
    montant_net_stock_final = fields.Float(string=u"Stock Final Montant net",  required=False, )
    montant_brut_stock_initial = fields.Float(string=u"Stock Initial Stock Final",  required=False, )
    provisions_stock_initial = fields.Float(string=u"Stock Initial Provision pour dépréciation",  required=False, )
    montant_net_stock_initial = fields.Float(string=u"Stock Initial Montant net",  required=False, )
    detail_stock_id = fields.Many2one(comodel_name="detail.stock", string=u"Detail Stock", required=False, )