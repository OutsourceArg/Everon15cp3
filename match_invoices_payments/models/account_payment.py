# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def reconciliar_pagos(self):
        print('self:',self)
        if not self:
            print('self:',self)
            print("self.env['account.payment'].search([('state','=','posted'),('is_reconciled','!=',True)]):",self.env['account.payment'].search([('state','=','posted'),('is_reconciled','!=',True)]))
            self=self.env['account.payment'].search([('state','=','posted'),('is_reconciled','!=',True)])
        for pago in self.filtered(lambda v: v.ref!=False):
            print('pago:',pago)
            asiento_pago_a_imputar=self.env["account.move.line"].search([("move_id","=",pago.move_id.id),('account_internal_type','in',['receivable', 'payable']),('reconciled','=',False)],limit=1)
            print('asiento_pago_a_imputar:',asiento_pago_a_imputar)
            invoice=self.env['account.move'].search([('name','=',pago.ref),('state','=','posted'),('payment_state','in',['not_paid','partial'])],limit=1)
            print('invoice:',invoice)
            if invoice and asiento_pago_a_imputar:
                print('entroooooooooooooooo')
                invoice.js_assign_outstanding_line(asiento_pago_a_imputar.id)
                self.env.cr.commit()
