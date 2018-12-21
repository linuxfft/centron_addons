# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def _sales_centron_count(self):
        r = {}
        domain = [
            ('state', 'in', ['sale', 'done']),
            ('product_id', 'in', self.ids),
        ]
        for group in self.env['sale.order.line'].read_group(domain, ['product_id', 'product_uom_qty', 'qty_delivered'], ['product_id']):
            r[group['product_id'][0]] = group['qty_delivered'] - group['product_uom_qty']
        for product in self:
            product.sales_centron_count = r.get(product.id, 0)
        return r

    sales_centron_count = fields.Integer(compute='_sales_centron_count', string='# Sales')

    @api.multi
    def _purchase_centron_count(self):
        r = {}
        domain = [
            ('state', 'in', ['purchase', 'done']),
            ('product_id', 'in', self.mapped('id')),
        ]
        for group in self.env['purchase.order.line'].read_group(domain, ['product_id', 'product_qty', 'qty_received'], ['product_id']):
            r[group['product_id'][0]] = group['product_qty'] - group['qty_received']
        for product in self:
            product.purchase_centron_count = r.get(product.id, 0)
        return r

    purchase_centron_count = fields.Integer(compute='_purchase_centron_count', string='# Purchases')