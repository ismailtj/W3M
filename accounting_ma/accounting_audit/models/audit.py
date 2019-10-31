# -*- coding: utf-8 -*-

# from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
from odoo import models,fields, api
from odoo.exceptions import ValidationError


class AuditReport(models.Model):
    _name = "audit.report"
    _description = "Rapport audit"

    name = fields.Char('Nom', required=True)
    rapport_ids = fields.Many2many('audit.engin', 'audit_report_rel', 'audit_report_id', 'audit_id', 'Rapports')

    @api.multi
    def report_print(self):
        self.ensure_one()
        report_list = []
        for record in self:
            for report in record.rapport_ids:
                report_list.append(report.report_id.id)
        # return self.env['report'].get_action(self.env['report.engin'].browse(report_list), 'report.engin.xlsx')

        return self.env['ir.actions.report']._get_report_from_name('report.engin.xlsx').report_action(self.env['report.engin'].browse(report_list))


class AuditEngin(models.Model):
    _name = "audit.engin"
    _description = "Audit Engin"

    name = fields.Char(u'Nom', required=True)
    line_ids = fields.One2many(comodel_name='audit.line', inverse_name='report_id',
                                     string=u'Lignes')
    python = fields.Text(string='Code lien')

    @api.multi
    def print_values(self):
        for rec in self:
            for line in rec.line_ids:
                print(line.name, line.get_cell_value())


class AuditLine(models.Model):
    _name = "audit.line"
    _description = "Lignes Audit"
    _order = 'report_id desc, sequence, id'

    #TODO case of Excel formulas
    @api.one
    def get_cell_value(self):
        value = False
        for formula in self.formulas_ids:
            print("formula", formula)
            op = 1
            if formula.op == 'minus':
                op = -1
            value += formula.formula_id.eval_formula(formula.domain) * op
        if self.op and self.op == 'minus':
            value *= -1
        return value

    name = fields.Char(u'Nom', required=True)
    type = fields.Selection(string="Type", selection=[('liasse', 'Liasse'),
                                                      ('formule', 'Formule'), ], required=True, )
    link_formula_id = fields.Many2one('formulas.engine', 'Formule', ondelete='cascade')
    model_id = fields.Many2one('ir.model', string='Objet')
    op = fields.Selection([
        ('plus', '+'),
        ('minus', '-'),
    ],
        string="Operateur",
        required=True,
        default='plus')
    formulas_ids = fields.One2many(comodel_name='audit.formula', inverse_name='report_line_id', string=u'Formules')
    report_id = fields.Many2one('audit.engin', 'Rapport audit', ondelete='cascade', readonly=True)
    sequence = fields.Integer(string='Sequence', default=10)


class Auditformula(models.Model):
    _name = "audit.formula"
    _description = "Formule audit"

    formula_id = fields.Many2one('formulas.engine', 'Formule', ondelete='cascade')
    domain = fields.Char('Domaine', default='[]')
    report_line_id = fields.Many2one('audit.line', 'Ligne audit', ondelete='cascade', readonly=True)
    op = fields.Selection([
        ('plus', '+'),
        ('minus', '-'),
    ],
        string="Operateur",
        required=True,
        default='plus')
