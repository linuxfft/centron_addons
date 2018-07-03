# -*- coding: utf-8 -*-
from odoo import http

# class SalesCentron(http.Controller):
#     @http.route('/sales_centron/sales_centron/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_centron/sales_centron/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_centron.listing', {
#             'root': '/sales_centron/sales_centron',
#             'objects': http.request.env['sales_centron.sales_centron'].search([]),
#         })

#     @http.route('/sales_centron/sales_centron/objects/<model("sales_centron.sales_centron"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_centron.object', {
#             'object': obj
#         })