# -*- encoding: utf-8 -*-

from odoo import models,fields, api
from odoo.tools.float_utils import float_round

#from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx


class DeclarationTvaXlsx(models.AbstractModel):
    _name = 'report.declaration.tva.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, declarations):
        for declaration in declarations:
            sheet = workbook.add_worksheet(u"Décaissement")
            sheet.set_column('A:B', 20)
            sheet.set_column('C:M', 10)
            bold = workbook.add_format({'bold': True})
            number_format = workbook.add_format()
            number_format.set_num_format('# ##0.00')
            color = workbook.add_format({'bg_color': '#DCDCDC', 'bold': True})
            color.set_align('center')
            color.set_align('vcenter')
            color1 = workbook.add_format({'bg_color': '#DCDCDC', 'bold': True})
            color.set_align('left')
            sheet.write('A1', u'Déclaration', color1)
            sheet.write('B1',declaration.name, color)
            sheet.write('A2', u'Société', color1)
            sheet.write('B2', str(declaration.company_id.name), color)

    #########################   Décaissement
            sheet.write('A5', u'N° facture', color)
            sheet.write('B5', u'Fournissseur', color)
            sheet.write('C5', u'IF', color)
            sheet.write('D5', u'ICE', color)
            sheet.write('E5', u'Description', color)
            sheet.write('F5', u'Montant HT', color)
            sheet.write('G5', u'Montant TVA', color)
            sheet.write('H5', u'Montant TTC', color)
            sheet.write('I5', u'Date facture', color)
            sheet.write('J5', u'Date paiement', color)
            sheet.write('K5', u'Méthode de paiement', color)
            sheet.write('L5', u'TVA', color)
            sheet.write('M5', u'Taux de TVA', color)
            i = 6
            for line in declaration.line_ids:
                sheet.write('A'+str(i), str(line.invoice_number))
                sheet.write('B'+str(i), str(line.partner_name))
                sheet.write('C'+str(i), str(line.id_fisc or ''))
                sheet.write('D'+str(i), str(line.ice or ''))
                sheet.write('E'+str(i), line.description)
                sheet.write('F'+str(i), float_round(line.amount_ht, 2),number_format)
                sheet.write('G'+str(i), float_round(line.amount_tva, 2),number_format)
                sheet.write('H'+str(i), float_round(line.amount_ttc, 2),number_format)
                sheet.write('I'+str(i), str(line.invoice_date))
                sheet.write('J'+str(i), str(line.paiement_date))
                sheet.write('K'+str(i), line.paiement_type.name or '')
                sheet.write('L'+str(i), str(line.tax_id.name))
                sheet.write('M'+str(i), str(line.tax_rate))
                i+=1
    #########################   Encaissement

            sheet1 = workbook.add_worksheet(u"Encaissement")
            sheet1.set_column('A:B', 20)
            sheet1.set_column('C:J', 10)
            sheet1.write('A1', u'Déclaration', color1)
            sheet1.write('B1', declaration.name, color)
            sheet1.write('A2', u'Société', color1)
            sheet1.write('B2', str(declaration.company_id.name), color)
            sheet1.write('A5', u'Facture', color)
            sheet1.write('B5', u'Client', color)
            sheet1.write('C5', u'Description', color)
            sheet1.write('D5', u'Montant HT', color)
            sheet1.write('E5', u'Montant TVA', color)
            sheet1.write('F5', u'Montant TTC', color)
            sheet1.write('G5', u'Date facture', color)
            sheet1.write('H5', u'Date de paiement', color)
            sheet1.write('I5', u'TVA', color)
            sheet1.write('J5', u'Taux de TVA', color)
            i = 6
            for line in declaration.encaissement_ids:
                sheet1.write('A' + str(i), str(line.invoice_number))
                sheet1.write('B' + str(i), str(line.partner_id.name))
                sheet1.write('C' + str(i), line.description)
                sheet1.write('D' + str(i), float_round(line.amount_ht, 2),number_format)
                sheet1.write('E' + str(i), float_round(line.amount_tva, 2),number_format)
                sheet1.write('F' + str(i), float_round(line.amount_ttc, 2),number_format)
                sheet1.write('G' + str(i), line.invoice_date)
                sheet1.write('H' + str(i), line.paiement_date)
                sheet1.write('I' + str(i), str(line.tax_id.name))
                sheet1.write('J' + str(i), line.tax_rate)
                i+=1
            #########################   Encaissement

            sheet2 = workbook.add_worksheet(u"TVA facturée")
            sheet2.set_column('A:A', 15)
            sheet2.set_column('B:C', 10)
            sheet2.write('A1', u'Déclaration', color1)
            sheet2.write('B1', declaration.name, color)
            sheet2.write('A2', u'Société', color1)
            sheet2.write('B2', str(declaration.company_id.name), color)
            sheet2.write('A5', u'TVA', color)
            sheet2.write('B5', u'Base TVA', color)
            sheet2.write('C5', u'Montant TVA', color)
            i = 6
            for line in declaration.payable_tva_ids:
                sheet2.write('A' + str(i), str(line.tax_id.name))
                sheet2.write('B' + str(i), float_round(line.amount_ht, 2),number_format)
                sheet2.write('C' + str(i), float_round(line.amount, 2),number_format)
                i+=1
            sheet3 = workbook.add_worksheet(u"TVA récupérable")
            sheet3.set_column('A:A', 20)
            sheet3.set_column('B:C', 10)
            sheet3.write('A1', u'Déclaration', color1)
            sheet3.write('B1', declaration.name, color)
            sheet3.write('A2', u'Société', color1)
            sheet3.write('B2', str(declaration.company_id.name), color)
            sheet3.write('A5', u'TVA', color)
            sheet3.write('B5', u'Base TVA', color)
            sheet3.write('C5', u'Montant TVA', color)
            i = 6
            for line in declaration.receivable_tva_ids:
                sheet3.write('A' + str(i), str(line.tax_id.name))
                sheet3.write('B' + str(i), float_round(line.amount_ht, 2),number_format)
                sheet3.write('C' + str(i), float_round(line.amount, 2),number_format)
                i += 1
            sheet4 = workbook.add_worksheet(u"TVA à payer")
            sheet4.set_column('A:A', 25)
            sheet4.set_column('B:C', 10)
            sheet4.write('A1', u'Déclaration', color1)
            sheet4.write('B1', declaration.name, color)
            sheet4.write('A2', u'Société', color1)
            sheet4.write('B2', str(declaration.company_id.name), color)
            sheet4.write('A4', u'Total TVA client ', color1)
            sheet4.write('B4', float_round(declaration.sum_receivable, 2),number_format )
            sheet4.write('A5', u'Total TVA fournisseur', color1)
            sheet4.write('B5', float_round(declaration.sum_payable, 2),number_format)
            sheet4.write('A6', u'Crédit de la période précédente', color1)
            sheet4.write('B6', float_round(declaration.sum_credit, 2),number_format)
            sheet4.write('A7', u'TVA à déclarer ', color1)
            sheet4.write('B7', float_round(declaration.to_be_payed, 2),number_format )


#DeclarationTvaXlsx('report.declaration.tva.xlsx', 'tva.declaration')