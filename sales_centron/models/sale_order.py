# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def button_contract_dummy(self):
        self.ensure_one()
        pty = self.contract_amount_untax / self.amount_untaxed
        if pty == 1.0 :
            return True
        for line in self.order_line:
            line.price_unit = pty * line.price_unit

    @api.depends('order_line.price_total', 'contract_amount_tax')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                # FORWARDPORT UP TO 10.0
                if order.company_id.tax_calculation_rounding_method == 'round_globally':
                    price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
                    taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                                    product=line.product_id, partner=order.partner_shipping_id)
                    amount_tax += sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
                else:
                    amount_tax += line.price_tax
            order.update({
                'amount_untaxed': order.pricelist_id.currency_id.round(amount_untaxed),
                'amount_tax': order.pricelist_id.currency_id.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
                'contract_order_diff': amount_untaxed + amount_tax - order.contract_amount_tax
            })

    contract_amount_untax = fields.Monetary(string='Untaxed Contract Amount',  track_visibility='always')

    contract_amount_tax = fields.Monetary(string='taxed Contract Amount',  track_visibility='always')

    contract_order_diff = fields.Monetary(string='Contract/Order Diff',  store=True,
                                          readonly=True, compute='_amount_all', track_visibility='always')

    _sql_constraints = [
        ('unique_name', 'unique (name)', u'销售订单号必须是唯一的!')
    ]
