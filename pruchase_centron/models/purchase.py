# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    act_company_id = fields.Many2one('res.company', '实际业务单据公司',
                                     default=lambda self: self.env['res.company']._company_default_get('purchase.order'))


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    order_id = fields.Many2one('purchase.order', 'Purchase Order', readonly=True)

    def _select(self):
        return super(PurchaseReport, self)._select() + ", s.id as order_id"

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ", s.id"
