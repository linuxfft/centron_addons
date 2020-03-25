# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    category_id = fields.Many2one('product.category', string='Product Category',
                                  related='product_id.categ_id', readonly=True, store=True)

