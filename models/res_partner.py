from odoo import models, fields


class SpanishName(models.Model):
    _inherit = 'res.partner'

    pos_due_limit = fields.Integer(string='POS Due Limit')

    def find_due_limit(self, current_client):
        customer_account = self.env['pos.payment.method'].search([('split_transactions', '=', True)])
        for rec in customer_account:
            pos_payment = self.env['pos.payment'].search([('payment_method_id', '=', rec.id)])
            # print(pos_payment)
            for dec in pos_payment:
                pos_order = self.env['pos.order'].search(
                    [('id', '=', dec.pos_order_id.id), ('partner_id', '=', current_client)])
                # print(pos_order)
                for koc in pos_order:
                    total_amount = koc.amount_paid
                    # print(total_amount)
                    return total_amount
