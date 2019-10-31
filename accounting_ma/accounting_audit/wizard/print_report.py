# -*- coding: utf-8 -*-
from odoo import models, api,fields , _
from openerp.exceptions import UserError
from lxml import etree
import base64
import zipfile
from openerp.tools.safe_eval import safe_eval
import datetime

class report_audit_result_lines(models.Model):
    _name = "report.audit.result.lines"
    _description = "Resultat audit (ligne)"

    name = fields.Char(u'Nom',readonly=True)
    result_id = fields.Many2one('report.audit.results','Audit',readonly=True)
    value = fields.Float(readonly=True)
    link = fields.Char("Lien",readonly=True)

    @api.multi
    def generate_link(self):
        self.ensure_one()
        for record in self:
            return safe_eval(record.link)

class report_audit_results(models.Model):
    _name = "report.audit.results"
    _description = "Resultat audit"

    name = fields.Char(u'Nom',required=True,readonly=True)
    line_ids = fields.One2many(comodel_name='report.audit.result.lines', inverse_name='result_id',
                                     string=u'Résultat',readonly=True)
    status = fields.Boolean(readonly=True)
    diff = fields.Float('Difference',readonly=True)
    report_id = fields.Many2one('report.audit.results','Audit',readonly=True)


class PrintReport(models.TransientModel):

    _name = "report.audit.print"
    _description = "Report engin print"

    report_id = fields.Many2one('audit.report','Rapport')
    fy_n_id = fields.Many2one('date.range','Exercice fiscal')
    result_ids = fields.One2many(comodel_name='report.audit.results', inverse_name='report_id',
                               string=u'Résultat',readonly=True)

    @api.multi
    def print_report(self):
        audit_res_obj =self.env['report.audit.results']
        audit_res_line_obj =self.env['report.audit.result.lines']
        self.ensure_one()
        ex_n = self.fy_n_id.id
        if not self.fy_n_id.previous_fiscal_year:
            raise UserError(_(
                "Merci de préciser l'exercice précédent pour l'exercice choisi!"))
        ex_n_1 = self.fy_n_id.previous_fiscal_year.id
        for record in self:
            record.result_ids.unlink()
            if record.report_id:
                for report in record.report_id.rapport_ids:
                    print(report.name)
                    audit_id  = audit_res_obj.create({
                        'name': report.name,
                        'status': True,
                        'report_id':self.id
                    })
                    sum = 0.0
                    for line in report.line_ids:
                        link_ids = []
                        if line.link_formula_id.eval_formula("[]"):
                            link_ids = line.link_formula_id.eval_formula("[]").ids
                        link = """{
                            'name': 'Journal Items',
                            'view_type': 'form',
                            'view_mode': 'tree,form',
                            'res_model': %s,
                            'view_id': False,
                            'type': 'ir.actions.act_window',
                            'domain': [('id', 'in',%s)],
                            #'res_id':1,
                        }"""%("'"+str(line.model_id.model)+"'",link_ids)
                        audit_res_line_obj.create({
                            'name': line.name,
                            'result_id' : audit_id.id,
                            'link':link,
                            'value': line.with_context(ex_n=ex_n, ex_n_1=ex_n_1).get_cell_value()[0]
                        })
                        sum += line.with_context(ex_n=ex_n, ex_n_1=ex_n_1).get_cell_value()[0]
                    if sum != 0.0:
                        audit_id.write({'status':False,'diff':sum})

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'report.audit.print',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': record.id,
                'views': [(False, 'form')],
                'target': 'new',
            }



