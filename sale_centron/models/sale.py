# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    company_id = fields.Many2one('res.company', domain=lambda self: [('id', 'in', self.env.user.company_id.ids)])
